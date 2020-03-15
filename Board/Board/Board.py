from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client request
import urllib, urllib.request, urllib.error # .request error handling library (Try, Except)
import datetime
import os
import codecs
import json

#creates main folder with date of scrape
now = datetime.datetime.now()
dirName = now.strftime("%H-%M-%S_%d-%m-%y")
#out_filename = dirName + "/boards.csv"
headers = "Product_id,Product_name,Product_price,Product_category,ProductDirName,Product_description\n"
try:
    os.mkdir(dirName)
    print("Directory " , dirName , " created  ") #creates main dir
    #f = codecs.open(out_filename, "w", encoding="utf-8") #creates main write file in main dir
    #f.write(headers)
    #https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
except FileExistsError:
    print("Directory " , dirName , " already exists")


start_number = 10680 #arbitrary skip of empty array
max_number = 4000 #possible max array size within boards.lt (to avoid empty requests and overloading their site)
product_count = 0 #actual products inbetween


for number in range(start_number, max_number + start_number):
    page_url = ('https://boards.lt/en/home/' + str(number) + '-nitro-2020-squash-snowboard.html')
    print(page_url)
    try: #2.Scraping (attempt to read)
        conn = urllib.request.urlopen(page_url) #opened connection to page_url
    except urllib.error.HTTPError as e: #skip 404 pages
        pass
        # Return code error (e.g. 404, 501, ...)
        #print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e: #skip unrequestable pages
        pass
        # Not an HTTP-specific error (e.g. connection refused)
        # print('URLError: {}'.format(e.reason))
    else:
        # 200

        page_soup = soup(conn.read(), "html.parser", from_encoding="utf-8")
        conn.close() #closing open connection as page is read to memory
        #print(page_soup)
        #write to file for better display
        #f = codecs.open("data.html", "w", encoding="utf-8")
        #f.write(str(page_soup))
     
        productShortInfo = page_soup.find("body",{"id":"product"}).get('class') #short info
        productLongInfo = page_soup.find("section",{"id":"wrapper"}) #full product info
        #print(ProductShortInfo[7]) #67

        productDir = dirName + "/" + productShortInfo[7]
        try:
            os.mkdir(productDir)
            #print("Directory " , productDirName , " created  ")
        except FileExistsError:
             print("Directory " , productShortInfo[7] , " already exists")

        product_Pictures = productLongInfo.findAll({"div":"a"},{"class":"thumb-container"})
        for picture in product_Pictures:
            try:
                #print(picture.a.get('data-image')) #the full image url
                product_Image = picture.a.get('data-image')
                filename = product_Image.split('/')[-2]
                urllib.request.urlretrieve(product_Image, productDir + '/' + filename + '.jpg') #the good one
            except AttributeError:
                pass
   
