# Hosting CollectionBuilder on Sites@Grinnell
Instructions for hosting a CollectionBuilder site on Reclaim Hosting cPanel
NOTE: I am having a TON of issues today making this work, but it worked yesterday. 
1. Create your desired subdomain on cPanel
2. Download and Deploy CollectionBuilder
	1. Be sure to add your new domain into the URL section of the `config.yml` file of your CollectionBuilder Repository
	2. In the terminal of whichever software you are using for editing your CollectionBuilder, enter `JEKYLL_ENV=production bundle exec jekyll build`
	3.  Copy and Download all  CollectionBuilder files on to your computer.  
	4. *Note: I should be able to just move all the files from the _site folder of the Collection Builder files, and skip all the Ruby junk, but I could not get this to work.*
3. . FTP Accounts
	2. Because you have to move all the CollectionBuilder Files to your domain in exact structure, you will need to do an FTP because the file manager on cPanel doesn't allow for importing whole files. 
	3. under the "Files" section of cPanel is a "FTP Accounts" button
	4. Fill in the log in details
	5. choose the subdomain
	6. set a password and store the password 
	7. set the directory as the file path to your domain directory
		1. You can find this by going to the "File Manager" section and finding the subdomain's folder
		2. Be sure to add the parent file name, which is typically `/home/username`, where the username is your username, in front of the file. For example, my directory file name is `/home/libbylea/cbtest2electricboogaloo.sites.grinnell.edu`
	8. Click Create FTP Account
4. FTP Set up
	1. *Note: I am having major issues getting my FTP to work today so godspeed*
	2. Download either [CyberDuck](https://cyberduck.io/)  or [CoreFTP](https://go.cpanel.net/coreftp). 
	3. In cPanel "FTP Accounts", click the "configure FTP client" link by the account you are using. 
	4. Click on the "FTP Configuration"
	5. If you run into security or error messages, click "continue"
	6. To login, us the password that you created for the FTP account
5. Copy the CollectionBuilder files to the FTP and upload. 
6. Open the "File Manger" in cPanel and check that the files uploaded
7. Set Up Ruby on your Domain
	1. On cPanel, go to the "Software" section and click on the "Setup Ruby App"
	2. set the App Directory to the subdomain file folder. You will need to essentially create a new folder by adding an extension to the end of the subdomain file folder name. For example, mine is `/home/libbylea/cbtest.libbylearnsdh.sites.grinnell.edu/jekyll`
	3. Set the app Domain/URI to the domain that you are editing
	4. Click Set up. This will take a few moments
	5. You will now see the application under "Existing Applications"
	6. **Keep track of/ copy the "Command for entering to virtual environment" on the bottom of the box. You will need this later** For example, mine is `source /home/libbylea/rubyvenv/cbtest.libbylearnsdh.sites.grinnell.edu_jekyll/2.6/bin/activate`
8. Terminal Instructions 
	1.  In the "Advanced" box of cPanel tools page, click the "Terminal" option
	2. Once in the terminal, put in your source command. You can only paste by right-clicking and choosing paste. Hit Enter. 
	3. Next, you will need to install the Gems for running Jekyll by entering `gem install jekyll bundler`. This will take a moment
		1. Errors:
			1. Error installing jekyll:
				1. `'Error installing jekyll:The last version of rouge (>= 3.0, < 5.0) to support your Ruby & RubyGems was 3.30.0. Try installing it with gem install rouge -v 3.30.0 and then running the current command again rouge requires Ruby version >= 2.7. The current ruby version is 2.6.4.104`.'
				2. To solve this, simply enter `gem install rouge -v 3.30.0` and then re-run `gem install jekyll bundler`
9. In the file manager, move the CollectionBuilder files to the folder for the subdomain. Typically there is a "public" file, and you should move the files here. Keep track of the file path!! 
10. Run via Ruby
	1. Go back to the "Terminal" under software
	2.  Enter in your source command that you did in step 7. Mine is  `source /home/libbylea/rubyvenv/cbtest.libbylearnsdh.sites.grinnell.edu_jekyll/2.6/bin/activate`
	3. Now enter the following syntax with your `source` command, `&&`, `cd` file path, `&&` and the `jekyll build` command. My looks like this: `/home/libbylea/rubyvenv/cbtest.libbylearnsdh.sites.grinnell.edu_jekyll/2.6/bin/activate && cd /home/cbtest2electricboogaloo.sites.grinnell.edu/public/ && jekyll build
	5. Ensure that you now have a `_site` folder in the file manager. 
	6.  *Note: I am not sure why I have to build it again to make it run correctly. That's just showbiz I guess*
11. Edit the Domain Document root
	1. Go back to your "domain" manager on cPanel. 
	2. Click "manage domain" next to your domain
	3. Under "New Document Root", enter the file path to your `_site` folder. Mine is `/home/libbylea/public_html/cb_CPANEL/_site`
	4. Now your website should be live! 
