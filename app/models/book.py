print("Book loaded")
from typing import List, Optional
from pydantic import BaseModel

class Book(BaseModel):
    work_id: str
    title: str
    authors: List[str] = []
    first_publish_year: Optional[int] = None
    subjects: List[str] = []
    cover_url: Optional[str] = None
    edition_count: int = 0  
    languages: List[str] = []   
    data_quality: str