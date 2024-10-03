"""Module to handle portfolio database"""
import pandas as pd
import chromadb


class PortFolio:
    """Class to handle portfolio
    """

    def __init__(self, filepath="./resources/my_portfolio.csv") -> None:
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
        self.chroma_client = chromadb.PersistentClient()
        self.collection = self.chroma_client.get_or_create_collection(
            name="portfolio")

    def load_portfolio(self):
        """Load portfolio into chroma db"""
        if not self.collection.count():
            for index, row in self.data.iterrows():
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(index)])

    def query_links(self, skills):
        """Method to query the chromadb dataset"""
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
