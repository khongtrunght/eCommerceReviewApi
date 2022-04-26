import requests
from consumer.shopee.schemas import ItemIdRqt, ItemIdRsp, KeywordSearchRqt, KeywordSearchRsp


class InfoGet:
    api_ver = '/api/v4/'

    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_cmt_item_by_id(self, item: ItemIdRqt):
        """
            Get cmt from shopee by item id
        """
        url = self.base_url + 'item/get_ratings'
        rsp = requests.get(url, params=item.dict())
        return ItemIdRsp.parse_obj(rsp.json())

    def get_item_list_by_keyword(self, keyword: str, limit: int = 10):
        """
            Get item list from shopee by keyword
        """
        url = self.base_url + 'search/search_items'
        rsp = requests.get(url, params=KeywordSearchRqt(
            keyword=keyword, limit=limit).dict())
        return KeywordSearchRsp.parse_obj(rsp.json())
