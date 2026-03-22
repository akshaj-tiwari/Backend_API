from app.clients.openlibrary_client import OpenLibraryClient
from app.models.book import Book

class BookService:
    def __init__(self):
        self.client = OpenLibraryClient()

    def search_books(self, query, page=1):
        data = self.client.search(query, page)
        docs = data.get("docs", [])
        results = []
        for raw in docs:
            book = self.buildBook(raw)
            results.append(book)
        return results
    def buildBook(self, raw):
        work_key = raw.get("key", "")
        work_id = work_key.split("/")[-1]

        cover_id = raw.get("cover_i")
        cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else None

        return Book(
            work_id=work_id,
            title=raw.get("title", "Unknown"),
            authors=raw.get("author_name", []),
            first_publish_year=raw.get("first_publish_year"),
            subjects=[],
            cover_url=cover_url,
            edition_count=raw.get("edition_count", 0),
            languages=[],
            data_quality="partial"
        )