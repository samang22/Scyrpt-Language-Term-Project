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
        self.button_summoner_name = Button(self.frame_search, command = self.search)
        self.button_summoner_name.grid(row = 0, column = 1)

        self.frame_records1 = Frame(window)
        self.frame_records1.pack()
        self.label_win = Label(self.frame_records1)
        self.label_win.grid(row = 1, column = 0)
        self.label_champion_portrait = Label(self.frame_records1)
        self.label_champion_portrait.grid(row = 1, column = 1)
        self.label_spell1 = Label(self.frame_records1)
        self.label_spell1.grid(row = 0, column = 2)
        self.label_spell2 = Label(self.frame_records1)
        self.label_spell2.grid(row = 2, column = 2)
        self.label_kda = Label(self.frame_records1)
        self.label_kda.grid(row = 0, column = 3)
        self.label_grade = Label(self.frame_records1)
        self.label_grade.grid(row = 2, column = 3)

        self.label_summoner_champion_list = []
        for i in range(10):
            self.label_summoner_champion_list.append(Label(self.frame_records1))
        for i in range(5):
            self.label_summoner_champion_list[i].grid(row = i, column = 4)
        for i in range(5, 10):
            self.label_summoner_champion_list[i].grid(row = i - 5, column = 6)

        self.label_summoner_name_list = []
        for i in range(10):
            self.label_summoner_name_list.append(Label(self.frame_records1))

        for i in range(5):
            self.label_summoner_name_list[i].grid(row = i, column = 5)
        for i in range(5, 10):
            self.label_summoner_name_list[i].grid(row = i - 5, column = 7)

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

    #def inputDataToLabel(self):


    
Window()



Process.GetSummonerName(summoner_name)

Process.GetSummonerInfo()
Process.GetSummonerLeagueData()
Process.GetSummonerMatchData()
Process.GetSummonerDetailMatchData()
