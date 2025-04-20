# UTD AI Assistant

An AI-powered chatbot for The University of Texas at Dallas using LLaMA model and LangChain.

## Features

- UTD-specific information retrieval
- Conversation memory
- Document-based responses
- Web interface

## Setup

1. Clone the repository
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

4. Add university documents to `knowledge_base/university_docs/`

5. Run the ingestion script:
```bash
python -m src.utils.ingest
```

6. Start the application:
```bash
python app.py
```

The chatbot will be available at `http://localhost:8000`

## Project Structure

```
llm_chatbot_university/
├── app.py                 # FastAPI application
├── requirements.txt       # Project dependencies
├── src/
│   ├── models/           # LLM handling
│   └── utils/            # Utility functions
├── templates/            # HTML templates
├── static/               # Static files
├── knowledge_base/       # Document storage
└── models/              # LLaMA model storage
```
