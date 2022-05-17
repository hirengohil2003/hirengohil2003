#Programme : B.tech CSE
#Name : Gohil Hiren Ashvinbhai
#Enrollment Number : 202103103510017

#---------------------------------------------------------------------------------

#Imporatant Libraries......
from distutils.filelist import findall
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
import re


def parse_review(url):
    #This Are The Basic Steps To GetData From The Website.
    httpObject=urlopen(url)
    webdata=httpObject.read()
    #print(webdata)
    soupdata=soup(webdata,'html.parser')

    containers=soupdata.find_all('div',{'class':'_2kHMtA'})
    #Now Print Information One By One.
    print("\n")
    f=open('ProductPage_Info.csv','wb')
    f.write('ProductName,Stars,Rating,Review,MRP,CurrentPrice,Processor,RAM,Storage,ImageUrl\n'.encode())
    for container in containers:
        #Finding Product Name.
        product=container.findAll('div',{'class':'_4rR01T'})
        ProductName=product[0].text.split('-')[0].strip()
        #Finding Stars
        star=container.find('div','_3LWZlK')
        try:
            Stars=star.text 
        except:
            Stars=0
 
        #Finding Rating and Review Of The Product.
        Rating=container.find('span',{'class':'_2_R_DZ'})
        try:
            ratRev=re.findall('\d+,?\d*',Rating.text) 
            Rating=ratRev[0].replace(',','')
            Review=ratRev[1].replace(',','')
        except:
            Rating=0
            Review=0
    
        #Finding Current Price
        CurrentPrice=container.find('div',{'class':'_30jeq3 _1_WHN1'}).text.replace(',','')
    
        #Finding MRP
        MRP=container.find('div',{'class':'_3I9_wc _27UcVY'}).text.replace(',','')
    
        #Finding Information Of The Product
        info=container.findAll('li',{'class':'rgWa7D'})
        Processor=info[0].text
        RAM=info[1].text
        Storage=info[3].text
        Image=container.img
        ImageUrl=Image.get('src')
    
        print(ProductName,Stars,Rating,Review,MRP,CurrentPrice,Processor,RAM,Storage,ImageUrl)
    
        f.write(f"{ProductName},{Stars},{Rating},{Review},{MRP},{CurrentPrice},{Processor},{RAM},{Storage},{ImageUrl}\n\n".encode())

        print("\n")
    f.close()


parse_review('https://www.flipkart.com/q/best-laptops-under-rs-50000')
pd.read_csv('ProductPage_Info.csv')