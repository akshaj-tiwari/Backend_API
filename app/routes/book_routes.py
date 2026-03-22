from fastapi import APIRouter, Query
from app.services.book_service import BookService

router = APIRouter()
service = BookService()

@router.get("/search")
def search(q: str, page: int =1):
    try:
        return service.search_books(q, page)
    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }
        