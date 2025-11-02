# 🍳 AI Recipe Generator - Streamlit App

An interactive web application for generating creative cooking recipes using a fine-tuned GPT-2 model.

## Features

- **Multiple Input Modes:**

  - Generate recipes from a list of ingredients
  - Generate recipes from a dish title
  - Use custom prompts for more control

- **Advanced Generation Settings:**

  - Adjustable temperature for creativity control
  - Top-K and Top-P sampling options
  - Repetition penalty to avoid redundant text
  - Configurable maximum recipe length
  - Generate multiple recipe variations at once

- **User-Friendly Interface:**
  - Clean and intuitive design
  - Real-time recipe generation
  - Download generated recipes as text files
  - Example prompts and usage tips

## Prerequisites

- Python 3.8 or higher
- Fine-tuned GPT-2 model in `results/best_recipe_model/` directory

## Installation

1. **Clone or navigate to the project directory:**

   ```bash
   cd "d:\Semester 7\Gen AI\proj_3\recipe generator"
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. **Make sure your model is in the correct location:**

   - The app expects the model at: `results/best_recipe_model/`
   - Ensure all model files are present (config.json, model.safetensors, tokenizer files, etc.)

2. **Launch the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

3. **Open your browser:**
   - The app will automatically open in your default browser
   - Default URL: http://localhost:8501

## How to Use

### Method 1: Ingredients-Based Generation

1. Select "Ingredients" mode in the sidebar
2. Enter ingredients separated by commas (e.g., "chicken, garlic, olive oil, tomatoes")
3. Click "Generate Recipe"

### Method 2: Title-Based Generation

1. Select "Recipe Title" mode
2. Enter a dish name (e.g., "Chocolate Chip Cookies")
3. Click "Generate Recipe"

### Method 3: Custom Prompt

1. Select "Custom Prompt" mode
2. Write your own prompt to guide the generation
3. Click "Generate Recipe"

## Advanced Settings

Adjust these parameters in the sidebar to fine-tune the generation:

- **Maximum Length:** Controls the length of the generated recipe (128-1024 tokens)
- **Temperature:** Higher values (1.0-2.0) = more creative but less coherent; Lower values (0.1-0.5) = more conservative
- **Top-K:** Number of highest probability tokens to consider (10-100)
- **Top-P:** Nucleus sampling parameter (0.1-1.0)
- **Repetition Penalty:** Prevents repetitive text (1.0-2.0)
- **Number of Recipes:** Generate 1-3 recipe variations

## Tips for Best Results

1. **For Ingredients Mode:**

   - Use 3-8 common ingredients
   - Be specific (e.g., "chicken breast" instead of just "chicken")
   - Separate with commas

2. **For Title Mode:**

   - Use descriptive dish names
   - Include cuisine type if desired (e.g., "Italian Pasta Carbonara")

3. **Temperature Guidelines:**

   - 0.3-0.5: More predictable, traditional recipes
   - 0.7-0.9: Balanced creativity and coherence (recommended)
   - 1.0-1.5: More experimental and creative combinations

4. **If Generation Quality is Poor:**
   - Lower the temperature
   - Increase repetition penalty
   - Reduce maximum length
   - Try different prompts

## Troubleshooting

### Model Not Found Error

- Ensure the model is located at `results/best_recipe_model/`
- Check that all required model files are present

### Out of Memory Error

- Reduce the maximum length
- Generate fewer recipes at once
- If using GPU, try reducing batch size

### Poor Quality Recipes

- Adjust temperature (try values between 0.7-1.0)
- Increase repetition penalty
- Use more specific prompts

## File Structure

```
recipe generator/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                      # This file
└── results/
    └── best_recipe_model/         # Fine-tuned GPT-2 model
        ├── config.json
        ├── generation_config.json
        ├── merges.txt
        ├── model.safetensors
        ├── special_tokens_map.json
        ├── tokenizer_config.json
        └── vocab.json
```

## Technical Details

- **Model:** Fine-tuned GPT-2 (124M parameters)
- **Framework:** Hugging Face Transformers
- **UI Framework:** Streamlit
- **Backend:** PyTorch
- **Tokenizer:** GPT2Tokenizer

## Example Prompts

**Ingredients:**

```
chicken breast, garlic, lemon, olive oil, rosemary
```

**Titles:**

```
Classic Margherita Pizza
Chocolate Lava Cake
Vegan Buddha Bowl
Thai Green Curry
```

**Custom Prompts:**

```
Recipe for a healthy breakfast with oats and berries
Quick 15-minute dinner with pasta
Dessert using chocolate and strawberries
```

## License

This project is part of a Gen AI course assignment.

## Acknowledgments

- Dataset: 3A2M_EXTENDED from Kaggle
- Model: GPT-2 by OpenAI
- Framework: Hugging Face Transformers
