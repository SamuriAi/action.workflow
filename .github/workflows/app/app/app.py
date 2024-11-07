from flask import Flask, render_template, request, redirect, url_for
from models.image_to_text_model import generate_text_from_image
from models.text_processing_model import process_text
from models.text_to_image_model import generate_image_from_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded image
        file_path = f"data/{file.filename}"
        file.save(file_path)
        
        # Process the image to generate text
        generated_text = generate_text_from_image(file_path)
        
        # Process the text
        processed_text = process_text(generated_text)
        
        # Generate an image from the processed text
        output_image_path = generate_image_from_text(processed_text)
        
        return render_template('result.html', original_image=file_path, text=processed_text, output_image=output_image_path)

if __name__ == '__main__':
    app.run(debug=True)
