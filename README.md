# Digital-Grinnell/collectionbuilder-csv

This is a `fork` of [CollectionBuilder/collectionbuilder-csv](https://github.com/CollectionBuilder/collectionbuilder-csv) with added GC-specific additions from Mark M., Libby C., and others.  

> **This repo should be the basis for ALL (including projects with oral histories!) GC CB projects of the future.**  ~~Note that there is a separate GC template repo for Oral History projects because that's the way the CollectionBuilder folks have structured the underlying code.~~  

> See the WORKFLOW.md document in this repository for guidance when updating this fork AND when creating a new GCCB (Grinnell College Collection Builder) project.  

See it in action at  
## https://victorious-sea-07a73ff10.2.azurestaticapps.net/ 

# Building Locally

Like other CB projects, the website from this repository can be easily built -- assuming your machine has all the necessary CB/Jekyll configuration -- using a simple command of the form:  

```
bundle exec jekyll serve
```

# Development Site as an Azure Static Web App

Likewise, this project has been configured with a corresponding Azure Static Web App to simplify collaboration while demonstrating and testing pre-production deployment.  

The Azure configuration was created following the workflow documented at [Deploy your web app](https://learn.microsoft.com/en-us/azure/static-web-apps/publish-jekyll#deploy-your-web-app).

I choose the `jekyll` (automatically detected) build option rather than `Custom`, and used all the default configuration choices.  I got this workflow file AND added the `env:` section to complete the Azure config...

```yaml
name: Azure Static Web Apps CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened, closed]
    branches:
      - main

jobs:
  build_and_deploy_job:
    if: github.event_name == 'push' || (github.event_name == 'pull_request' && github.event.action != 'closed')
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
          lfs: false
      - name: Build And Deploy
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_<GENERATED_HOSTNAME> }}
          repo_token: ${{ secrets.GITHUB_TOKEN }} # Used for Github integrations (i.e. PR comments)
          action: "upload"
          ###### Repository/Build Configurations - These values can be configured to match your app requirements. ######
          # For more information regarding Static Web App workflow configurations, please visit: https://aka.ms/swaworkflowconfig
          app_location: "/" # App source code path
          api_location: "" # Api source code path - optional
          output_location: "_site" # Built app content directory - optional
          ###### End of Repository/Build Configurations ######
        env: # Add environment variables here
          JEKYLL_ENV: production
          TZ: America/Chicago
 
  close_pull_request_job:
    if: github.event_name == 'pull_request' && github.event.action == 'closed'
    runs-on: ubuntu-latest
    name: Close Pull Request Job
    steps:
      - name: Close Pull Request
        id: closepullrequest
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_<GENERATED_HOSTNAME> }}
          action: "close"
```

Following the aforementioned procedure eventually produced the site https://victorious-sea-07a73ff10.2.azurestaticapps.net.

This workflow uses GitHub Actions to deploy and you can see the status of deployment at https://github.com/Digital-Grinnell/collectionbuilder-csv/actions.

> Note that pushing changes to the `main` branch of this repository will automatically re-build https://victorious-sea-07a73ff10.2.azurestaticapps.net/!  

# Updated Local Clone from Upstream

This is the recommended workflow...  

Here's a breakdown of how to pull changes from the original repository (upstream) to your local clone of a GitHub fork:  

## Add the Original Repository as a Remote (Only Needed Once!)

This step tells your local Git repository about the original repository from which you forked. You can name this remote "upstream" (a common convention).

```zsh
git remote add upstream https://github.com/CollectionBuilder/collectionbuilder-csv
```

In the above command I replaced ORIGINAL-OWNER and ORIGINAL-REPOSITORY with the actual owner and repository name of the original project.  

## Verify the Upstream Remote

You can check if the upstream remote has been added correctly by listing the configured remotes:  

```zsh
git remote -v
```

You should see URLs for both 'origin' (your fork) and 'upstream' (the original repository).

## Fetch Changes From the Upstream

This downloads the updates from the original repository but doesn't merge them into your current branch yet.  

```zsh
git fetch upstream
```

If you only want to fetch changes from a specific branch (e.g., main), you can specify it:  

```zsh
git fetch upstream main
```

## Merge the Changes

If you're on your local main (or default) branch:  

```zsh
git checkout main        # or your default branch
git merge upstream/main  # or upstream/your-default-branch
```

This will merge the fetched changes from the upstream's main (or default) branch into your local main (or default) branch. If you're on a feature branch and want to incorporate the latest upstream changes:
It's often recommended to first update your local main (or default) branch, then rebase your feature branch on top of it to maintain a cleaner history.  

```zsh
git checkout main
git merge upstream/main  # or git pull upstream main (equivalent to fetch + merge)
git checkout your-feature-branch
git rebase main
```

## Resolve Conflicts (If Any)

If there are conflicts during the merge, Git will notify you. You'll need to manually resolve these conflicts in the conflicting files.  Push the updated changes to your fork on GitHub:  

```zsh
git push origin main  # or git push origin your-branch-name
```

This updates your online fork with the changes you've pulled from the upstream.  

## Special Oral History Considerations

Note that oral history objects (any audio or video objects with transcription) need some additional attention and metadata.  However, you do NOT need to add these REQUIRED metadata fields to your `_data/config-metadata.csv` file!   The additional column headings and metadata required in your CSV file is:  

  - objectid: Unique identifier for each item
  - title: Title of the oral history<sup>*</sup>
  - format: Should include “oral history” for transcript items
  - transcript-file: Name of the transcript file (without path)

<sup>*</sup>The `title` field already exists in nearly every CB project and it's OK that `title` appears in the `_data/config-metadata.csv` file.  

Final oral history note:  Your `transcript` filenames must EXACTLY match the names of the CSV files found in the `_data/transcripts` directory.  Don't put these files anywhere else, don't store them remotely and specify URLs, and don't include the `path` in your metadata file's `transcript-file` column, just the name of the file (with its extension) as it appears in your `_data/transcripts` directory.     

## Suggested Metadata CSV Column Headings

The following CSV column headings were pulled from the `_data/grinnell-CB-CSV-demo.csv` file in this repository.  This is a `COMPLETE` list of fields that makes ALL features and options possible, including 6 fields for whatever you want!  Have fun with it!    

```
objectid,parentid,title,creator,date,description,focused_event,subject,people,location,latitude,longitude,source,identifier,type,format,language,display_template,WORKSPACE1,WORKSPACE2,WORKSPACE3,object_location,image_small,image_thumb,image_alt_text,object_transcript,bio,pdf,temp1,temp2,temp3,rights,rightsstatement
```

## Markdown Objects

No longer supported here since .md files cannot be served from web addressable storage.  Convert your .md files to .pdf and display those instead.  

~~Added as a Grinnell College feature, this project has the ability to render `markdown` (.md) documents as objects using a `display_template` value of `markdown`.  Note that .md files used in this manner MUST be stored locally in the project because, like `transcript` files, cloud storage will generally NOT serve a raw .md file for consumption by applications like _CollectionBuilder_.   Also, make sure your .md files contain `front matter`!  Markdown files without front matter appear as an empty span in the output!~~  


# What follows is from the original `CollectionBuilder/collectionbuilder-csv` repository.
**BEWARE! This information may be outdated!** 

# CollectionBuilder-CSV

CollectionBuilder-CSV is a robust and flexible "stand alone" template for creating digital collection and exhibit websites using Jekyll and a metadata CSV.
Driven by your collection metadata, the template generates engaging visualizations to browse and explore your objects.
The resulting static site can be hosted on any basic web server (or built automatically using GitHub Actions).

Visit the [CollectionBuilder Docs](https://collectionbuilder.github.io/cb-docs/) for step-by-step details for getting started and building collections!

## Brief Overview of Building a Collection

The [CollectionBuilder Docs](https://collectionbuilder.github.io/cb-docs/) contain detailed information about building a collection from start to finish--including installing software, using Git/GitHub, preparing digital objects, and formatting metadata.
However, here is a super quick overview of the process:

- Make your own copy of this template repository by clicking the green "Use this Template" button on GitHub (see [repository set up docs](https://collectionbuilder.github.io/cb-docs/docs/repository/)). This copy of the template is the starting point for your "project repository", i.e. the source code for your digital collection site!
- Prepare your collection metadata following the CB-CSV template (see our demo [metadata template on Google Sheets](https://docs.google.com/spreadsheets/d/1nN_k4JQB4LJraIzns7WcM3OXK-xxGMQhW1shMssflNM/edit?usp=sharing) and [metadata docs](https://collectionbuilder.github.io/cb-docs/docs/metadata/csv_metadata/)). Your metadata will include links to your digital files (images, pdfs, videos, etc) and thumbnails wherever they are hosted.
- Add your metadata as a CSV to your project repository's "_data" folder (see [upload metadata docs](https://collectionbuilder.github.io/cb-docs/docs/metadata/uploading/)).
- Edit your project's "_config.yml" with your collection information (see [site configuration docs](https://collectionbuilder.github.io/cb-docs/docs/config/)). Additional customization is done via a theme file, configuration files, CSS tweaks, and more--however, once your "_config.yml" is edited your site is ready to be previewed. 
- Generate your site using Jekyll! (see docs for how to [use Jekyll locally](https://collectionbuilder.github.io/cb-docs/docs/repository/generate/) and [deploy on the web](https://collectionbuilder.github.io/cb-docs/docs/deploy/))

Please feel free to ask questions in the main [CollectionBuilder discussion forum](https://github.com/CollectionBuilder/collectionbuilder.github.io/discussions).

----------

## CollectionBuilder 

<https://collectionbuilder.github.io/>

CollectionBuilder is a project of University of Idaho Library's [Digital Initiatives](https://www.lib.uidaho.edu/digital/) and the [Center for Digital Inquiry and Learning](https://cdil.lib.uidaho.edu) (CDIL) following the [Lib-Static](https://lib-static.github.io/) methodology. 
Powered by the open source static site generator [Jekyll](https://jekyllrb.com/) and a modern static web stack, it puts collection metadata to work building beautiful sites.

The basic theme is created using [Bootstrap](https://getbootstrap.com/).
Metadata visualizations are built using open source libraries such as [DataTables](https://datatables.net/), [Leafletjs](http://leafletjs.com/), [Spotlight gallery](https://github.com/nextapps-de/spotlight), [lazysizes](https://github.com/aFarkas/lazysizes), and [Lunr.js](https://lunrjs.com/).
Object metadata is exposed using [Schema.org](http://schema.org) and [Open Graph protocol](http://ogp.me/) standards.

Questions can be directed to **collectionbuilder.team@gmail.com**

## License

CollectionBuilder documentation and general web content is licensed [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/). 
This license does *NOT* include any objects or images used in digital collections, which may have individually applied licenses described by a "rights" field.
CollectionBuilder code is licensed [MIT](https://github.com/CollectionBuilder/collectionbuilder-csv/blob/master/LICENSE). 
This license does not include external dependencies included in the `assets/lib` directory, which are covered by their individual licenses.
