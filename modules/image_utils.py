import requests 
from PIL import Image 
import io 
from modules.ipfs import resolve_ipfs_url

def fetch_image(image_url):
    # Fetch an image from url 
    resolved_url = resolve_ipfs_url(image_url)
    response = requests.get(resolved_url)
    response.raise_for_status()
    return response.content

def display_image(image_data):
    # Display an image from binary data 
    image = Image.open(io.BytesIO(image_data))
    image.show() 