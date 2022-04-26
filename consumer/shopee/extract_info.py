import re

from consumer.shopee.info_get import InfoGet
from consumer.shopee.schemas import ItemIdRqt

BASE_URL = "https://shopee.vn/api/v4/"


class ExtractInfo:
    def __init__(self):
        self.api = InfoGet(base_url=BASE_URL)

    def get_cmt_list_by_item_id(self, item_id, shop_id, limit=10):
        """
            Get cmt from shopee by item id
        """
        item_id_rqt = ItemIdRqt(itemid=item_id, shopid=shop_id, limit=limit)
        rsp = self.api.get_cmt_item_by_id(item=item_id_rqt)
        # rsp = requests.get(BASE_URL + "item/get_ratings",
        #    params = item_id_rqt.dict())
        print(rsp)
        return {"comments": [rating.comment for rating in rsp.data.ratings]}

    def get_cmt_list_by_url(self, url: str, limit=10):
        try:
            shop_id, item_id = re.findall(r'i.(\d+).(\d+)', url)[0]
        except:
            print("Can't get shop_id and item_id from url")

        return self.get_cmt_list_by_item_id(item_id=item_id, shop_id=shop_id, limit=limit)

    def get_cmt_list_by_keyword(self, keyword: str):
        """
            Get item list from shopee by keyword
        """
        tra_ve = {"comments": []}

        rsp = self.api.get_item_list_by_keyword(keyword=keyword)
        for id in rsp.id:
            rsp_id = self.get_cmt_list_by_item_id(
                item_id=id.item_id, shop_id=id.shop_id)
            tra_ve["comments"].extend(rsp_id["comments"])

        return tra_ve
