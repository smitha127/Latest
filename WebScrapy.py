import requests
from bs4 import BeautifulSoup
import json
from largeauto import Config
import sys

class WebScrapy():

    def __init__(self):
        self.head = Config.obj.headers()
        self.cred = Config.obj.credentials()
        self.url1 = Config.obj.url_store()
        self.url_1 = self.url1[0]
        # print(self.url_1)
        self.header = json.loads(self.head.replace("'", "\""))

    def userLogin(self): #userLogin
        try:
            with requests.session() as session:
                # url_1 = self.url1[0]
                # header = json.loads(self.head.replace("'", "\""))
                credentials = self.cred
                request = session.get(self.url_1, headers=self.header)
                url_2 = self.url1[1]
                request = session.get(url_2)
                WebScrapy.boards(self, request)
        except Exception as e: #ex
            print("Exception in login", e)
            linenum = sys.exc_info()[-1].tb_lineno
            print("", linenum)

    def leanKitBoards(self, r):
        try:
            with requests.session() as session:
                # url_1 = self.url1[0]
                # header = json.loads(self.head.replace("'", "\""))
                request = session.post(self.url_1, data=self.cred, headers=self.header)
                board_no = ["123457855", "111137067", "106606106", "107600350"]
                url_3 = self.url1
                url_4 = self.url1[3]
                print(type(url_4))
                for i in board_no:
                    request = session.get(url_3 + i + url_4 + i + "")
                    soup1 = BeautifulSoup(r.content, 'lxml')
                    cards1 = soup1.find("p")
                    cards2 = cards1.text
                    listofcards = []
                    card_Nos = {}
                    card_Nos = json.loads(cards2) # variables in lowercase
                    asd = card_Nos['cards']
                    for i in range(len(asd)):
                        listofcards.append(card_Nos['cards'][i]['id'])
                        WebScrapy.getcard_data(self, listofcards)
        except Exception as e:
            print(e)
            linenumer = sys.exc_info()[-1].tb_lineno
            print(linenumer)

    def getcard_data(self, li):
        try:
            with requests.session() as s:
                # url_1 = self.url1[0]
                # header = json.loads(self.head.replace("'", "\""))
                r = s.post(self.url_1, data=self.cred, headers=self.header)
                listofcards = li
                url_5 = self.url1[4]
                consession_list = []
                for i in listofcards:
                    try:
                        r = s.get(url_5 + i + "?id=" + i + "")
                        soup = BeautifulSoup(r.content, 'lxml')
                        card = soup.findAll(text=True)
                        if len(card) > 1:
                            card = card[0] + card[len(card) - 1]
                        elif len(card) == 1:
                            card = card[0]
                        card_Details = json.loads(card)
                        card_body = soup.find('body')
                        plannedFinish = card_Details['plannedfinish']
                        externalLinks = card_Details['external_links']
                        customId_Consession_no = card_Details['customId']['value']
                        if (externalLinks != []):
                            externalLinks = card_Details['external_links'][0]['url']
                        elif (externalLinks == None):
                            external_links = card_Details['external_Links'][0]['label']
                        elif (external_links == []):
                            externalLinks = soup.findAll(text=True)[1]
                        card_ID = card_Details['id']
                        lane_ID = card_Details['lane']['id']
                        lane_ClassType = card_Details['lane']['laneClassType']
                        lane_title = card_Details['lane']['title']
                        priority = card_Details['priority']
                        card_size = card_Details['size']
                        card_title = card_Details['title']
                        card_title1 = card_title.split(" ")
                        engine_no = card_title1[0]
                        engpartNo = str(card_title1[1:])
                        card_type = card_Details['type']['title']
                        if (lane_ClassType != "active"):
                            card_Details_data = {"card_title": card_title, "engine_no": engine_no, "partNo": engpartNo,
                                                 "customId_Consession_no": customId_Consession_no,
                                                 "plannedFinish": plannedFinish, "external_links": external_links,
                                                 "card_ID": card_ID,
                                                 "lane_ID": lane_ID, "lane_ClassType": lane_ClassType,
                                                 "priority": priority,
                                                 "card_size": card_size, "card_type": card_type}
                            # return card_Details_data
                            print(card_Details_data)
                    except:
                        pass

        except Exception as e:
            print(e)
            linenum = sys.exc_info()[-1].tb_lineno
            print(linenum)
