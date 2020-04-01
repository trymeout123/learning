from plyer import notification
from bs4 import BeautifulSoup
import requests
import time

def notifyMe(title, msg):
        notification.notify( title=title, message=msg, app_icon="icon1.ico", timeout=15)
# something added to new branch
if __name__ == "__main__":
         #just adding  for git test
        data = requests.get('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(data.text, "html.parser")
        #tr =soup.find_all("tbody")
        tr=soup.find_all('div', class_='site-stats-count')
        #this just test 
        str=""
        for x in tr:
            str+=x.text
        # print(str)
        infoList=str.split('\n\n\n\n')
        print(infoList)
        # print(len(infoList))
        # x=len(infoList)
        # #storing last row
        # if(len(infoList[x-1])>1):
        #     last_row=infoList[x-5:]
        # else:
        #     last_row=infoList[x-4:]
        # print(last_row)


        # last_row_col_1=last_row[0].split('\n')[2]
        # # print(last_row_col_1)
        # last_row_col_2=last_row[1].split('\n')[1]
        # # print(last_row_col_2)
        # last_row_col_3 = last_row[2].split('\n')[1]
        # # print(last_row_col_3)
        # # last_row_col_4 = last_row[3].split('\n')[0]
        # # print(last_row_col_1, last_row_col_2, last_row_col_3, last_row_col_4)

        # # str1="{}{}".format("sagar", " chikhale")
        # # detail="Indian confirmed cases  : {}\nForeigner confirmed cases: {}\nCured : {}\nDeath : {}".format(last_row_col_1,last_row_col_2,last_row_col_3,last_row_col_4)
        # detail="Total confirmed cases  : {}\nCured : {}\nDeath : {}".format(last_row_col_1,last_row_col_2,last_row_col_3)
        # notifyMe("CORONA'S EFFECT SO FAR IN INDIA", detail)
        # time.sleep(30)
        # print(tr)
    