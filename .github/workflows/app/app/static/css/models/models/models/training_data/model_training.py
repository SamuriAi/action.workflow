import os
import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset, Dataset

def train_image_to_text_model(dataset_dir):
    """
    Train an image-to-text model using preprocessed datasets.
    
    Args:
    dataset_dir (str): Directory containing the dataset.
    """
    model_name = "nlpconnect/vit-gpt2-image-captioning"
    model = VisionEncoderDecoderModel.from_pretrained(model_name)
    feature_extractor = ViTImageProcessor.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Load and preprocess datasets
    dataset = load_dataset('csv', data_files={'train': os.path.join(dataset_dir, 'training_data.csv')})
    
    def preprocess_function(examples):
        images = [Image.open(image_path) for image_path in examples['image_path']]
        pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
        input_ids = tokenizer(examples['text'], truncation=True, padding="max_length", return_tensors="pt").input_ids
        return {"pixel_values": pixel_values, "input_ids": input_ids}
    
    dataset = dataset.map(preprocess_function, batched=True)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=4,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset['train']
    )

    # Train model
    trainer.train()

    # Save model
    model.save_pretrained("./model")
    tokenizer.save_pretrained("./model")
    print("Model training complete.")

if __name__ == "__main__":
    dataset_dir = "data/"
    train_image_to_text_model(dataset_dir)
