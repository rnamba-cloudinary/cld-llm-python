# LLM based on Cloudinary Documentation pages. 
 - Uses LlamaIndex and TrafilaturaWebReader to scrape our documentation pages and ChromaDB to create the Embeddings for the ChatGPT API LLM. Users will be able to query our documentation pages that are indexed with text. Currently for internal use only, there are some queries that will return wonky results, so please verify the validity of the response from this tool. 
 -  Currently indexing the following pages: 
"https://cloudinary.com/documentation/transformation_reference",
"https://cloudinary.com/documentation/image_upload_api_reference",
"https://cloudinary.com/documentation/admin_api",
"https://cloudinary.com/documentation/search_api",
"https://cloudinary.com/documentation/metadata_api",
"https://cloudinary.com/documentation/provisioning_api",
"https://cloudinary.com/documentation/cloudinary_cli",                                
"https://cloudinary.com/documentation/upload_widget_reference",
"https://cloudinary.com/documentation/product_gallery_reference",
"https://cloudinary.com/documentation/media_editor_reference",
"https://cloudinary.com/documentation/video_player_api_reference",
"https://cloudinary.com/documentation/shopify_integration",
"https://cloudinary.com/documentation/wordpress_integration"

Will add SDK references next and frontend endpoint.

First run may take a bit longer.
# Install dependencies and running
  - pip3 install -r requirements.txt 
  - Please input your own Open AI API Key. You can get one at platform.openai.com/account/api-key after signing up for an account.
  - Within the docsLLM.py file, the questions Array contains a few example questions. This supports multiple quote encapsulated questions per run separated by commas.
  - Run with python3 docsLLM.py
  - Note: Please watch your credit consumption as you can burn through the free tier ( or paid credits ) pretty quickly running these requests. 
  - Note: URLs.txt contains the full list of scraped URLs. Inputting these into the url_list will result it much more accurate responses, however, this will cause the application to take 15-20 minutes to run a batch of queries and possible timeouts. These can be avoided through refactoring the application in further phases
