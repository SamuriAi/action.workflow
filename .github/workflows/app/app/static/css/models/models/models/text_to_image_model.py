import openai
import os

# Load your OpenAI API key from an environment variable or a file
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image_from_text(text_description, output_image_path='output_image.png'):
    """
    Generate an image from a text description using a pre-trained model.
    
    Args:
    text_description (str): The text description to generate the image from.
    output_image_path (str): The path where the generated image will be saved.
    
    Returns:
    str: The path to the generated image.
    """
    response = openai.Image.create(
        prompt=text_description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    
    # Download the image and save it to the specified path
    image_data = requests.get(image_url).content
    with open(output_image_path, 'wb') as image_file:
        image_file.write(image_data)
    
    return output_image_path

# Example usage
if __name__ == "__main__":
    text_description = "A ninja crouched atop a roof of a tree house with his backpack and gear all sprawled out, reflecting the moonlight in an anime city backdrop."
    output_image = generate_image_from_text(text_description)
    print(f"Generated image saved at {output_image}")
