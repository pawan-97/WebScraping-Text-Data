from bs4 import BeautifulSoup
import requests
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

url =  'https://insights.blackcoffer.com/how-artificial-intelligence-can-boost-your-productivity-level/'
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.text,'html.parser')

title = soup.find('h1',class_='entry-title')
contents = soup.find('div',class_='td-post-content').find_all('ol')
for con in contents:
    print(con.text)
# contents = soup.find('div',class_='td-post-content').find_all(['p','h3'])
# subtitle = soup.find('div',class_='td-post-content').find_all()

# paragraph = [content.text for content in contents]
# print(paragraph)