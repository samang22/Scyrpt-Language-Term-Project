#https://api.neople.co.kr/df/items?itemName=<itemName>&q=minLevel:<minLevel>,maxLevel:<maxLevel>,rarity:<rarity>,trade:<trade>&limit=<limit>&wordType=<wordType>&apikey=ppMk2pUeHbk6Wi0dazKt7YM4PvkTnzDB
import webbrowser
import urllib.request
import urllib.parse

import json
import os
from tkinter import *
from tkinter.ttk import *

from tkinter.font import *
import http.client

#JSON 파일을 딕셔너리로 파싱하기
my_api_key = "RGAPI-20f33bb9-dd69-4562-a966-0440eb963870"

# 소환사 정보 : 닉네임으로 검색
# id        # 리그 정보 검색에 필요
# accountId
# puuid
# name
# profileIconId
# revisionDate
# summonerLevel

# 리그 정보 : id 로 검색
# 솔랭
# tier
# summonerName
# hotStreak 연승
# wins 승수
# losses 패배
# rank 랭크
# leagueName 리그이름
# leagueId
# queueType
# summonerId
# leaguePoints": 23
# 자유랭 반복

my_api_key = "RGAPI-20f33bb9-dd69-4562-a966-0440eb963870"

class LOLAPIProcess:

    def GetSummonerName(self, SummonerName):

        if (SummonerName == ""):
            print("비어있는입력")
            return

        #파싱 ..
        SummonerName = urllib.parse.quote(SummonerName)

        server = "kr.api.riotgames.com"  

        summoner_url = "/lol/summoner/v4/summoners/by-name/" + SummonerName + "?api_key=" + my_api_key

        conn = http.client.HTTPSConnection(server)

        conn.request("GET", summoner_url)
        response = conn.getresponse()
        cLen = response.getheader("Content-Length")  # 헤더에서 Content-Length 즉 얼만큼 읽었는지 추출
        result = response.read(int(cLen)).decode('utf-8')

        SummonerJsonData = ParsingSummonerData(result) #파싱한 JSON 데이터를 요소별로 객체에 저장ㅇ한 클래스



	##이미지 파일 얻어오는코드
 #       url = "https://img-api.neople.co.kr/df/items/" + jsonData.itemID
 #       outpath = "images/"
 #       outfile = "image_" +jsonData.itemName + ".png"

 #       if not os.path.isdir(outpath):
 #           os.makedirs(outpath)

 #       urllib.request.urlretrieve(url, outpath + outfile)
	#여기까지

        print(SummonerJsonData)





class ParsingSummonerData:
    def __init__(self, JSON):
        self.jsonData = json.loads(JSON) #string 형태의 JSON 객체를 딕셔너리로 바꾼다



        #self.id = self.jsonData["rows"][0]["id"]
        #self.accountId = self.jsonData["rows"][0]["itemName"]
        #self.itemRarity = self.jsonData["rows"][0]["itemRarity"]
        #self.itemType = self.jsonData["rows"][0]["itemType"]
        #self.itemDetail = str(self.jsonData["rows"][0]["itemTypeDetail"])
        #self.itemAvailableLevel = str(self.jsonData["rows"][0]["itemAvailableLevel"])

        self.id = str(self.jsonData["id"])
        self.accountId = str(self.jsonData["accountId"])
        self.puuid = str(self.jsonData["puuid"])
        self.name = str(self.jsonData["name"])
        self.profileIconId = str(self.jsonData["profileIconId"])
        self.revisionDate = str(self.jsonData["revisionDate"])
        self.summonerLevel = str(self.jsonData["summonerLevel"])

    def __str__(self):
        return "[id : " + self.id + \
            "]\n[accountId : " + self.accountId + \
            "]\n[puuid : " + self.puuid + \
            "]\n[name : " + self.name + \
            "]\n[profileIconId : " + self.profileIconId + \
            "]\n[revisionData : " + self.revisionDate + \
            "]\n[summonerLevel : " + self.summonerLevel + "]" 

    def getid(self):
        return self.id

# 리그 정보 : id 로 검색
# 솔랭
# tier
# summonerName
# hotStreak 연승
# wins 승수
# losses 패배
# rank 랭크
# leagueName 리그이름
# leagueId
# queueType
# summonerId
# leaguePoints": 23
# 자유랭 반복

class ParsingSummonerLeagueData:
    def __init__(self, JSON):
        self.jsonData = json.loads(JSON) #string 형태의 JSON 객체를 딕셔너리로 바꾼다


        self.tier = str(self.jsonData["tier"])
        self.summonerName = str(self.jsonData["summonerName"])
        self.hotStreak = str(self.jsonData["hotStreak"])
        self.wins = str(self.jsonData["wins"])
        self.losses = str(self.jsonData["losses"])
        self.rank = str(self.jsonData["rank"])
        self.leagueName = str(self.jsonData["leagueName"])
        self.leagueId = str(self.jsonData["leagueId"])
        self.queueType = str(self.jsonData["queueType"])
        self.summonerId = str(self.jsonData["summonerId"])
        self.leaguePoints = str(self.jsonData["leaguePoints"])


    def __str__(self):
        return "[tier : " + \
            self.tier + "]\n[summonerName : " + \
            self.summonerName + "]\n[hotStreak : " + \
            self.hotStreak + "]\n[wins : " + \
            self.wins + "]\n[losses : " + \
            self.losses + "]\n[rank" + \
            self.rank + "]\n[leagueName : " + \
            self.leagueName + "]\n[leagueId : " + \
            self.leagueId + "]\n[queueType : " + \
            self.queueType + "]\n[summonerId : " + \
            self.summonerId + "]\n[leaguePoints : " + \
            self.leaguePoints + "]"

    def getid(self):
        return self.id



LOLAPIProcess().GetSummonerName("사망합니다")