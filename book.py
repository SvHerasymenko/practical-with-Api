import requests
import json
from bs4 import BeautifulSoup

bookname=str(input('Enter bookname:'))

def bookinfo(bookname):
    url =f'https://www.googleapis.com/books/v1/volumes?q={bookname}+intitle:keyes&key=AIzaSyCE1fuJ62Yr3qi_6xKcNt7cmgUh_WxXHA8'
    res=requests.get(url).json()

    if res['totalItems'] != 0:
        for items in res['items']:

            try:print('~~~'+items['volumeInfo']['title']+'~~~\n')
            except:...

            try:
                for authors in items['volumeInfo']['authors'] :
                    print('Authors: '+ authors)
            except:...

            try:print('PublishedDate: ' + items['volumeInfo']['publishedDate'])
            except:...

            try:print('PageCount: '+ str(items['volumeInfo']['pageCount']))
            except:...

            try:print('InfoLink: ' + items['volumeInfo']['infoLink'])
            except:...
    else:
        print('Enter the book title correctly')

bookinfo(bookname)