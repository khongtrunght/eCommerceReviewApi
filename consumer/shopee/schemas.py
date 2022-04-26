from typing import Dict, List, Any
import pydantic
from pydantic import BaseModel, root_validator


class ItemIdRqt(BaseModel):
    filter = 0
    flag = 1
    offset = 0
    type = 0
    itemid: int
    shopid: int
    limit: int


class Rating(BaseModel):
    comment: str


class Data(BaseModel):
    ratings: List[Rating]
    item_rating_summary: dict


class ItemIdRsp(BaseModel):
    data: Data


class KeywordSearchRqt(BaseModel):
    by: str = 'relevancy'
    keyword: str
    limit: int = 5
    newest = 0
    order: str = 'desc'
    page_type: str = 'search'
    scenario: str = 'PAGE_GLOBAL_SEARCH'
    version: int = 2


class Id(BaseModel):
    shop_id: int
    item_id: int


class KeywordSearchRsp(BaseModel):
    items: List[Dict]
    id: List[Id] = list()

    @root_validator
    def compute_id(cls, obj: Any):
        obj['id'] = [Id(shop_id=item['item_basic']['shopid'],
                     item_id=item['item_basic']['itemid']) for item in obj['items']]
        return obj
