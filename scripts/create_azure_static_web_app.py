#!/usr/bin/env python3
"""
Create a new Azure Static Web App for the current repository and print its URL.

What it does:
- Verifies required command-line tools are available
- Resolves the current git branch and repository URL by default
- Creates the Azure resource group if it does not already exist
- Creates or links a new Azure Static Web App to the repository
- Prints the final production URL when the deployment is ready

Usage:
    python3 scripts/create_azure_static_web_app.py \
        --name my-static-app \
        --resource-group my-resource-group

You can also override the repo URL, branch, and build locations if needed.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new Azure Static Web App and print its production URL.",
    )
    parser.add_argument("--name", required=True, help="Azure Static Web App name")
    parser.add_argument(
        "--resource-group",
        required=True,
        help="Azure resource group to create or reuse",
    )
    parser.add_argument(
        "--location",
        default="centralus",
        help="Azure region for the resource group and Static Web App",
    )
    parser.add_argument(
        "--subscription",
        help="Azure subscription name or ID",
    )
    parser.add_argument(
        "--source",
        help="GitHub repository URL. Defaults to the current repo origin URL.",
    )
    parser.add_argument(
        "--branch",
        help="Git branch to deploy. Defaults to the current checked-out branch.",
    )
    parser.add_argument(
        "--app-location",
        default="/",
        help="App source path relative to the repository root",
    )
    parser.add_argument(
        "--api-location",
        default="",
        help="Optional API source path relative to the repository root",
    )
    parser.add_argument(
        "--output-location",
        default="_site",
        help="Build output path relative to the app location",
    )
    parser.add_argument(
        "--sku",
        choices=["Free", "Standard", "Dedicated"],
        default="Free",
        help="Azure Static Web App SKU",
    )
    parser.add_argument(
        "--token",
        help="GitHub repository token. If omitted, the script uses `gh auth token`.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the Azure CLI commands without executing them",
    )
    return parser.parse_args()


def run_command(command: list[str], *, dry_run: bool = False) -> subprocess.CompletedProcess[str]:
    printable = " ".join(shlex_quote(part) for part in command)
    print(f"[CMD] {printable}")
    if dry_run:
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    completed = subprocess.run(
        command,
        check=False,
        text=True,
        capture_output=True,
    )
    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.returncode != 0:
        if completed.stderr:
            print(completed.stderr.rstrip(), file=sys.stderr)
        raise SystemExit(completed.returncode)
    if completed.stderr:
        print(completed.stderr.rstrip(), file=sys.stderr)
    return completed


def shlex_quote(value: str) -> str:
    if not value:
        return "''"
    if re.fullmatch(r"[A-Za-z0-9_./:-]+", value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"


def require_command(command: str) -> None:
    completed = subprocess.run(
        ["/usr/bin/env", "bash", "-lc", f"command -v {command} >/dev/null"],
        check=False,
    )
    if completed.returncode != 0:
        raise SystemExit(f"Required command not found: {command}")


def git_output(args: list[str]) -> str:
    completed = subprocess.run(["git", *args], check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        stderr = completed.stderr.strip() or completed.stdout.strip() or "git command failed"
        raise SystemExit(stderr)
    return completed.stdout.strip()


def normalize_repo_url(remote_url: str) -> str:
    remote_url = remote_url.strip()

    if remote_url.startswith("git@github.com:"):
        path = remote_url.removeprefix("git@github.com:")
        path = path.removesuffix(".git")
        return f"https://github.com/{path}"

    if remote_url.startswith("https://github.com/"):
        return remote_url.removesuffix(".git")

    if remote_url.startswith("http://github.com/"):
        return "https://" + remote_url.removeprefix("http://").removesuffix(".git")

    raise SystemExit(
        "The repository origin remote is not a GitHub URL. Pass --source with a GitHub repo URL."
    )


def current_repo_url() -> str:
    origin = git_output(["remote", "get-url", "origin"])
    return normalize_repo_url(origin)


def current_branch() -> str:
    branch = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    if branch == "HEAD":
        raise SystemExit("Detached HEAD detected. Pass --branch explicitly.")
    return branch


def get_github_token(explicit_token: str | None) -> str:
    if explicit_token:
        return explicit_token.strip()

    require_command("gh")
    completed = subprocess.run(["gh", "auth", "token"], check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        stderr = completed.stderr.strip() or completed.stdout.strip() or "gh auth token failed"
        raise SystemExit(
            "Could not retrieve a GitHub token from `gh auth token`. Pass --token or authenticate gh.\n"
            f"{stderr}"
        )

    token = completed.stdout.strip()
    if not token:
        raise SystemExit("`gh auth token` returned an empty token.")
    return token


def ensure_azure_login() -> None:
    completed = subprocess.run(
        ["az", "account", "show", "--output", "none"],
        check=False,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise SystemExit(
            "Azure CLI is installed, but not logged in. Run `az login` and try again."
        )


def ensure_resource_group(resource_group: str, location: str, dry_run: bool) -> None:
    show = subprocess.run(
        ["az", "group", "show", "--name", resource_group, "--output", "none"],
        check=False,
        text=True,
        capture_output=True,
    )
    if show.returncode == 0:
        print(f"[INFO] Using existing resource group: {resource_group}")
        return

    print(f"[INFO] Creating resource group: {resource_group} ({location})")
    run_command(
        ["az", "group", "create", "--name", resource_group, "--location", location],
        dry_run=dry_run,
    )


def create_static_web_app(args: argparse.Namespace, repo_url: str, branch: str, token: str) -> None:
    command = [
        "az",
        "staticwebapp",
        "create",
        "--name",
        args.name,
        "--resource-group",
        args.resource_group,
        "--location",
        args.location,
        "--source",
        repo_url,
        "--branch",
        branch,
        "--app-location",
        args.app_location,
        "--output-location",
        args.output_location,
        "--sku",
        args.sku,
        "--token",
        token,
    ]

    if args.api_location:
        command.extend(["--api-location", args.api_location])

    if args.subscription:
        command.extend(["--subscription", args.subscription])

    run_command(command, dry_run=args.dry_run)


def lookup_static_web_app_hostname(args: argparse.Namespace) -> str:
    command = [
        "az",
        "staticwebapp",
        "show",
        "--name",
        args.name,
        "--resource-group",
        args.resource_group,
        "--query",
        "defaultHostname",
        "--output",
        "tsv",
    ]
    if args.subscription:
        command.extend(["--subscription", args.subscription])

    completed = subprocess.run(command, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        stderr = completed.stderr.strip() or completed.stdout.strip() or "az staticwebapp show failed"
        raise SystemExit(stderr)

    hostname = completed.stdout.strip()
    if not hostname:
        raise SystemExit("Azure Static Web App was created, but no defaultHostname was returned.")
    return hostname


def main() -> None:
    args = parse_args()

    require_command("git")

    if not args.dry_run:
        require_command("az")
        ensure_azure_login()

    repo_url = normalize_repo_url(args.source) if args.source else current_repo_url()
    branch = args.branch or current_branch()
    token = args.token.strip() if args.token else ("<github-token>" if args.dry_run else get_github_token(None))

    if not args.dry_run:
        ensure_resource_group(args.resource_group, args.location, args.dry_run)
    create_static_web_app(args, repo_url, branch, token)

    if args.dry_run:
        print("[INFO] Dry run complete; no Azure resources were created.")
        return

    hostname = lookup_static_web_app_hostname(args)
    print()
    print(f"Azure Static Web App URL: https://{hostname}")


if __name__ == "__main__":
    main()