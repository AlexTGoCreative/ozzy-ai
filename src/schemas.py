"""
Pydantic schemas for API request/response validation.
"""

from pydantic import BaseModel
from typing import List, Optional, Dict


class ChatMessage(BaseModel):
    role: str
    text: str


class ChatPayload(BaseModel):
    chat_history: List[ChatMessage]
    scan_results: Optional[Dict] = None
    file_info: Optional[Dict] = None
    process_info: Optional[Dict] = None
    sanitized_info: Optional[Dict] = None
    sandbox_data: Optional[Dict] = None
    url_data: Optional[Dict] = None
