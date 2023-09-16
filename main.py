from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from aliexpress_api import AliexpressApi, models

API_KEY  = '33792213'
API_SECRET  = '23d6195dce2267ff0fa0b7ef755ecf36'
aliexpress = AliexpressApi(API_KEY, API_SECRET, models.Language.EN, models.Currency.EUR, "default")
app = FastAPI()

def addsourceType(input_string):
    # Use the split() method to split the string at the "?" mark
    parts = input_string.split("?")
    return parts[0] + '?sourceType=620&'+ parts[1]

def make_affiliate_links(input_string):
    print('make_affiliate_links called')
    affiliate_links = aliexpress.get_affiliate_links(input_string)
    return affiliate_links[0].promotion_link


def get_product_details(input_string):
    print('get_product_details called')
    products = aliexpress.get_products_details([API_KEY, input_string])
    return products[0]



class Link(BaseModel):
    link: str
    shop: str

class Product(BaseModel):
    name: str
    img: str

@app.get("/", response_model=str)
async def start():
    return "hello there !"

# Create an endpoint to create an item
@app.post("/get-affiliat-link/", response_model=Link)
async def get_link(item: Link):
    aff_link =  make_affiliate_links(addsourceType(item.link))
    shop_link = make_affiliate_links("https://www.aliexpress.com/p/shoppingcart/index.html")
    return  Link(link=aff_link , shop=shop_link)

@app.post("/get-product-detial/", response_model=Product)
async def get_product(item: Link):
    product = get_product_details(item.link)
    return Product(name=product.product_title,img=product.product_main_image_url)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
