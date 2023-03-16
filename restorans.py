import requests 
import json

cityname= str(input('Enter city name: '))

def resttoransInfo(cityname)
    url = f"https://api.yelp.com/v3/businesses/search?location={cityname}&categories=&sort_by=best_match"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer XCGoXidrY1S0p2jYe4trfR2bEZjr3hkfXgvjX5yUUCrn99X3wj-4xx0jKYwCfTC_PFQF1dXXuhyh7k40U0NI1NuPBSt7y9lsUw67XxBYhz9IBjr5OR6MTlhiHWwTZHYx"
    }

    response = requests.get(url, headers=headers).json()

    json = json.dumps(response, indent=4)

    restInfo=[]

    try:
        data= response['businesses']
        for items in data:
            print('\n~~~'+ items['name'] +'~~~\n')
            print('Rating: '+ str(items['rating']))
            print('Location: '+items['location']['address1'])
            print('Review_count: '+str(items['review_count']))
            print('Phone: '+items['phone'])
            print('Url: '+items['url'])
            print("Category:")
            for categories in items['categories']:
                print(categories['title'])
    
    except:print('Enter the city name correctly')

resttoransInfo(cityname)
