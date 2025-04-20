from langchain.llms import LlamaCpp
from langchain.embeddings import LlamaCppEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class LLMHandler:
    def __init__(self):
        # Initialize the LLM
        self.llm = LlamaCpp(
            model_path="models/llama-2-7b-chat.ggmlv3.q3_K_L.bin",
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
        )
        
        # Initialize embeddings
        self.embeddings = LlamaCppEmbeddings(
            model_path="models/llama-2-7b-chat.ggmlv3.q3_K_L.bin"
        )
        
        # Load the vector store
        self.db = Chroma(
            persist_directory="knowledge_base/chroma_db",
            embedding_function=self.embeddings
        )
        
        # Create custom prompt template
        prompt_template = """You are an AI assistant for The University of Texas at Dallas (UTD).
        Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}

        Question: {question}

        Answer: Let me help you with information about UTD - """
        
        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create the chain with custom prompt
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.db.as_retriever(search_kwargs={"k": 3}),
            chain_type_kwargs={"prompt": PROMPT}
        )

    def get_response(self, query: str) -> str:
        try:
            response = self.qa_chain.run(query)
            return response
        except Exception as e:
            print(f"Error in LLMHandler: {str(e)}")
            return "I apologize, but I encountered an error while processing your query. Please try again."