import re

def clean_text(text):
    """
    Clean the generated text by removing unwanted characters and formatting.
    
    Args:
    text (str): The raw generated text.
    
    Returns:
    str: The cleaned and formatted text.
    """
    # Remove unwanted characters
    text = re.sub(r'\n', ' ', text)  # Remove newlines
    text = re.sub(r'[^A-Za-z0-9 .,?!]', '', text)  # Remove non-alphanumeric characters except punctuation

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Capitalize the first letter of each sentence
    sentences = re.split(r'(?<=[.!?]) +', text)
    text = ' '.join([sentence.capitalize() for sentence in sentences])

    return text

def format_text_for_comic(text):
    """
    Format the cleaned text to fit into comic book speech bubbles or text boxes.
    
    Args:
    text (str): The cleaned text.
    
    Returns:
    str: The formatted text.
    """
    # Example of splitting text into lines suitable for comic book text bubbles
    max_line_length = 40
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += " " + word
        else:
            lines.append(current_line.strip())
            current_line = word

    if current_line:
        lines.append(current_line.strip())

    formatted_text = '\n'.join(lines)
    return formatted_text

# Example usage
if __name__ == "__main__":
    raw_text = "This is an example of the raw generated text. It might contain unwanted characters or formatting issues."
    cleaned_text = clean_text(raw_text)
    formatted_text = format_text_for_comic(cleaned_text)
    print("Cleaned Text:", cleaned_text)
    print("Formatted Text:\n", formatted_text)
