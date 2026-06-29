# Creating New Page Templates#
## Background ##
<p> We wanted to create a unique page template that could be easily filled with a featured image of the event, context about the event at Grinnell, context about the event in the US, and a section for browsing materials marked as that event. 
<p>I am NOT a trained developer - everything I do, including this, is a process of trial and error, web searching and asking AI tools for help. I mainly used the CollectionBuilder documentation and Slack channel, Perplexity AI, and good ol' click around and find out to create this. I will make sure to note where I used AI or existing documentation. If it is unclear how I did something, it is because I have no idea what I did. </p>
<p> According to the CollectionBuilder documentation found in /docs/code_design_notes.md:
Template Page Design

Generally CB template pages are made of three parts:

- a "stub" found in "pages" folder, generally in markdown. The stub can contain markdown content and feature includes, but should not generally contain complicated JS.
- a "layout" found in "_layouts" folder, in html. This is the template html that the content will be injected into. Most layouts will have an additional layout of "page" or "default".
- component includes found in "_includes" folder, generally in html. Includes contain modular components of html, JS, and Liquid that add content or code to the page.

To ensure JS is loaded in correct order, JS includes are added via the "_includes/foot.html".
See "docs/foot.md" for details.
## Custom CSS ##
The example of this can be found `_sass\_custom.scss`
I am a silly goose who doesn't have a tech background, so I utilized AI for this. I added some comments to help show what each code chunk does. 
The goal of this section is to create the general look of the page. 
## Layout: HTML ##
The example of this page can be found under `_layouts/event.html`
I utilized a lot AI for this. I added some comments to help show what each code chunk does. 
### Add Header ###
I am not going to pretend I understand this part, but it doesn't work if you do not do this. 
```

    ---
    # collection "Event" page
    layout: page
    custom-foot: js/event-browse-js.html
    ---
    {{content}}

```
### Add HTML content ###
I am not going to pretend I understand this at all, but every time you see `{{ page.[variable] }}`, it is going to bring in information from the Markdown file for the page you are creating. Edit this to match the variable names on the markdown page. 

## Custom Includes item
Again, I had no idea what I was doing here. Evan Williamson, one of developer at University of Idaho who created CollectionBuilder, helped me with this via the Slack Channel. Below is the conversation thread from Slack dated 5/1/25. 
>Libby: Hi all! I am trying to make a page template that gives context and the associated items for different activist movements for a collection on student activism. I would like a browse feature that would be limited to the items associated with the movement (which is marked in the metadata) under the text. Right now, I can only manage to get browse with all the items to show up. Any ideas on how to do this? The html for the page layout is attached. 
*(see event layout)*
>
>Evan: @Libby The final step would be to create a customized version of the "_includes/js/browse-js.html" which includes a filter to limit the metadata to your specific grouping. I would probably create a copy of "_includes/js/browse-js.html" named "_includes/js/event-browse-js.html" to start
>
>Evan: Then on your Event page layout, change the front matter value custom-foot: `js/event-browse-js.html`
>
>Evan: Then in the new event-browse-js.html file, take a look at the top where it sets up the metadata to be used, currently looks like:
```
    {% if site.data.theme.browse-child-objects == true %}
    {%- assign items = site.data[site.metadata] | where_exp: 'item','item.objectid' -%}
    {% else %}
    {%- assign items = site.data[site.metadata] | where_exp: 'item','item.objectid and item.parentid == nil' -%}
    {% endif %}
```
>Evan: Replace those lines with something like: 
```
    {%- assign items = site.data[site.metadata] | where_exp: 'item','item.objectid' | where_exp: 'item', 'item.event == page.focused_event' -%}
```
>Evan: The key is the `where_exp: 'item', 'item.event == page.focused_event'`
>
>Evan: `item.event` you would change "event" to what ever metadata field value you used to mark the related items. `page.focused_event` is pulling the value you have in the page's front matter in your example set up.
>
>Evan:So for the example page with `focused_event: "Anti-Vietnam war"` in the front matter, the where expression will look in all the metadata in the "event" column for "Anti-Vietnam war" and limit it to those items.



## Create Template Stub in "Pages" in Markdown ##
You can see the main Event page `pages\eventtem.md`. I recommend creating a template page and then creating duplicates of that page for each unique page you want to make with this template.
1. Set Layout: This should be the same name as your Layout file
```
    ---
    layout: event
```
**Notice how this line does NOT incase the layout variable (in this case `event`) in quotation marks.**
2. Set your variables 
This is where you will "set" the "variables for each unique page. These variable WILL be incased in quotation marks. **Remember: This is just a template page and will not show on the website so the content doesn't need to be real.** Mine are as follows: 

```
    title: "Event Title"
```
This is where you will give your page a title. 

```
    featured_image: "/path/to/featured_image.jpg"
```
This is where you set the featured image for the page. **NOTE: You have to use a relative file path in the repository OR an externally hosted image link, NOT an object id. If adding to the repository separately, put these images in `_assets/img/`**
```
    institution_event: "Details about the event at our institution."
    us_event: "Details about the event in the general US."
```
These two contain the information that will go in the information boxes we created with the custom css and the html layout page. 

```
    focused_event: "Anti-Vietnam war"
```
This is where I set the metadata variable to limit the browse feature to just the items marked with that exact metadata tag in the "focused_activism" section of my metadata. 

3. Set your permalink
```
    permalink: /cevent.html
    ---
```
This last last line sets the permalink for the page. **Note: This is NOT put in quotation marks**

## Creating Pages with the Template ##
You can see an example on `pages\eventplayboy.md`
1. Copy the Template Stub page
2. Paste it in the `_pages/` folder
3. Rename it with a unique name. 
    >I like to make sure that it remains clear that all pages made with this template are connected so I keep the `event` and add a shortened title for the event, i.e: `eventavw.md`
4. Leave the `---` and the `layout` variable as is. The `layout` should always be the name of the layout file you are using. 
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
