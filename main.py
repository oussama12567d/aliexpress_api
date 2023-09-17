import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from aliexpress_api import AliexpressApi, models




API_KEY  = '33792213'
API_SECRET  = '23d6195dce2267ff0fa0b7ef755ecf36'
aliexpress = AliexpressApi(API_KEY, API_SECRET, models.Language.EN, models.Currency.EUR, "default")
app = FastAPI()






 

   
    



def addsourceType(input_string):
    # Use the split() method to split the string at the "?" mark
    return input_string + '?sourceType=620&'

def make_affiliate_links(input_string):
    print('make_affiliate_links called')
    affiliate_links = aliexpress.get_affiliate_links((input_string))
    
    return affiliate_links[0].promotion_link


def get_product_details(input_string):
    print('get_product_details called')
    products = aliexpress.get_products_details(input_string)
    return products[0]

class Requiest (BaseModel):
    link: str


class Response(BaseModel):
    aff: str
    shop: str
    name: str
    img: str


    

@app.get("/", response_model=str)
async def start():
    return "hello there !"

# Create an endpoint to create an item
@app.post("/get-affiliat-link/", response_model=Response)
async def get_link(item: Requiest):
    aff_link = addsourceType(make_affiliate_links((item.link)))
    shop_link = make_affiliate_links("https://www.aliexpress.com/p/shoppingcart/index.html")
    product = get_product_details((item.link))
    return  Response(aff=aff_link , shop=shop_link , name=product.product_title,img=product.product_main_image_url)



if __name__ == "__main__":    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
