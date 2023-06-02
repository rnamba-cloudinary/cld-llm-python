from dotenv import load_dotenv
from llama_index import GPTChromaIndex, TrafilaturaWebReader
import chromadb

load_dotenv()

def create_embedding_store(name):
    chroma_client = chromadb.Client()
    return chroma_client.create_collection(name)

def query_pages(collection, urls, questions):
    docs = TrafilaturaWebReader().load_data(urls)
    index = GPTChromaIndex.from_documents(docs, chroma_collection=collection)
    index.save_to_disk('master_index.json')
    for question in questions:
        print(f"Question: {question} \n")
        print(f"Answer: {index.query(question)}")

if __name__ == "__main__":
    url_list = ["https://cloudinary.com/documentation/transformation_reference",
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
                "https://cloudinary.com/documentation/wordpress_integration",
                ]

    questions = [
        "What does the asset Delivery URL structure looks like?",
        "Give me an example URL of how would I take a sample image and add a black and white filter to it, then crop the image to focus on faces with the transformation URL API?",
        "Admin API Get request for all assets in a specific folder named 'cats_smiling'?",
        "How do I delete a user in my cloud?"
    ]

    collection = create_embedding_store("supertype")

    query_pages(
        collection,
        url_list,
        questions
    )
