# Creating New Event Pages #
This is a shortened version of the `new_template_documentation` that is only includes the information relevant for people trying to create new pages using the existing Event page template. 
You can see an example on `pages\eventplayboy.md`
1. Copy the Template Stub page
2. Paste it in the `_pages/` folder
3. Rename it with a unique name. 
    >I like to make sure that it remains clear that all pages made with this template are connected so I keep the `event` and add a shortened title for the event, i.e: `eventavw.md`
4. Leave the `---` and the `layout` variable as is. The `layout` should always be the name of the layout file you are using, which in this case is `event`
    ```
        ---
        layout: event
    ```
5. Fill in the variables with the information that you would like
    1. `Title`: This is what will show up as the title of the page.  This is put in quotation marks.

            title: "Playboy Nude-In"
    2. `Featured_image`: Chose the image you would like to use for the top of this page. This is put in quotation marks
        >**NOTE: You have to use a relative file path in the repository OR an externally hosted image link, NOT an object id. If adding to the repository separately, put these images in `_assets/img/`**  

            featured_image: "https://collectionbuilder.blob.core.windows.net/smalls/student_activism/dg_1745010246.jpg"

    3. `Institutional Event`: Add context about the event at Grinnell. This is put in quotation marks. 

         institution_event: "Feminist movements existed along side Anti-War movement and counterculture movements at Grinnell College. Students created the Women’s Liberation groups and sought recognition for .....

    4. `us_event`: This is the where I added context about the event outside of Grinnell College. This is put in quotation marks. 
            
            us_event: "This protest emerged during the second-wave feminist movement of the 1960s to 1980s, which focused on achieving substantive equality-ensuring policies and practices addressed systemic discrimination to produce equitable outcomes...
        
    5. `focused_event`: This is where I set the metadata variable to limit the browse feature to just the items marked with that exact metadata tag in the "focused_activism" section of my metadata. This is put in quotation marks.
            
            focused_event: "Playboy Nude-in"
    
6. Add the permalink
    >Set the permalink as something that makes sense for the event, like the title of the event. This becomes part of the URL for the page, so it is really important! 
    ```
        permalink: /nude-in.html
        ---
    ``` 

## Add Page to Navigation ##
Your new page exists now, but for people to actually find it, you need to add it to the navigation. 
>For this exhibit, I put all the "Event" pages under the same `dropdown_parent`. To learn more about configuring navigation, go to https://collectionbuilder.github.io/cb-docs/docs/customization/config-nav/
1. Go to the `_data/config-nav.csv` file in your repository

    - Mine looks like this: 
    ```
        display_name,stub,dropdown_parent
        Home,/,
        Browse,/browse.html,
        Browse by Movements,/subjects.html,
        Movement Details,,
        Anti-Vietnam War,/anti-vietnam.html,Movement Details
        Playboy Nude-in,/nude-in.html,Movement Details
        Nisei Program,/nisei.html,Movement Details
        LGBTQ+ Activism,/lgbtq.html,Movement Details
        Locations,/locations.html,
        Map,/map.html,
        Timeline,/timeline.html,
        Data,/data.html,
        About,/about.html,
    ```
    - This is just a csv file, so its nothing to be afraid of! 

    >Order matters here! The order they show up as in this CSV is the order they will show up on the navigation bar on the website. 

2. Enter a new line to create the dropdown parent (if the parent does not exist yet)
    - A dropdown parent creates a vertical pop-down menu with more navigation options. This keeps the navigation bar from being too cluttering while still allowing users to find pages. 
    - To create one, simply write the display_name followed by two commas. 

        Movement Details,,

    >Notice how I did not add a stub (or permalink) here. This means that this section of the navigation menu will not be clickable. You can add a stub to make it clickable, and it can still be a dropdown_parent.
3. Enter a new line, and create the entry for the new page you made
    - Enter in the `display_name`followed by a comma `,`, the permalink or `stub` followed by another `,` and the `dropdown_parent`. 
        >**DO NOT add spaces before or after commas!**

            Playboy Nude-in,/nude-in.html,Movement Details

        -The `display_name` is seen by users, so make sure it is descriptive, complete, and spelled correctly. Spaces are fine here! 
        -Copy the `permalink` from the page's markdown file (detailed in *Creating Pages with the Template*, step 6) and paste it. It needs to be **EXACTLY** as it appears on the markdown page!!!
        -Copy the `display_name` of the `dropdown_parent` and paste it at the end. This needs to be **EXACTLY** the same value what is listed in the parent's `display_name` value. 

Save all the files that you edited in your repository. You are now the proud creator of unique template pages! 