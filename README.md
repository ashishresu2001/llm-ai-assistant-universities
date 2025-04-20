# LLM AI Assistant for Universities

An AI-powered chatbot using LLaMA model and LangChain, adaptable for any university. Currently configured for The University of Texas at Dallas.

## Features
- University-specific information retrieval
- Conversation memory with context awareness
- Document-based knowledge base
- Modern web interface
- Customizable for any university

## Adapting for Your University

1. **Update University Name and Branding**:
   - In `src/models/llm_handler.py`, modify the prompt template:
   ```python
   prompt_template = """You are an AI assistant for [YOUR UNIVERSITY NAME].
   Use the following pieces of context to answer the question at the end.
   If you don't know the answer, just say that you don't know, don't try to make up an answer.
   """
   ```

2. **Customize the UI**:
   - In `templates/index.html`, update the branding colors:
   ```css
   :root {
       --university-primary: #YOUR_PRIMARY_COLOR;
       --university-secondary: #YOUR_SECONDARY_COLOR;
   }
   ```
   - Update the title and welcome message

3. **Knowledge Base Setup**:
   ```bash
   # Clear existing documents
   rm -rf knowledge_base/university_docs/*
   
   # Add your university's documents
   cp /path/to/your/docs/* knowledge_base/university_docs/
   
   # Recommended document types:
   # - Course catalogs
   # - Academic policies
   # - Student handbooks
   # - Campus guides
   # - Department information
   ```

4. **Reindex Knowledge Base**:
   ```bash
   python -m src.utils.ingest
   ```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/llm-ai-assistant-universities.git
cd llm-ai-assistant-universities
```

2. Install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Download the LLaMA model:
```bash
mkdir -p models
curl -L https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q3_K_L.bin -o models/llama-2-7b-chat.ggmlv3.q3_K_L.bin
```

4. Start the application:
```bash
python app.py
```

Visit `http://localhost:8000` to interact with the chatbot.

## Project Structure
```
llm-ai-assistant-universities/
├── app.py                    # FastAPI application
├── requirements.txt          # Project dependencies
├── src/
│   ├── models/
│   │   └── llm_handler.py   # LLM configuration and 
│   └── utils/
│       └── ingest.py        # Document ingestion
├── static/
│   └── index.html           # Web interface
├── knowledge_base/          # Document storage
│   └── university_docs/     # University-specific 
└── models/                  # LLaMA model storage
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
