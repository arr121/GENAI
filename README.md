# GENAI - OpenAI Learning Project

A comprehensive learning project designed to explore and understand OpenAI's API capabilities through practical implementation. This Python application demonstrates the integration of multiple OpenAI models (GPT and DALL-E) in a real-world scenario by creating an intelligent cooking assistant that generates recipes with shopping lists and visual representations of ingredients.

## 🎯 Learning Objectives

This project serves as a hands-on tutorial for:
- **OpenAI API Integration**: Learn how to authenticate and interact with OpenAI's services
- **GPT Model Usage**: Understand prompt engineering and text generation capabilities
- **DALL-E Implementation**: Explore AI image generation and visual content creation
- **API Response Handling**: Master parsing and processing AI-generated content
- **Multi-Model Workflows**: Combine different AI models for complex applications
- **Environment Management**: Best practices for API key security and configuration

Cooking Receipe.py:  This application leverages OpenAI's GPT and DALL-E models to generate cooking recipes with shopping lists and visual representations of ingredients.


## 📁 Project Structure

```
GENAI/
├── README.md
├── DALL-E/
│   └── Cooking_Receipe.py    #Sample Python project created to retrieve the cooking receipe and images of imgredients to prepare the Cusine  
└── Examples/
    ├── Embedding.ipynb
    ├── Execution_File.py
    ├── parsed_logs_1.csv
    └── top_rated_wines.csv
├── Semantic_Kernel/
│   └── Semantic_Kernel.py    # Semantic Kernel is SDK Api

## 🔧 Prerequisites

- Python 3.7+
- OpenAI API key
- Required Python packages (see Installation section)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd GENAI
   ```

2. **Set up virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install openai python-dotenv regex
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 How to Execute

### Running the Cooking Recipe Generator

1. **Navigate to the project directory**:
   ```bash
   cd /workspaces/GENAI
   ```

2. **Execute the main script**:
   ```bash
   python DALL-E/Cooking_Receipe.py
   ```
