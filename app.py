import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os

# Set page config
st.set_page_config(
    page_title="AI Recipe Generator",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF5252;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .recipe-output {
        background-color: #ffffff;
        color: #1a1a1a;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #FF6B6B;
        margin-top: 1rem;
    }
    .info-box {
        background-color: #e3f2fd;
        color: #0d47a1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2196F3;
        margin-bottom: 1rem;
    }
    /* Improve text visibility */
    .stTextArea textarea {
        color: #ffffff !important;
        background-color: #2b2b2b !important;
    }
    .stTextInput input {
        color: #ffffff !important;
        background-color: #2b2b2b !important;
    }
    /* Make labels more visible */
    label {
        color: #ffffff !important;
    }
    /* Improve markdown text visibility */
    .stMarkdown {
        color: #ffffff !important;
    }
    /* Style for recipe text specifically */
    .recipe-output p, .recipe-output strong, .recipe-output em {
        color: #1a1a1a !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Cache the model loading
@st.cache_resource
def load_model(model_path):
    """Load the fine-tuned GPT-2 model and tokenizer"""
    try:
        with st.spinner("Loading AI Recipe Model... This may take a moment."):
            tokenizer = GPT2Tokenizer.from_pretrained(model_path)
            model = GPT2LMHeadModel.from_pretrained(model_path)
            
            # Set pad token if not set
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token
            
            # Move model to GPU if available
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model = model.to(device)
            model.eval()
            
            return model, tokenizer, device
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None, None

def generate_recipe(model, tokenizer, device, prompt, max_length=512, temperature=0.8, 
                   top_k=50, top_p=0.95, num_return_sequences=1, repetition_penalty=1.2):
    """Generate recipe using the fine-tuned model"""
    try:
        # Encode the prompt
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
        
        # Generate
        with torch.no_grad():
            output = model.generate(
                input_ids,
                max_length=max_length,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
                num_return_sequences=num_return_sequences,
                do_sample=True,
                repetition_penalty=repetition_penalty,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=3
            )
        
        # Decode the generated text
        generated_recipes = []
        for i in range(num_return_sequences):
            generated_text = tokenizer.decode(output[i], skip_special_tokens=True)
            generated_recipes.append(generated_text)
        
        return generated_recipes
    except Exception as e:
        st.error(f"Error generating recipe: {str(e)}")
        return None

def format_recipe_display(recipe_text):
    """Format the recipe text for better display"""
    # Replace common patterns with markdown formatting
    formatted_text = recipe_text
    
    # Make sections bold
    formatted_text = formatted_text.replace("Ingredients:", "**Ingredients:**")
    formatted_text = formatted_text.replace("Instructions:", "**Instructions:**")
    formatted_text = formatted_text.replace("Directions:", "**Directions:**")
    formatted_text = formatted_text.replace("Steps:", "**Steps:**")
    
    return formatted_text

def main():
    # Header
    st.title("🍳 AI Recipe Generator")
    st.markdown("### Generate Creative Recipes with AI")
    st.markdown("---")
    
    # Model path
    model_path = os.path.join("results", "best_recipe_model")
    
    # Check if model exists
    if not os.path.exists(model_path):
        st.error(f"Model not found at path: {model_path}")
        st.info("Please ensure the model is located in the 'results/best_recipe_model' directory.")
        return
    
    # Load model
    model, tokenizer, device = load_model(model_path)
    
    if model is None or tokenizer is None:
        st.error("Failed to load the model. Please check the model path and try again.")
        return
    
    # Display model info
    device_name = "GPU (CUDA)" if device.type == "cuda" else "CPU"
    st.sidebar.success(f"✅ Model loaded successfully on {device_name}")
    
    # Sidebar - Settings
    st.sidebar.header("⚙️ Generation Settings")
    
    # Input mode selection
    input_mode = st.sidebar.radio(
        "Input Mode:",
        ["Ingredients", "Recipe Title", "Custom Prompt"],
        help="Choose how you want to provide input to the model"
    )
    
    st.sidebar.markdown("---")
    
    # Advanced settings
    with st.sidebar.expander("🔧 Advanced Settings", expanded=False):
        max_length = st.slider(
            "Maximum Length",
            min_value=128,
            max_value=1024,
            value=512,
            step=64,
            help="Maximum length of generated recipe"
        )
        
        temperature = st.slider(
            "Temperature",
            min_value=0.1,
            max_value=2.0,
            value=0.8,
            step=0.1,
            help="Higher values make output more random, lower values more deterministic"
        )
        
        top_k = st.slider(
            "Top-K",
            min_value=10,
            max_value=100,
            value=50,
            step=10,
            help="Number of highest probability tokens to keep"
        )
        
        top_p = st.slider(
            "Top-P (Nucleus Sampling)",
            min_value=0.1,
            max_value=1.0,
            value=0.95,
            step=0.05,
            help="Cumulative probability for nucleus sampling"
        )
        
        repetition_penalty = st.slider(
            "Repetition Penalty",
            min_value=1.0,
            max_value=2.0,
            value=1.2,
            step=0.1,
            help="Penalty for repeating tokens"
        )
        
        num_recipes = st.slider(
            "Number of Recipes to Generate",
            min_value=1,
            max_value=3,
            value=1,
            help="Generate multiple recipe variations"
        )
    
    # About section
    with st.sidebar.expander("ℹ️ About", expanded=False):
        st.markdown("""
        This app uses a fine-tuned GPT-2 model to generate creative cooking recipes.
        
        **How to use:**
        1. Select input mode
        2. Enter ingredients, title, or custom prompt
        3. Adjust generation settings (optional)
        4. Click "Generate Recipe"
        
        **Tips:**
        - Use clear, simple ingredient names
        - Separate multiple ingredients with commas
        - Experiment with different temperature values
        - Higher temperature = more creative (but potentially less coherent)
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("### 📝 Input")
        
        # Input based on mode
        if input_mode == "Ingredients":
            st.markdown('<div class="info-box">💡 Enter ingredients separated by commas (e.g., chicken, garlic, olive oil, tomatoes)</div>', unsafe_allow_html=True)
            ingredients_input = st.text_area(
                "Ingredients:",
                height=150,
                placeholder="chicken breast, garlic, olive oil, tomatoes, basil",
                help="Enter the ingredients you want to use, separated by commas"
            )
            
            if ingredients_input:
                prompt = f"Recipe with ingredients: {ingredients_input}\n\nTitle:"
            else:
                prompt = ""
                
        elif input_mode == "Recipe Title":
            st.markdown('<div class="info-box">💡 Enter a recipe title or dish name (e.g., "Chocolate Chip Cookies")</div>', unsafe_allow_html=True)
            title_input = st.text_input(
                "Recipe Title:",
                placeholder="Chocolate Chip Cookies",
                help="Enter the name of the dish you want to create"
            )
            
            if title_input:
                prompt = f"Title: {title_input}\n\nIngredients:"
            else:
                prompt = ""
                
        else:  # Custom Prompt
            st.markdown('<div class="info-box">💡 Write a custom prompt for the model</div>', unsafe_allow_html=True)
            prompt = st.text_area(
                "Custom Prompt:",
                height=150,
                placeholder="Recipe for a healthy breakfast with oats and berries...",
                help="Enter any custom text to guide the recipe generation"
            )
        
        # Generate button
        generate_button = st.button("🎯 Generate Recipe", use_container_width=True)
    
    with col2:
        st.markdown("### 🍽️ Generated Recipe")
        
        if generate_button:
            if not prompt or prompt.strip() == "":
                st.warning("⚠️ Please provide input before generating a recipe.")
            else:
                # Display the prompt being used
                with st.expander("📄 View Prompt", expanded=False):
                    st.code(prompt, language="text")
                
                # Generate recipes
                with st.spinner("🔮 Generating your recipe... Please wait..."):
                    recipes = generate_recipe(
                        model, 
                        tokenizer, 
                        device, 
                        prompt,
                        max_length=max_length,
                        temperature=temperature,
                        top_k=top_k,
                        top_p=top_p,
                        num_return_sequences=num_recipes,
                        repetition_penalty=repetition_penalty
                    )
                
                if recipes:
                    # Display generated recipes
                    for idx, recipe in enumerate(recipes):
                        if num_recipes > 1:
                            st.markdown(f"#### 📖 Recipe Variation {idx + 1}")
                        
                        # Format and display
                        formatted_recipe = format_recipe_display(recipe)
                        st.markdown(f'<div class="recipe-output">{formatted_recipe}</div>', unsafe_allow_html=True)
                        
                        # Download button for each recipe
                        st.download_button(
                            label=f"📥 Download Recipe {idx + 1}",
                            data=recipe,
                            file_name=f"recipe_{idx + 1}.txt",
                            mime="text/plain",
                            key=f"download_{idx}"
                        )
                        
                        if idx < len(recipes) - 1:
                            st.markdown("---")
                    
                    st.success("✅ Recipe(s) generated successfully!")
                else:
                    st.error("Failed to generate recipe. Please try again with different settings.")
        else:
            st.info("👈 Configure your input and click 'Generate Recipe' to get started!")
            
            # Show example recipes
            with st.expander("💡 View Examples", expanded=False):
                st.markdown("""
                **Example Ingredients:**
                - chicken, garlic, lemon, herbs
                - chocolate, flour, eggs, sugar, butter
                - pasta, tomatoes, basil, parmesan
                
                **Example Titles:**
                - Classic Margherita Pizza
                - Chocolate Lava Cake
                - Chicken Tikka Masala
                - Vegan Buddha Bowl
                """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>Built with ❤️ using Streamlit and GPT-2 | "
        "Fine-tuned on Recipe Dataset</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
