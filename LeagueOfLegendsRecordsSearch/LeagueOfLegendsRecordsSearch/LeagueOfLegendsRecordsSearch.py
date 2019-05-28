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

my_api_key = "RGAPI-1d01a975-e32d-4e86-8e44-0f90de28f81a"
class LOLAPIProcess:
    def GetSummonerName(self, SummonerName):

        if (SummonerName == ""):
            print("비어있는입력")
            return
        else:
            self.SummonerName = SummonerName

    def GetSummonerInfo(self):
        #파싱 ..
        if self.SummonerName == None:
            print("소환사 이름이 제대로 입력되지 않았습니다.")
            return

        ParsedSummonerName = urllib.parse.quote(self.SummonerName)

        server = "kr.api.riotgames.com"  

        summoner_url = "/lol/summoner/v4/summoners/by-name/" + ParsedSummonerName + "?api_key=" + my_api_key
        self.conn = http.client.HTTPSConnection(server)

        self.conn.request("GET", summoner_url)
        response = self.conn.getresponse()
        if 200 != response.code: 
            print("없는 소환사명입니다.")
            return
        cLen = response.getheader("Content-Length")  # 헤더에서 Content-Length 즉 얼만큼 읽었는지 추출
        result = response.read(int(cLen)).decode('utf-8')

        self.SummonerJsonData = ParsingSummonerData(result) #파싱한 JSON 데이터를 요소별로 객체에 저장ㅇ한 클래스
    
        
    def GetSummonerLeagueData(self):
        summoner_league_url = "/lol/league/v4/positions/by-summoner/" + self.SummonerJsonData.id + "?api_key=" + my_api_key
        self.conn.request("GET", summoner_league_url)
        response = self.conn.getresponse()
        cLen = response.getheader("Content-Length")  # 헤더에서 Content-Length 즉 얼만큼 읽었는지 추출
        result = response.read(int(cLen)).decode('utf-8')
        self.SummonerLeagueJsonData = ParsingSummonerLeagueData(result)

    def GetSummonerMatchData(self):
        summoner_match_url = "/lol/match/v4/matchlists/by-account/" + self.SummonerJsonData.accountId +"?api_key="+my_api_key
        self.conn.request("GET", summoner_match_url)
        response = self.conn.getresponse()
        cLen = response.getheader("Content-Length")  # 헤더에서 Content-Length 즉 얼만큼 읽었는지 추출
        #13523

        #if cLen != None:
        #    result = response.read(int(cLen)).decode('utf-8')
        #    self.SummonerLeagueJsonData = ParsingSummonerMatchData(result)
        #else:
        #    print("매치데이터 읽어오기 실패")
        result = response.read(15000).decode('utf-8')
        self.SummonerMatchJsonData = ParsingSummonerMatchData(result)



	##이미지 파일 얻어오는코드
 #       url = "https://img-api.neople.co.kr/df/items/" + jsonData.itemID
 #       outpath = "images/"
 #       outfile = "image_" +jsonData.itemName + ".png"

 #       if not os.path.isdir(outpath):
 #           os.makedirs(outpath)

 #       urllib.request.urlretrieve(url, outpath + outfile)
	#여기까지
    def PrintSummonerData(self):
        print(self.SummonerJsonData)

    def PrintSummonerLeagueData(self):
        print(self.SummonerLeagueJsonData)

    def PrintSummonerMatchData(self):
        print(self.SummonerMatchJsonData)


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
            "]\n[summonerLevel : " + self.summonerLevel + "]\n\n" 

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

        self.solo_tier = self.jsonData[0]["tier"]
        self.solo_summonerName = str(self.jsonData[0]["summonerName"])
        self.solo_hotStreak = str(self.jsonData[0]["hotStreak"])
        self.solo_wins = str(self.jsonData[0]["wins"])
        self.solo_losses = str(self.jsonData[0]["losses"])
        self.solo_rank = str(self.jsonData[0]["rank"])
        self.solo_leagueName = str(self.jsonData[0]["leagueName"])
        self.solo_leagueId = str(self.jsonData[0]["leagueId"])
        self.solo_queueType = str(self.jsonData[0]["queueType"])
        self.solo_summonerId = str(self.jsonData[0]["summonerId"])
        self.solo_leaguePoints = str(self.jsonData[0]["leaguePoints"])

        #self.free_tier = self.jsonData[1]["tier"]
        #self.free_summonerName = str(self.jsonData[1]["summonerName"])
        #self.free_hotStreak = str(self.jsonData[1]["hotStreak"])
        #self.free_wins = str(self.jsonData[1]["wins"])
        #self.free_losses = str(self.jsonData[1]["losses"])
        #self.free_rank = str(self.jsonData[1]["rank"])
        #self.free_leagueName = str(self.jsonData[1]["leagueName"])
        #self.free_leagueId = str(self.jsonData[1]["leagueId"])
        #self.free_queueType = str(self.jsonData[1]["queueType"])
        #self.free_summonerId = str(self.jsonData[1]["summonerId"])
        #self.free_leaguePoints = str(self.jsonData[1]["leaguePoints"])

    def __str__(self):
        return "[solo]\n" + \
            "[tier : " + self.solo_tier + \
            "]\n[summonerName : " + self.solo_summonerName + \
            "]\n[hotStreak : " + self.solo_hotStreak + \
            "]\n[wins : " + self.solo_wins + \
            "]\n[losses : " + self.solo_losses + \
            "]\n[rank : " +  self.solo_rank + \
            "]\n[leagueName : " + self.solo_leagueName + \
            "]\n[leagueId : " + self.solo_leagueId + \
            "]\n[queueType : " + self.solo_queueType + \
            "]\n[summonerId : " + self.solo_summonerId + \
            "]\n[leaguePoints : " + self.solo_leaguePoints + "]\n\n"
            #"]\n[leaguePoints : " + self.solo_leaguePoints + "]\n" + \
            #"[free]\n" + \
            #"[tier : " + self.solo_tier + \
            #"]\n[summonerName : " + self.solo_summonerName + \
            #"]\n[hotStreak : " + self.solo_hotStreak + \
            #"]\n[wins : " + self.solo_wins + \
            #"]\n[losses : " + self.solo_losses + \
            #"]\n[rank" +  self.solo_rank + \
            #"]\n[leagueName : " + self.solo_leagueName + \
            #"]\n[leagueId : " + self.solo_leagueId + \
            #"]\n[queueType : " + self.solo_queueType + \
            #"]\n[summonerId : " + self.solo_summonerId + \
            #"]\n[leaguePoints : " + self.solo_leaguePoints + "]"

class ParsingSummonerMatchData:
    def __init__(self, JSON):
        self.jsonData = json.loads(JSON) #string 형태의 JSON 객체를 딕셔너리로 바꾼다

        #self.platformId = self.jsonData[0]["platformId"]
        #self.gameId = str(self.jsonData[0]["gameId"])
        #self.champion = str(self.jsonData[0]["champion"])
        #self.queue = str(self.jsonData[0]["queue"])
        #self.season = str(self.jsonData[0]["season"])
        #self.timestamp = str(self.jsonData[0]["timestamp"])
        #self.role = str(self.jsonData[0]["role"])
        #self.lane = str(self.jsonData[0]["lane"])

        self.platformId = []
        self.gameId = []
        self.champion = []
        self.queue = []
        self.season = []
        self.timestamp = []
        self.role = []
        self.lane = []


        for n in range(int(self.jsonData["endIndex"])):
            self.platformId.append(self.jsonData["matches"][n]["platformId"])
            self.gameId.append(str(self.jsonData["matches"][n]["gameId"]))
            self.champion.append(str(self.jsonData["matches"][n]["champion"]))
            self.queue.append(str(self.jsonData["matches"][n]["queue"]))
            self.season.append(str(self.jsonData["matches"][n]["season"]))
            self.timestamp.append(str(self.jsonData["matches"][n]["timestamp"]))
            self.role.append(str(self.jsonData["matches"][n]["role"]))
            self.lane.append(str(self.jsonData["matches"][n]["lane"]))


    def __str__(self):
        return \
            "[platformId : " + self.platformId[0] + \
            "]\n[gameId : " + self.gameId[0] + \
            "]\n[champion : " + self.champion[0] + \
            "]\n[queue : " + self.queue[0] + \
            "]\n[season : " + self.season[0] + \
            "]\n[timestamp" +  self.timestamp[0] + \
            "]\n[role : " + self.role[0] + \
            "]\n[lane : " + self.lane[0] + "]\n" \
                + \
            "[platformId : " + self.platformId[1] + \
            "]\n[gameId : " + self.gameId[1] + \
            "]\n[champion : " + self.champion[1] + \
            "]\n[queue : " + self.queue[1] + \
            "]\n[season : " + self.season[1] + \
            "]\n[timestamp" +  self.timestamp[1] + \
            "]\n[role : " + self.role[1] + \
            "]\n[lane : " + self.lane[1] + "]\n" \
                + \
            "[platformId : " + self.platformId[2] + \
            "]\n[gameId : " + self.gameId[2] + \
            "]\n[champion : " + self.champion[2] + \
            "]\n[queue : " + self.queue[2] + \
            "]\n[season : " + self.season[2] + \
            "]\n[timestamp" +  self.timestamp[2] + \
            "]\n[role : " + self.role[2] + \
            "]\n[lane : " + self.lane[2] + "]\n" \
                + \
            "[platformId : " + self.platformId[3] + \
            "]\n[gameId : " + self.gameId[3] + \
            "]\n[champion : " + self.champion[3] + \
            "]\n[queue : " + self.queue[3] + \
            "]\n[season : " + self.season[3] + \
            "]\n[timestamp" +  self.timestamp[3] + \
            "]\n[role : " + self.role[3] + \
            "]\n[lane : " + self.lane[3] + "]\n" \
                + \
            "[platformId : " + self.platformId[4] + \
            "]\n[gameId : " + self.gameId[4] + \
            "]\n[champion : " + self.champion[4] + \
            "]\n[queue : " + self.queue[4] + \
            "]\n[season : " + self.season[4] + \
            "]\n[timestamp" +  self.timestamp[4] + \
            "]\n[role : " + self.role[4] + \
            "]\n[lane : " + self.lane[4] + "]\n\n" \
            




Process = LOLAPIProcess()
summoner_name = str(input("소환사 이름 입력 : "))
Process.GetSummonerName(summoner_name)
Process.GetSummonerInfo()
Process.GetSummonerLeagueData()
Process.GetSummonerMatchData()
Process.PrintSummonerData()
Process.PrintSummonerLeagueData()
Process.PrintSummonerMatchData()


