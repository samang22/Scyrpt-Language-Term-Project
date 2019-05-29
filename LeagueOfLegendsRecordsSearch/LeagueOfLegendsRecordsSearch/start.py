from tkinter import *
import ParsedData

LOLSearchProgress = ParsedData.LOLAPIProcess()



class Window:
    def __init__(self):
        window = Tk()
        self.frame_search = Frame(window)
        self.frame_search.pack()
        self.entry_summoner_name = Entry(self.frame_search)
        self.entry_summoner_name.grid(row = 0, column = 0)
        self.button_summoner_name = Button(self.frame_search, command = self.search, text = "검색")
        self.button_summoner_name.grid(row = 0, column = 1)


        # 랭크 정보
        self.frame_league = Frame(window)
        self.frame_league.pack()
        self.label_tier = Label(self.frame_league)
        self.label_tier.grid(row = 1, column = 0)
        self.label_rank = Label(self.frame_league)
        self.label_rank.grid(row = 1, column = 1)
        self.label_leaguePoints = Label(self.frame_league)
        self.label_leaguePoints.grid(row = 1, column = 2)
        self.label_wins = Label(self.frame_league)
        self.label_wins.grid(row = 1, column = 3)
        self.label_losses = Label(self.frame_league)
        self.label_losses.grid(row = 1, column = 4)

        ## 전적 정보
        #self.frame_records = []
        #self.label_win = []
        #self.label_champion_portrait = []
        #self.label_spell1 = []
        #self.label_spell2 = []
        #self.label_kda = []
        #self.label_grade = []
        #self.label_summoner_champion_list = [[]]
        #self.label_summoner_name_list = [[]]
        #temp_champion_list = []
        #temp_name_list = []
    
        #for o in range(5):
        #    self.frame_records.append(Frame(window))
        #    self.label_win.append(Label(self.frame_records[o]))
        #    self.label_champion_portrait.append(Label(self.frame_records[o]))
        #    self.label_spell1.append(Label(self.frame_records[o]))
        #    self.label_spell2.append(Label(self.frame_records[o]))
        #    self.label_kda.append(Label(self.frame_records[o]))
        #    self.label_grade.append(Label(self.frame_records[o]))
        #    self.frame_records[o].pack()
        #    self.label_win[o].grid(row = 2 + o * 5, column = 0)
        #    self.label_champion_portrait[o].grid(row = 2 + o * 5, column = 1)
        #    self.label_spell1[o].grid(row = 1 + o * 5, column = 2)
        #    self.label_spell2[o].grid(row = 3 + o * 5, column = 2)
        #    self.label_kda[o].grid(row = 0 + o * 5, column = 3)
        #    self.label_grade[o].grid(row = 2 + o * 5, column = 3)
        #    for i in range(10):
        #        #self.label_summoner_champion_list[o][i].append(Label(self.frame_records[o]))
        #        temp_champion_list.append(Label(self.frame_records[o]))
        #    self.label_summoner_champion_list.append(temp_champion_list)
        #    for i in range(5):
        #        self.label_summoner_champion_list[o][i].grid(row = i + o * 5, column = 4)
        #        self.label_summoner_champion_list[o][i + 5].grid(row = i + o * 5, column = 6)

        #    for i in range(10):
        #        self.label_summoner_name_list[o].append(Label(self.frame_records[o]))
        #    for i in range(5):
        #        self.label_summoner_name_list[o][i].grid(row = i + o * 5, column = 5)
        #        self.label_summoner_name_list[o][i + 5].grid(row = i + o * 5, column = 7)

        self.frame_records = Frame(window)
        self.frame_records.pack()
        self.label_win = Label(self.frame_records)
        self.label_win.grid(row = 2, column = 0)
        self.label_champion_portrait = Label(self.frame_records)
        self.label_champion_portrait.grid(row = 2, column = 1)
        self.label_spell1 = Label(self.frame_records)
        self.label_spell1.grid(row = 1, column = 2)
        self.label_spell2 = Label(self.frame_records)
        self.label_spell2.grid(row = 3, column = 2)
        self.label_kda = Label(self.frame_records)
        self.label_kda.grid(row = 0, column = 3)
        self.label_grade = Label(self.frame_records)
        self.label_grade.grid(row = 2, column = 3)
        self.label_summoner_champion_list = []


        for i in range(10):
            self.label_summoner_champion_list.append(Label(self.frame_records))
        for i in range(5):
            self.label_summoner_champion_list[i].grid(row = i, column = 4)
            self.label_summoner_champion_list[i + 5].grid(row = i, column = 6)

        self.label_summoner_name_list = []
        for i in range(10):
            self.label_summoner_name_list.append(Label(self.frame_records))
        for i in range(5):
            self.label_summoner_name_list[i].grid(row = i, column = 5)
            self.label_summoner_name_list[i + 5].grid(row = i, column = 7)

        window.mainloop()

    def search(self):
        global LOLSearchProgress
        LOLSearchProgress.GetSummonerName(self.entry_summoner_name.get())
        self.PasringData()
        self.inputDataToLabel()

    def PasringData(self):
        global LOLSearchProgress
        LOLSearchProgress.GetSummonerInfo()
        LOLSearchProgress.GetSummonerLeagueData()
        LOLSearchProgress.GetSummonerMatchData()
        LOLSearchProgress.GetSummonerDetailMatchData()

    def inputDataToLabel(self):
        global LOLSearchProgress

        #solo_tier = self.
        #solo_summonerName
        #solo_hotStreak = 
        #solo_wins = str(s
        #solo_losses = str
        #solo_rank = str(s
        #solo_leagueName =
        #solo_leagueId = s
        #solo_queueType = 
        #solo_summonerId =
        #solo_leaguePoints
        # 랭크 정보
        self.label_rank["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_rank
        self.label_tier["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_tier
        self.label_leaguePoints["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_leaguePoints
        self.label_wins["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_wins
        self.label_losses["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_losses
        
        # 승패, 게임같이한 인원, 스펠, 챔프, kda, 평점

        for i in range(10):
            self.label_summoner_name_list[i]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[0].summonerName[i]
            self.label_summoner_champion_list[i]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[0].champion_id[i]
        
            if LOLSearchProgress.SummonerDetailMatchJsonData[0].summonerName[i] == LOLSearchProgress.SummonerName:
                if LOLSearchProgress.SummonerDetailMatchJsonData[0].win[i]:
                    self.label_win["text"] = "승리"
                else:
                    self.label_win["text"] = "패배"
        
                self.label_kda["text"] = str(LOLSearchProgress.SummonerDetailMatchJsonData[0].kills[i]) + "/" +\
                                        str(LOLSearchProgress.SummonerDetailMatchJsonData[0].deaths[i]) + "/" +\
                                        str(LOLSearchProgress.SummonerDetailMatchJsonData[0].assists[i])
                self.label_grade["text"] = str((LOLSearchProgress.SummonerDetailMatchJsonData[0].kills[i] + LOLSearchProgress.SummonerDetailMatchJsonData[0].assists[i]) / LOLSearchProgress.SummonerDetailMatchJsonData[0].deaths[i])
                self.label_champion_portrait["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[0].champion_id[i]
                self.label_spell1["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[0].spell1[0]
                self.label_spell2["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[0].spell2[0]

        #for o in range(5):
        #    for i in range(10):
        #        self.label_summoner_name_list[o][i]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[o].summonerName[i]
        #        self.label_summoner_champion_list[o][i]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[o].champion_id[i]

        #        if LOLSearchProgress.SummonerDetailMatchJsonData[o].summonerName[i] == LOLSearchProgress.SummonerName:
        #            if LOLSearchProgress.SummonerDetailMatchJsonData[o].win[i]:
        #                self.label_win["text"] = "승리"
        #            else:
        #                self.label_win["text"] = "패배"

        #            self.label_kda[o]["text"] = str(LOLSearchProgress.SummonerDetailMatchJsonData[o].kills[i]) + "/" +\
        #                                    str(LOLSearchProgress.SummonerDetailMatchJsonData[o].deaths[i]) + "/" +\
        #                                    str(LOLSearchProgress.SummonerDetailMatchJsonData[o].assists[i])
        #            self.label_grade[o]["text"] = str((LOLSearchProgress.SummonerDetailMatchJsonData[o].kills[i] + LOLSearchProgress.SummonerDetailMatchJsonData[0].assists[i]) / LOLSearchProgress.SummonerDetailMatchJsonData[0].deaths[i])
        #            self.label_champion_portrait[o]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[o].champion_id[i]
        #            self.label_spell1[o]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[o].spell1[0]
        #            self.label_spell2[o]["text"] = LOLSearchProgress.SummonerDetailMatchJsonData[o].spell2[0]
        
    
Window()


