---
title: About
layout: about
permalink: /about.html
# include CollectionBuilder info at bottom
credits: true
# featured-image value can be one objectid for a photo object in this collection, a relative path to an image in this project, or a full url to any image. If left blank, no featured image will appear at top of About page.
about-featured-image: demo_031
# set background-position for featured image, "center", "top", "bottom"
position: bottom
# major heading to display over featured image
heading: About the Collection
# paragraph text below heading in featured image
sub-heading: 
# additional padding added to the feature to increase size. Give value in em or px, e.g. "5em".
padding: 6em
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---
## About Digital Grinnell
[Digital Grinnell](https://grinnell.primo.exlibrisgroup.com/discovery/collectionDiscovery?vid=01GCL_INST:GCL&collectionId=81302943070004641) contributes to “free inquiry and the open exchange of ideas” through the preservation and publication of scholarship created by Grinnell College students, faculty, and staff, as well as selected material that illuminates the College’s history and other activities.

## About Grinnell College Libraries
The 11 faculty librarians and 19 staff of the [Grinnell College Libraries](https://www.grinnell.edu/academics/libraries/about-us) — Burling Library, the Kistle Science Library, and the Curriculum Library — are dedicated to helping Grinnell students, faculty, and staff succeed in learning, teaching, and research. Our services emphasize working closely with students to develop fluency in the use and evaluation of information sources as they conduct research and other intellectual investigations, through individualized research appointments, classroom instruction, and drop-in research assistance. Each academic department and concentration has a professional librarian assigned as its liaison, and we work closely with our campus colleagues to integrate writing, reading, data analysis, academic advising, and other services. The Libraries’ book, journal, data, and media collections — in analog and digital formats — are wide-ranging and intellectually challenging, representing multiple viewpoints, languages, and cultures, and we are part of a worldwide network of libraries that can bring you information from all parts of the globe. We offer a variety of spaces for quiet and collaborative study, practicing presentations, and relaxing, and we sponsor readings, lectures, and musical performances throughout the year. We’re also part of the Grinnell town community; residents are welcome to borrow from our collection, use our facilities, and enjoy our events.

As the world of information grows more complex — available in more formats, from more sources, with confusing questions about copyright and reliability — libraries are more central to learning than ever before. We look forward to working with you!


## About CollectionBuilder CSV

This demo collection features items from the University of Idaho Library's [Digital Collections](https://www.lib.uidaho.edu/digital/), and is build using [CollectionBuilder-CSV](https://github.com/CollectionBuilder/collectionbuilder-csv).

CollectionBuilder-CSV is a "Stand Alone" template for creating digital collection and exhibit websites using Jekyll, given:

- a CSV of collection metadata
- a folder of images, PDFs, audio, or video files

Driven by your collection metadata, the template generates engaging visualizations to browse and explore your objects.
The resulting static site can be hosted on any basic web server.

[CollectionBuilder](https://github.com/CollectionBuilder/) is an set of open source tools for creating digital collection and exhibit websites that are driven by metadata and powered by modern static web technology.
See [CB Docs](https://collectionbuilder.github.io/cb-docs/) for detailed information.

{% include feature/image.html objectid="demo_001" width="75" %} 

<!-- IMPORTANT!!! DELETE this comment and the include below when you are finished editing this page for your collection. The include below introduces about page features. They will show up on your collection's about page until you delete it.  -->
{% include cb/about_the_about.md %} 
