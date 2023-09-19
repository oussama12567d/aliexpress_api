import time


from aliexpress_api import AliexpressApi, models

import telebot
from telebot import types




TOKEN  = '6158128739:AAEdbQIGdfq9BvuKJgdmUbWMH7q_GeuzrWo'
BOT_USERNAME  ='@abdelghani_djedidi_bot'
API_KEY  = '33792213'
API_SECRET  = '23d6195dce2267ff0fa0b7ef755ecf36'
aliexpress = AliexpressApi(API_KEY, API_SECRET, models.Language.EN, models.Currency.EUR, "default")


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_photo(message.chat.id, 'https://wipdidoo.ie/wp-content/uploads/2022/01/Aliexpress-Wipdidoo-gif-300x300.gif')
    bot.send_message(message.chat.id, '🔥🔥🔥\n👋مرحبًا بك في بوت   Ali \n \n مهمة هذا البوت زيادة نسبة التخفيض بالنقاط (العملات) \nمن 1%~5% إلى 11%~24% حسب المنتج 🔥 \n \n✅ تعمل الروابط فقط مع المنتوجات التي يتوفر فيها تخفيض النقاط \n🔥🔥🔥\n')
    bot.send_message(message.chat.id, 'الرجاء نسخ الرابط من التطبيق ثم إرساله إلى البوت')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        await_animate = bot.send_animation(message.chat.id, 'https://media.giphy.com/media/cvSf28B7CM3aPuCMDC/giphy.gif')
        link = get_the_final_link(message.text)
        aff =  make_affiliate_links(link)
        shoping_cart = aliexpress.get_affiliate_links("https://www.aliexpress.com/p/shoppingcart/index.html")
        product = get_product_details(link)
        time.sleep(1.1)
        bot.delete_message(message.chat.id, await_animate.message_id)
        bot.send_photo(message.chat.id, product.product_main_image_url)
        # bot.send_message(message.chat.id, "🌟اسم المنتج: \n"+ product.product_title)
        # markup = types.InlineKeyboardMarkup()
        # link = types.InlineKeyboardButton(text="🌟رابط المنتج", url=aff)
        # markup.add(link)
        # bot.send_message(message.chat.id, "🌟رابط تخفيض النقاط: \n", reply_markup=markup)
        superdelas = aliexpress.get_affiliate_links(superdels(link))[0].promotion_link
        mahdodo_link = aliexpress.get_affiliate_links(mahdod(link))[0].promotion_link
        markup = types.InlineKeyboardMarkup()
        link = types.InlineKeyboardButton(text="🌟رابط التخفيض🌟", url=aff)
        link2 = types.InlineKeyboardButton(text="🛒الشراء بتخفيض النقاط من السلة🛒", url=shoping_cart[0].promotion_link )
        link3 = types.InlineKeyboardButton(text="🌟رابط السوبر ديلز🌟", url=superdelas)
        link4 = types.InlineKeyboardButton(text="🌟رابط العرض المحدود🌟", url=mahdodo_link)
        markup.row(link)
       
        markup.row(link3)
        markup.row(link4)
        markup.row(link2)
        
        bot.send_message(message.chat.id, "🌟اسم المنتج: \n"+ product.product_title, reply_markup=markup)

    except:
        bot.delete_message(message.chat.id, await_animate.message_id)
        bot.send_animation(message.chat.id, 'https://media.giphy.com/media/fJxnT4k3H0aZ8JwOII/giphy.gif')
        bot.send_message(message.chat.id, "✅ يجب نسخ الرابط من التطبيق ثم إرساله إلى البوت")    
       

def addsourceType(input_string):
    # Use the split() method to split the string at the "?" mark
    
    
    return input_string + '?sourceType=620&'
def superdels(input_string):
    return input_string + '?sourceType=562'
def mahdod(input_string):
    return input_string + '?sourceType=561'
def make_affiliate_links(input_string):
    print('make_affiliate_links called')
    affiliate_links = aliexpress.get_affiliate_links(addsourceType(input_string))
    return affiliate_links[0].promotion_link


def get_product_details(input_string):
    print('get_product_details called')
    products = aliexpress.get_products_details([API_KEY, input_string])
    return products[0]



# Define a Flask route to receive updates
import re
def extract_links(text):
    url_regex = r'https?://[^\s]+'
    matches = re.findall(url_regex, text)
    
    if matches:
        return matches
    else:
        return []
import requests



    # Start polling
    
import requests

def resolve_short_url(short_url):
    try:
        if 'aliexpress.com/item/' in short_url:
            final_url = short_url
            return final_url
        response = requests.head(short_url, allow_redirects=True)
        final_url = response.url
        return final_url
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

import urllib.parse

def extract_redirect_url(input_link):
    # Parse the input URL
    parsed_url = urllib.parse.urlparse(input_link)
    
    # Extract the 'redirectUrl' query parameter
    query_parameters = urllib.parse.parse_qs(parsed_url.query)
    redirect_url = query_parameters.get('redirectUrl', [''])[0]
    
    # Decode the redirect URL
    decoded_url = urllib.parse.unquote(redirect_url)
    
    return decoded_url
from urllib.parse import urlparse
def get_base_url(url):
    parsed_url = urlparse(url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
    return base_url

# Example usage:
    
def get_the_final_link(url):
    short_url = extract_links(url)[0]
    if short_url:
        resolved_url = resolve_short_url(short_url)
        if( resolved_url == short_url):
            fina_url = get_base_url(resolved_url)
            return fina_url
        else:
            redirect_url = extract_redirect_url(resolved_url)
            if redirect_url:
                final_url = get_base_url(redirect_url)
                return final_url
    
    
if __name__ == '__main__':
    bot.polling()
        
       
   


