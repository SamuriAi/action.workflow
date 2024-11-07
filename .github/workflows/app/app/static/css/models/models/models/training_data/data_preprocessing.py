import os
import pandas as pd
from PIL import Image

def load_and_preprocess_images(image_dir, output_dir):
    """
    Load images from a directory, preprocess them, and save to an output directory.
    
    Args:
    image_dir (str): Directory containing raw images.
    output_dir (str): Directory to save preprocessed images.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_dir, filename)
            image = Image.open(image_path)
            # Example preprocessing: resizing images
            image = image.resize((256, 256))
            output_path = os.path.join(output_dir, filename)
            image.save(output_path)
            print(f"Processed {filename}")

def load_and_preprocess_texts(text_dir):
    """
    Load text files from a directory and preprocess them.
    
    Args:
    text_dir (str): Directory containing text files.
    
    Returns:
    pd.DataFrame: DataFrame containing preprocessed texts.
    """
    texts = []
    for filename in os.listdir(text_dir):
        if filename.endswith(".txt"):
            text_path = os.path.join(text_dir, filename)
            with open(text_path, 'r') as file:
                text = file.read().strip()
                # Example preprocessing: lowercasing text
                text = text.lower()
                texts.append({'filename': filename, 'text': text})
    
    df = pd.DataFrame(texts)
    return df

if __name__ == "__main__":
    image_dir = "data/training_data/images/"
    output_image_dir = "data/processed_images/"
    text_dir = "data/training_data/texts/"
    
    load_and_preprocess_images(image_dir, output_image_dir)
    preprocessed_texts = load_and_preprocess_texts(text_dir)
    preprocessed_texts.to_csv("data/processed_texts.csv", index=False)
    print("Preprocessing complete.")
