# -*- coding: utf-8 -*-


#global value
from tkinter import *
from tkinter import font
import ParsedData

import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
LOLSearchProgress = ParsedData.LOLAPIProcess()



class Window:
    def __init__(self):
        window = Tk()
        window.geometry("400x600+700+200")
        TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
        MainText = Label(window, font = TempFont, text="[롤 전적검색 App]")
        MainText.pack()
        MainText.place(x=75)
        #self.frame_search = Frame(window)
        #self.frame_search.pack()
        self.entry_summoner_name = Entry(window)
        self.entry_summoner_name.pack(side = LEFT)
        self.entry_summoner_name.place(x = 110, y = 50)
        self.button_summoner_name = Button(window, command = self.search, text = "검색")
        self.button_summoner_name.pack()
        self.button_summoner_name.place(x = 250, y = 45)


        # 랭크 정보
        #self.frame_league = Frame(window)
        #self.frame_league.pack()
        self.photo_tear = {"default" : PhotoImage(file = "default.png")}
        self.photo_tear["SILVER"] = PhotoImage(file = "iron.png")
        self.photo_tear["BRONZE"] = PhotoImage(file = "bronze.png")
        self.photo_tear["SILVER"] = PhotoImage(file = "silver.png")
        self.photo_tear["GOLD"] = PhotoImage(file = "gold.png")
        self.photo_tear["PLATINUM"] = PhotoImage(file = "platinum.png")
        self.photo_tear["DIAMOND"] = PhotoImage(file = "diamond.png")
        self.photo_tear["MASTER"] = PhotoImage(file = "master.png")
        self.photo_tear["GRANDMASTER"] = PhotoImage(file = "grandmaster.png")
        self.photo_tear["CHALLENGER"] = PhotoImage(file = "challenger.png")



        self.label_image_tier = Label(window, image = self.photo_tear["default"])
        self.label_image_tier.pack()
        self.label_image_tier.place(x = 0, y = 70)
        #self.label_tier = Label(window, bg = "red", text = "tier")
        self.label_tier = Label(window)
        self.label_tier.pack()
        self.label_tier.place(x = 130, y = 120)
        #self.label_rank = Label(window, bg = "red", text = "rank")
        self.label_rank = Label(window)
        self.label_rank.pack()
        self.label_rank.place(x = 190, y = 120)
        #self.label_leaguePoints = Label(window, bg = "red", text = "lp")
        self.label_leaguePoints = Label(window)
        self.label_leaguePoints.pack()
        self.label_leaguePoints.place(x = 210, y = 120)
        #self.label_wins = Label(window, bg = "red", text = "wins")
        self.label_wins = Label(window)
        self.label_wins.pack()
        self.label_wins.place(x = 130, y = 150)
        #self.label_losses = Label(window, bg = "red", text = "losses")
        self.label_losses = Label(window)
        self.label_losses.pack()
        self.label_losses.place(x = 210, y = 150)

        self.canvas_width = 140
        self.canvas_height = 140
        self.canvas_winsLossesGraph = Canvas(window, width = 140, height = 140, bg = "white")
        self.canvas_winsLossesGraph.pack()
        self.canvas_winsLossesGraph.place(x = 250, y = 70)

        self.scrollbar_records = Scrollbar(window)
        self.scrollbar_records.pack()
        # 스크롤바 좌표

        RecordsTextFont = font.Font(window, size = 10, weight = 'bold', family = 'Consolas')
        self.text_records = Text(window, font = RecordsTextFont, width = 50, height = 21, borderwidth = 12, relief = 'ridge', yscrollcommand=self.scrollbar_records.set)
        self.text_records.pack()
        self.text_records.place(x = 10, y = 220)
        self.scrollbar_records.config(command = self.text_records.yview)
        self.scrollbar_records.pack(side = RIGHT, fill = BOTH)
        self.text_records.configure(state = 'normal')

        # 이메일 전송
        self.button_sendEmail = Button(window, text = "이메일 전송", command = self.sendEmail)
        self.button_sendEmail.pack()
        self.button_sendEmail.place(x = 300, y = 570)
        self.entry_emailInsert = Entry(window)
        self.entry_emailInsert.pack()
        self.entry_emailInsert.place(x = 150, y = 565)

        ### 전적 정보
        #self.label_win = []
        #self.label_champion_portrait = []
        #self.label_spell1 = []
        #self.label_spell2 = []
        #self.label_kda = []
        #self.label_grade = []
        #self.label_summoner_champion_list = []
        #self.label_summoner_name_list = []
        #temp_champion_list = []
        #temp_name_list = []
    
        #for o in range(5):
        #    self.frame_records.append(Frame(window))
        #    self.frame_records[o].pack()
        #    self.label_win.append(Label(self.frame_records[o]))
        #    self.label_champion_portrait.append(Label(self.frame_records[o]))
        #    self.label_spell1.append(Label(self.frame_records[o]))
        #    self.label_spell2.append(Label(self.frame_records[o]))
        #    self.label_kda.append(Label(self.frame_records[o]))
        #    self.label_grade.append(Label(self.frame_records[o]))
        #    self.label_win[o].pack(side = LEFT)
        #    self.label_champion_portrait[o].pack(side = LEFT)
        #    self.label_spell1[o].pack(side = LEFT)
        #    self.label_spell2[o].pack(side = LEFT)
        #    self.label_kda[o].pack(side = LEFT)
        #    self.label_grade[o].pack(side = LEFT)
        #    #self.label_win[o].grid(row = 2 + o * 5, column = 0)
        #    #self.label_champion_portrait[o].grid(row = 2 + o * 5, column = 1)
        #    #self.label_spell1[o].grid(row = 1 + o * 5, column = 2)
        #    #self.label_spell2[o].grid(row = 3 + o * 5, column = 2)
        #    #self.label_kda[o].grid(row = 0 + o * 5, column = 3)
        #    #self.label_grade[o].grid(row = 2 + o * 5, column = 3)
        #    for i in range(10):
        #        #self.label_summoner_champion_list[o][i].append(Label(self.frame_records[o]))
        #        temp_champion_list.append(Label(self.frame_records[o]))
        #    self.label_summoner_champion_list.append(temp_champion_list)
        #    #for i in range(5):
        #    #    #self.label_summoner_champion_list[o][i].grid(row = i + o * 5, column = 4)
        #    #    #self.label_summoner_champion_list[o][i + 5].grid(row = i + o * 5, column = 6)
        #    #    self.label_summoner_champion_list[o][i].pack(side = LEFT)
        #    #    self.label_summoner_champion_list[o][i + 5].pack(side = LEFT)
        #    for i in range(10):
        #        #self.label_summoner_champion_list[o][i].grid(row = i + o * 5, column = 4)
        #        #self.label_summoner_champion_list[o][i + 5].grid(row = i + o * 5, column = 6)
        #        self.label_summoner_champion_list[o][i].pack(side = RIGHT)

        #    for i in range(10):
        #        temp_name_list.append(Label(self.frame_records[o]))
        #    self.label_summoner_name_list.append(temp_name_list)
        #    #for i in range(5):
        #    #    #self.label_summoner_name_list[o][i].grid(row = i + o * 5, column = 5)
        #    #    #self.label_summoner_name_list[o][i + 5].grid(row = i + o * 5, column = 7)
        #    #    self.label_summoner_name_list[o][i].pack(side = LEFT)
        #    #    self.label_summoner_name_list[o][i + 5].pack(side = LEFT)
        #    for i in range(10):
        #        self.label_summoner_name_list[o][i].pack(side = RIGHT)

        ##self.frame_records = Frame(window)
        ##self.frame_records.pack()
        ##self.label_win = Label(self.frame_records)
        ##self.label_win.grid(row = 2, column = 0)
        ##self.label_champion_portrait = Label(self.frame_records)
        ##self.label_champion_portrait.grid(row = 2, column = 1)
        ##self.label_spell1 = Label(self.frame_records)
        ##self.label_spell1.grid(row = 1, column = 2)
        ##self.label_spell2 = Label(self.frame_records)
        ##self.label_spell2.grid(row = 3, column = 2)
        ##self.label_kda = Label(self.frame_records)
        ##self.label_kda.grid(row = 0, column = 3)
        ##self.label_grade = Label(self.frame_records)
        ##self.label_grade.grid(row = 2, column = 3)
        ##self.label_summoner_champion_list = []


        ##for i in range(10):
        ##    self.label_summoner_champion_list.append(Label(self.frame_records))
        ##for i in range(5):
        ##    self.label_summoner_champion_list[i].grid(row = i, column = 4)
        ##    self.label_summoner_champion_list[i + 5].grid(row = i, column = 6)

        ##self.label_summoner_name_list = []
        ##for i in range(10):
        ##    self.label_summoner_name_list.append(Label(self.frame_records))
        ##for i in range(5):
        ##    self.label_summoner_name_list[i].grid(row = i, column = 5)
        ##    self.label_summoner_name_list[i + 5].grid(row = i, column = 7)

        window.mainloop()

    def search(self):
        global LOLSearchProgress
        LOLSearchProgress.GetSummonerName(self.entry_summoner_name.get())
        self.PasringData()
        self.inputDataToLabel()

    def sendEmail(self):
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        #htmlFileName = "logo.html"
        
        senderAddr = "minhyuk5757@gmail.com"     # 보내는 사람 email 주소.
        recipientAddr = self.entry_emailInsert.get()   # 받는 사람 email 주소.
        
        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = self.entry_summoner_name.get() + "님의 리그오브레전드 전적 검색 정보입니다."
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        
        ## MIME 문서를 생성합니다.
        #htmlFD = open(htmlFileName, 'rb')
        #HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
        #htmlFD.close()
        HtmlPart = MIMEText(self.text_records.get(1.0, END))
        
        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)
        
        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("minhyuk5757@gmail.com","5080700g")
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()


    def PasringData(self):
        global LOLSearchProgress
        LOLSearchProgress.GetSummonerInfo()
        LOLSearchProgress.GetSummonerLeagueData()
        LOLSearchProgress.GetSummonerMatchData()
        LOLSearchProgress.GetSummonerDetailMatchData()

    def inputDataToLabel(self):
        global LOLSearchProgress


        self.label_image_tier["image"] = self.photo_tear[LOLSearchProgress.SummonerLeagueJsonData.solo_tier]
        self.label_rank["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_rank
        self.label_tier["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_tier
        self.label_leaguePoints["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_leaguePoints+ "LP"
        self.label_wins["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_wins + "승"
        self.label_losses["text"] = LOLSearchProgress.SummonerLeagueJsonData.solo_losses + "패"
        
        self.text_records.delete(1.0, END)

        # 승패, 게임같이한 인원, 스펠, 챔프, kda, 평점
        for match in range(10):
            for i in range(10):
                if LOLSearchProgress.SummonerDetailMatchJsonData[match].summonerName[i] == LOLSearchProgress.SummonerName:
                    if LOLSearchProgress.SummonerDetailMatchJsonData[match].win[i] == "True":
                        self.text_records.insert(INSERT, "["+"승리"+"]\n")
                    else:
                        self.text_records.insert(INSERT, "["+"패배"+"]\n")
                    self.text_records.insert(INSERT, "K/D/A : " + str(LOLSearchProgress.SummonerDetailMatchJsonData[match].kills[i]) + "/" +\
                                                            str(LOLSearchProgress.SummonerDetailMatchJsonData[match].deaths[i]) + "/" +\
                                                            str(LOLSearchProgress.SummonerDetailMatchJsonData[match].assists[i]) + "  ") 
                    self.text_records.insert(INSERT, "챔피언 : " + LOLSearchProgress.SummonerDetailMatchJsonData[match].champion_id[i] + "  ")
                    self.text_records.insert(INSERT, "소환사 주문 : " + LOLSearchProgress.SummonerDetailMatchJsonData[match].spell1[match] + ", " + \
                        LOLSearchProgress.SummonerDetailMatchJsonData[match].spell2[match] + "\n")
                    for o in range(5):
                        self.text_records.insert(INSERT, LOLSearchProgress.SummonerDetailMatchJsonData[match].champion_id[o] + "\t" + \
                                LOLSearchProgress.SummonerDetailMatchJsonData[match].summonerName[o] + "\t\t")
                        self.text_records.insert(INSERT, LOLSearchProgress.SummonerDetailMatchJsonData[match].champion_id[o+5] + "\t" + \
                                LOLSearchProgress.SummonerDetailMatchJsonData[match].summonerName[o+5] + "\n")
                    self.text_records.insert(INSERT, "\n")

        
        self.canvas_winsLossesGraph.delete("graph")
        winHeight = self.canvas_height * int(LOLSearchProgress.SummonerLeagueJsonData.solo_wins) / (int(LOLSearchProgress.SummonerLeagueJsonData.solo_wins) + int(LOLSearchProgress.SummonerLeagueJsonData.solo_losses))
        loseHeight = self.canvas_height * int(LOLSearchProgress.SummonerLeagueJsonData.solo_losses) / (int(LOLSearchProgress.SummonerLeagueJsonData.solo_wins) + int(LOLSearchProgress.SummonerLeagueJsonData.solo_losses))
        self.canvas_winsLossesGraph.create_rectangle(30, 140 - winHeight, 60, 140, fill = "blue", tags = "graph")
        self.canvas_winsLossesGraph.create_rectangle(80, 140 - loseHeight, 110, 140, fill = "red", tags = "graph")


        
    
Window()


