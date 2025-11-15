from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import papermill as pm

# Initialize the clients
qdrant_client = QdrantClient()
model = SentenceTransformer('all-MiniLM-L6-v2')

print("Libraries imported and initialized successfully!")

pm.execute_notebook(
   'Embedding.ipynb',  # Path to the notebook
}   