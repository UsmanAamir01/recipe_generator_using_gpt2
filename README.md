# 🍳 AI Recipe Generator - Streamlit App

An interactive web application for generating creative cooking recipes using a fine-tuned GPT-2 model.

[![GitHub](https://img.shields.io/badge/GitHub-UsmanAamir01-blue?logo=github)](https://github.com/UsmanAamir01/recipe_generator_using_gpt2)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Live Demo

🔗 **GitHub Repository:** [https://github.com/UsmanAamir01/recipe_generator_using_gpt2](https://github.com/UsmanAamir01/recipe_generator_using_gpt2)

## 📖 About

This project is part of a **Generative AI Course Assignment** focused on fine-tuning decoder models for creative text generation. The application uses a GPT-2 model fine-tuned on the 3A2M_EXTENDED recipe dataset to generate coherent and creative cooking recipes from ingredients, titles, or custom prompts.

## 📋 Features

- **Multiple Input Modes:**

  - 🥗 Generate recipes from a list of ingredients
  - 📝 Generate recipes from a dish title
  - ✍️ Use custom prompts for more control

- **Advanced Generation Settings:**

  - 🌡️ Adjustable temperature for creativity control
  - 🎯 Top-K and Top-P sampling options
  - 🔄 Repetition penalty to avoid redundant text
  - 📏 Configurable maximum recipe length
  - 🎲 Generate multiple recipe variations at once

- **User-Friendly Interface:**
  - 🎨 Clean and intuitive design
  - ⚡ Real-time recipe generation
  - 💾 Download generated recipes as text files
  - 💡 Example prompts and usage tips

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Git LFS (for downloading model files)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/UsmanAamir01/recipe_generator_using_gpt2.git
   cd recipe_generator_using_gpt2
   ```

2. **Install Git LFS and pull model files:**

   ```bash
   git lfs install
   git lfs pull
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Launch the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Open your browser:**
   - The app will automatically open in your default browser
   - Default URL: http://localhost:8501

**Alternative (Windows):** Double-click `run_app.bat` for automatic setup and launch.

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

## 📁 File Structure

```
recipe_generator_using_gpt2/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── run_app.bat                     # Windows quick-start script
├── .gitignore                      # Git ignore rules
├── .gitattributes                  # Git LFS configuration
└── results/
    └── best_recipe_model/          # Fine-tuned GPT-2 model
        ├── config.json
        ├── generation_config.json
        ├── merges.txt
        ├── model.safetensors       # (Tracked with Git LFS)
        ├── special_tokens_map.json
        ├── tokenizer_config.json
        └── vocab.json              # (Tracked with Git LFS)
```

## 🔧 Technical Details

- **Model:** Fine-tuned GPT-2 (124M parameters)
- **Dataset:** [3A2M_EXTENDED](https://www.kaggle.com/datasets/nazmussakibrupol/3a2mext/data) from Kaggle
- **Framework:** Hugging Face Transformers 4.35+
- **UI Framework:** Streamlit
- **Backend:** PyTorch
- **Tokenizer:** GPT2Tokenizer
- **Storage:** Git LFS for large model files

## 🎓 Project Context

This project fulfills the **Task 1: Decoder Model (GPT-2) — Recipe Generation** requirement for a Generative AI course assignment.

### Deliverables Completed:

✅ Tokenization and dataset formatting script  
✅ Training loop for GPT-2  
✅ Example generations and quality evaluation (ROUGE, BLEU)  
✅ **Streamlit app for interactive recipe generation**

### Dataset Information:

- **Source:** [Kaggle - 3A2M_EXTENDED](https://www.kaggle.com/datasets/nazmussakibrupol/3a2mext/data)
- **Size:** 50+ MB of recipe data
- **Content:** Recipe titles, ingredients, and cooking instructions

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

## 📄 License

This project is part of a Gen AI course assignment.

## 🙏 Acknowledgments

- **Dataset:** [3A2M_EXTENDED](https://www.kaggle.com/datasets/nazmussakibrupol/3a2mext/data) from Kaggle
- **Model:** GPT-2 by OpenAI
- **Framework:** Hugging Face Transformers
- **UI:** Streamlit

## 👤 Author

**Usman Aamir**

- GitHub: [@UsmanAamir01](https://github.com/UsmanAamir01)
- Repository: [recipe_generator_using_gpt2](https://github.com/UsmanAamir01/recipe_generator_using_gpt2)

## 🤝 Contributing

This is an academic project, but suggestions and feedback are welcome! Feel free to open an issue or submit a pull request.

---

<div align="center">
  <p>Made with ❤️ using Streamlit and GPT-2</p>
  <p>⭐ Star this repo if you find it helpful!</p>
</div>
