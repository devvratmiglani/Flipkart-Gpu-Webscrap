#@github: https://github.com/devvratmiglani/Flipkart-Gpu-Webscrap.git
#@Author: https://github.com/devvratmiglani

#FOR GPU
from colorama import Fore
import requests
from bs4 import BeautifulSoup


def linkx(uri, label=None):
    if label is None:
        label = uri
    parameters = '' # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'
    return escape_mask.format(parameters, uri, label)


urlTrue = 'https://www.flipkart.com/search?q=graphics+card&sid=6bo%2Cg0i%2C6sn&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&as-pos=2&as-type=RECENT&suggestionId=graphics+card%7CGraphic+Cards&requestId=51790db7-fe1c-4e52-9766-b85637c36665&as-searchtext=gra&page='

for i in range(1,8):
    url = urlTrue+str(i)
    print('******************')
    print('******************')
    print('**** PAGE  ',i,'****')
    print('******************')
    print('******************')

    r = requests.get(url)
    myhtmlcontent = r.content
    soup = BeautifulSoup(myhtmlcontent,'html5lib')

    TopDiv = soup.find_all('div',attrs={ 'class':'_4ddWXP'})
    for link in TopDiv:
        anchor1 = link.find('a',attrs={'class':'_2rpwqI'})
        anchor2 = link.find('a',attrs={'class':'s1Q9rs'})
        anchor3 = link.find('a',attrs={'class':'_8VNy32'})
        
        if isinstance(anchor1,type(None))==False and isinstance(anchor2,type(None))==False and isinstance(anchor3,type(None))==False:
            # anchor1
            try:
                imglink = anchor1.find('div',attrs={'class':'CXW8mj'}).find('img').get('src')
            except:
                imglink = "NotFound"

            # anchor2
            try:
                title = anchor2.text
            except:
                title = "NotFound"
            try:
                productrating = link.find('div',attrs={'class':'gUuXy- _2D5lwg'}).find('span',attrs={'span':'_1lRcqv'}).find('div',attrs={'class':'_3LWZlK'}).text
            except:
                productrating = "NotFound"
            # anchor3
            try:
                productlink = 'https://www.flipkart.com' + anchor3.get('href')
            except:
                productlink = "NotFound"
            try:
                pricediv = anchor3.find('div',attrs={'class':'_25b18c'})
            except:
                pricediv = "NotFound"
            try:
                currentprice = pricediv.find('div',attrs={'class':'_30jeq3'}).text
            except:
                currentprice = "NotFound"
            try:
                launchprice = pricediv.find('div',attrs={'class':'_3I9_wc'}).text
            except:
                launchprice = "NotFound"
            try:
                offpercentage = pricediv.find('div',attrs={'class':'_3Ay6Sb'}).text
            except:
                offpercentage = "NotFound"
            try:
                deliverycharges = anchor3.find('div',attrs={'class':'_3tcB5a _2hu4Aw'}).find('div').find('div',attrs={'class':'_2Tpdn3'}).text
            except:
                deliverycharges = "NotFound"
            # try:
            #     pricevstime = link.find('div',attrs={'class':'_2ZdXDB'}).find('div',attrs={'class':'_3xFhiH'}).find('div',attrs={'class':'_2Tpdn3 _18hQoS'}).text
            # except:
            #     pricevstime = "NotFound"

            # print
            print("\033[1;37;1m" +f'Title:' +Fore.YELLOW+f' {title}'+Fore.WHITE)
            print("\033[1;36;1m"+f'Current Price:'+Fore.GREEN+f' {currentprice}'+Fore.WHITE)
            print(Fore.WHITE+f'Launch Price:'+f' {launchprice}')
            print("\033[1;36;1m"+f'Product Rating:'+f' {productrating}')
            print(Fore.WHITE+f'Percentage Off:'+f' {offpercentage}')
            print("\033[1;36;1m"+f'Delivery Charges:'+f' {deliverycharges}')
            # print(f'Time vs Price: {pricevstime}')

            uri = str(productlink)
            label = uri
            if len(uri) > 50:
                label = uri[:50] + "..."
            print(Fore.WHITE+ f'Product Link:' + Fore.MAGENTA+f'{linkx(uri, label)}')

            uri = str(imglink)
            label = uri
            if len(uri) > 50:
                label = uri[:50] + "..."
            print("\033[1;36;1m"+f'Image Link:'+Fore.MAGENTA+ f'{linkx(uri, label)}')
            print(Fore.WHITE+'')
