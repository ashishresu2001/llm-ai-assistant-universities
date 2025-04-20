from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import LlamaCppEmbeddings
from langchain.vectorstores import Chroma
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ingest_documents():
    """
    Ingest documents from the knowledge base directory and create embeddings.
    """
    try:
        logger.info("Starting document ingestion process...")
        
        # Load documents from directory
        loader = DirectoryLoader(
            'knowledge_base/university_docs',
            glob="**/*.*",
            show_progress=True
        )
        documents = loader.load()
        logger.info(f"Loaded {len(documents)} documents from knowledge base")
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        texts = text_splitter.split_documents(documents)
        logger.info(f"Split documents into {len(texts)} chunks")
        
        # Initialize embeddings
        embeddings = LlamaCppEmbeddings(
            model_path="models/llama-2-7b-chat.ggmlv3.q3_K_L.bin"
        )
        logger.info("Initialized LlamaCppEmbeddings")
        
        # Create and persist vector store
        db = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory="knowledge_base/chroma_db"
        )
        db.persist()
        logger.info(f"Successfully created and persisted vector store with {len(texts)} chunks")
        
        return True
        
    except Exception as e:
        logger.error(f"Error during document ingestion: {str(e)}", exc_info=True)
        return False

if __name__ == "__main__":
    success = ingest_documents()
    if success:
        logger.info("Document ingestion completed successfully")
    else:
        logger.error("Document ingestion failed")