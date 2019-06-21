
# from selenium import webdriver

from selenium import webdriver
from bs4 import BeautifulSoup
import time

url= 'http://jp.qsbdc.com/jpword/index.php'
urlBase='http://jp.qsbdc.com/jpword/'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }


driver=webdriver.Chrome()
driver.get(url)
# assert "Python" in driver.title
time.sleep(10)               #留出加载时间

# element=driver.find_element_by_id('chapter-list-1')
# print(element)

# find element 'chapter-list-1'

soup = BeautifulSoup(driver.page_source, "html.parser")

par=soup.find('div',class_=['index_r f_r r_bian']).find_all('a')
for i in par:
    print(i['href'])
# li=par.get('href')
# for link in par.find_all('a'):
#     print(link.get('a'))
# print(par)

# lessonList=soup.find_all('tbody','')

# for link in soup.find_all('a'):
#     print(link.get('href'))
# for t2 in lessonList:
#     t3 = t2.get('href')
#     print(t3)
# driver.close()
# print(par[0]['href'])
print(urlBase+par[0]['href'])
driver.get(urlBase+par[0]['href'])
time.sleep(10)
soup = BeautifulSoup(driver.page_source, "html.parser")
lessonList=soup.find_all('a',string='列表学习')
# lessonList=soup.find('div',class_=['index_r f_r r_bian']).find('a')
# print(lessonList)
for i in lessonList:
    print(i['href'])
# print(lessonList)

# word_list.php?lesson_id=400
# http://jp.qsbdc.com/jpword/word_list.php?lesson_id=401&&tag=all&&page_id=1
# wordLink=urlBase+'word_list.php?lesson_id=400'+'&&tag=all&&page_id=1'
driver.get(urlBase+lessonList[0]['href']+'&&tag=all&&page_id=1')
soup = BeautifulSoup(driver.page_source, "html.parser")
time.sleep(10)

kana = soup.find_all('span', class_='hidden_2_1')
Chinese = soup.find_all('span', class_='hidden_3_1')
for k in Chinese:
    print(k.string)

print(soup.find_all('span',style_='color:grey;'))
print(soup.find_all('span',style_='color:grey;').string)
while(len(soup.find_all('span',style_='color:grey;').string) != ""):
    # driver.find_element_by_name("下一页")
    Japanese = soup.find_all('span', class_='hidden_1_1')
    kana = soup.find_all('span', class_='hidden_2_1')
    Chinese = soup.find_all('span', class_='hidden_3_1')
    for k in Chinese:
        print(k.string)

# Japanese=soup.find_all('span',class_='hidden_1_1')
# kana=soup.find_all('span',class_='hidden_2_1')
# Chinese=soup.find_all('span',class_='hidden_3_1')
# partOfSpeech=soup.find_all('span',class_='hidden_2_1')
# print(word[0].string)
# print(word[0]['hidden_2_1'])
# for i in Japanese:
#     print(i.string)
# for j in kana:
#     print(j.string)
# for k in Chinese:
#     print(k.string)

print('Program END！')

driver.quit()




