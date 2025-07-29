from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ProductInput(BaseModel):
    name: str
    category: str
    features: List[str]
    keywords: List[str]
    location: str
    target_audience: str

class SEOContent(BaseModel):
    slug: str
    seo_title: str
    meta_description: str
    intro_content: str
    sections: List[Dict[str, str]]
    faqs: List[Dict[str, str]]
    call_to_action: str
    json_ld_schema: Dict[str, Any]

class ProductResponse(BaseModel):
    id: int
    slug: str
    name: str
    category: str
    features: List[str]
    keywords: List[str]
    location: str
    target_audience: str
    seo_title: str
    meta_description: str
    intro_content: str
    sections: List[Dict[str, str]]
    faqs: List[Dict[str, str]]
    call_to_action: str
    json_ld_schema: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class GenerateResponse(BaseModel):
    success: bool
    message: str
    product: Optional[ProductResponse] = None 