
from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np

class SICSemanticMatcher:
    def __init__(self, descriptions: list[str], model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.descriptions = descriptions
        self.embeddings = self.model.encode(descriptions, convert_to_tensor=False, show_progress_bar=True)
        self.index = self._build_faiss_index(self.embeddings)

    def _build_faiss_index(self, vectors: np.ndarray):
        dim = vectors[0].shape[0]
        index = faiss.IndexFlatL2(dim)
        index.add(np.array(vectors).astype('float32'))
        return index

    def match(self, query: str, top_k: int = 5):
        query_vec = self.model.encode([query], convert_to_tensor=False)
        D, I = self.index.search(np.array(query_vec).astype('float32'), top_k)
        return I[0], D[0]
