import requests

BASE_URL = "https://openlibrary.org"
class OpenLibraryClient:
    def search(self, query, page=1):
        url = f"{BASE_URL}/search.json"
        params = {"q": query, "page": page}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"API failed")
        return response.json()
    