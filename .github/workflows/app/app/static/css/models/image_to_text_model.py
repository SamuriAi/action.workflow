from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import requests

# Load the model, tokenizer, and processor
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_text_from_image(image_path):
    """
    Generate a text description from an image using a pre-trained model.
    
    Args:
    image_path (str): The path to the image file.
    
    Returns:
    str: The generated text description.
    """
    # Open the image file
    image = Image.open(image_path)
    
    # Preprocess the image
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    
    # Generate text from image
    output_ids = model.generate(pixel_values)
    description = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return description

# Example usage
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    description = generate_text_from_image(image_path)
    print(description)
