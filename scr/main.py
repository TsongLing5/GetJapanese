
# from selenium import webdriver
import xlwt
from selenium import webdriver
from bs4 import BeautifulSoup
import time

global nextFlag
url= 'http://jp.qsbdc.com/jpword/index.php'
urlBase='http://jp.qsbdc.com/jpword/'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }


# driver=webdriver.Chrome()
# driver.get('http://jp.qsbdc.com/jpword/index.php')
# # assert "Python" in driver.title
# time.sleep(10)               #留出加载时间
#
# # element=driver.find_element_by_id('chapter-list-1')
# # print(element)
#
# # find element 'chapter-list-1'
#
# soup = BeautifulSoup(driver.page_source, "html.parser")
# par=soup.find('div',class_=['index_r f_r r_bian']).find_all('a')
# print(par)
# print(par[2])
# for i in par:
#     print(i.get_text())
#     driver.get(urlBase + i['href'])
#     time.sleep(10)
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     lessonList = soup.find_all('a', string='列表学习')
#     for j in lessonList:
#         print(j['href'])
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


# print(urlBase+par[0]['href'])
# driver.get(urlBase+par[0]['href'])
# time.sleep(10)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# lessonList=soup.find_all('a',string='列表学习')
# # lessonList=soup.find('div',class_=['index_r f_r r_bian']).find('a')
# # print(lessonList)
# for i in lessonList:
#     print(i['href'])


# print(lessonList)

# word_list.php?lesson_id=400
# http://jp.qsbdc.com/jpword/word_list.php?lesson_id=401&&tag=all&&page_id=1
# wordLink=urlBase+'word_list.php?lesson_id=400'+'&&tag=all&&page_id=1'


# driver.get(urlBase+lessonList[0]['href']+'&&tag=all&&page_id=1')
# driver.get('http://jp.qsbdc.com/jpword/word_list.php?lesson_id=401')
# soup = BeautifulSoup(driver.page_source, "html.parser")
# time.sleep(10)
#
# kana = soup.find_all('span', class_='hidden_2_1')
# Chinese = soup.find_all('span', class_='hidden_3_1')
# for k in Chinese:
#     print(k.string)
#
#
# # nextFlag=soup.find_all('span',style_=['color:grey;'])
# # print(nextFlag)
# # print(len(nextFlag))
# # print(soup.find_all('span',style_='color:grey;').string)
# while(1):
#
#     # print(soup.find_all('span', style='color:grey;'))
#     # print(len(soup.find_all('span',style_=['color:grey;'])))
#     # print(soup.find_all('span',style_=['color:grey;']))
#
#     time.sleep(10)
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#
#     Japanese = soup.find_all('span', class_='hidden_1_1')
#     kana = soup.find_all('span', class_='hidden_2_1')
#     Chinese = soup.find_all('span', class_='hidden_3_1')
#     for k in Chinese:
#         print(k.string)
#
#     nextFlag = soup.find_all('span', style='color:grey;')
#     # print(nextFlag)
#     # print(len(nextFlag))
#
#     if(len(nextFlag)):
#         break;
#     else:
#         driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[23]/td/a[1]').click()



# /html/body/div[5]/div[2]/table/tbody/tr[23]/td/a[1]
# //*[@id="editor-form"]/table/tbody/tr[3]/td/table/tbody/tr/td

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


# print('Program END！')
#
# driver.quit()



def getBookID(url,driver):
    driver.get(url)
    time.sleep(10)  # 留出加载时间
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find('div', class_=['index_r f_r r_bian']).find_all('a')
    return result

def getLessonList(url,driver):

    result=[]
    lessonName=[]
    driver.get(url)
    loop=1
    while (loop):
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        resultTemp = soup.find_all('a', string='列表学习')
        lessonNameTemp=soup.find_all('strong')
        result.extend(resultTemp)
        lessonName.extend(lessonNameTemp)

        nextFlag = soup.find_all('span', style='color:grey;')
        print(nextFlag)
        print(len(nextFlag))

        str = ''
        for k in nextFlag:
            str = str + k.get_text()
        if (len(nextFlag)):

            if('下一页' in str):
                loop = 0
                print('none')
                break
            else:
                driver.find_element_by_partial_link_text('下一页').click()
            # for next in nextFlag:
            #     if ('下一页' in next.string):
            #         print('meiyouzhaodao')
            #         loop = 0
            #         break
            # print('下一页可用')
            # driver.find_element_by_partial_link_text('下一页').click()

            # if('下一页' in nextFlag[0].get_text()):
            #     loop = 0
            #     break
            # elif('下一页' in nextFlag[1].get_text()):
            #     loop = 0
            #     break
            # else:
            #     driver.find_element_by_partial_link_text('下一页').click()

        else:
            # print('下一页')
            driver.find_element_by_partial_link_text('下一页').click()

    return result,lessonName

def getLessonWord(url,driver):
    Japanese=[]
    kana=[]
    Chinese=[]
    # driver.get(urlBase + urlLesson + urlPage + str(page))
    loop=1
    driver.get(url)
    while (loop):
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        par = soup.find('div', class_=['index_r f_r r_bian']).find_all('a')  # for test

        JapaneseTemp = soup.find_all('span', class_='hidden_1_1')

        kanaTemp = soup.find_all('span', class_='hidden_2_1')
        ChineseTemp = soup.find_all('span', class_='hidden_3_1')
        Japanese.extend(JapaneseTemp)
        kana.extend(kanaTemp)
        Chinese.extend(ChineseTemp)
        for k in Japanese:
            print(k.string)

        # for p in par:
        #     print(p.string)

        # nextPage=soup.find_all('a',value='下一页')
        # print(nextPage)
        nextFlag = soup.find_all('span', style='color:grey;')
        print(nextFlag)
        str=''
        for k in nextFlag:
            str=str+k.get_text()
        if (len(nextFlag)):

            # print(nextFlag.get_text())
            if ('下一页' in str):
                loop = 0
                print('none')
                break
            else:
                driver.find_element_by_partial_link_text('下一页').click()

        else:
            # print('下一页')
            driver.find_element_by_partial_link_text('下一页').click()
    return Japanese,kana,Chinese



if __name__=="__main__":
    # url='http://jp.qsbdc.com/jpword/word_list.php?lesson_id=401'

    bookIDList=[]
    driver = webdriver.Chrome()

    bookIDList=getBookID(url,driver)
    for i in bookIDList:
        print(i['href'])

        wb = xlwt.Workbook()
        # sheet = wb.add_sheet()
        lessonList,lessonName=getLessonList(urlBase+i['href'],driver)
        print(lessonName)
        counter=1
        for j in lessonList:
            print(j['href'])
            print(lessonName[counter].get_text())

            sheet = wb.add_sheet(lessonName[counter].get_text())
            counter = counter + 1
            Japanese,kana,Chinese=getLessonWord(urlBase+j['href'],driver)
            row=0
            for ja in Japanese:
                sheet.write(0, row, ja.string)
                row=row+1

        print(i.get_text())
        wb.save(i.get_text())


    driver.quit()
