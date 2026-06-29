# Change Display of PDF Items from Images to an Embedded PDF Viewer 
The item pages for pdfs display the items's first page the same way as it displays images. Enhance the user's experience by changing the pdf items to displaying in an embedded PDF viewer. 

1. Go to `__layouts/item/pdf.html` in your repository


            ---
            # basic layout for PDF documents
            # Displays image_small if available, with fall back to image_thumb, or a pdf icon.
            layout: item/item-page-base
            ---

            <div class="card mb-4 text-center">
                <div class="card-body">
                    <p>
                        {% include item/item-thumb.html %}
                    </p>

                    <div class="mt-2">

                        {% include item/download-buttons.html %}

                    </div>

                </div>
            </div>
2. Replace `{% include item/item-thumb.html %}` with `{% include item/pdf-embed.html %}`

            ---
            # basic layout for PDF documents
            # Displays image_small if available, with fall back to image_thumb, or a pdf icon.
            layout: item/item-page-base
            ---

            <div class="card mb-4 text-center">
                <div class="card-body">
                    <p>
                        {% include item/pdf-embed.html %}
                    </p>

                    <div class="mt-2">

                        {% include item/download-buttons.html %}

                    </div>

                </div>
            </div>

3. Save the file in your repository. You should now see all PDF items in the PDF viewer on their item page! 
