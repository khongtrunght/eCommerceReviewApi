from fastapi import FastAPI

from consumer.shopee.extract_info import ExtractInfo
app = FastAPI()

test_api = ExtractInfo()


@app.get("/")
def comment_list():
    return test_api.get_cmt_list_by_item_id(item_id=4563287513, shop_id=43135227, limit=30)


@app.get("/url")
def from_url(url: str, limit: int = 10):
    return test_api.get_cmt_list_by_url(url=url, limit=limit)


@app.get("/keyword")
def from_keyword(keyword: str):
    return test_api.get_cmt_list_by_keyword(keyword=keyword)
