
# -*- coding: utf-8 -*-

import telepot
import time
import ParsedData
import spam

LOLSearchProgress = ParsedData.LOLAPIProcess()
def handle(msg):
    global main
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    LOLSearchProgress.GetSummonerName(text)
    LOLSearchProgress.GetSummonerInfo()
    LOLSearchProgress.GetSummonerLeagueData()
    LOLSearchProgress.GetSummonerMatchData()
    LOLSearchProgress.GetSummonerDetailMatchData()
    result = ""

    count = 0
    for match in range(10):
        count = spam.plusplus(count)
        for i in range(10):
            if LOLSearchProgress.SummonerDetailMatchJsonData[match].summonerName[i] == LOLSearchProgress.SummonerName:
                if LOLSearchProgress.SummonerDetailMatchJsonData[match].win[i] == "True":
                    result += "["+"승리"+"]\n"
                else:
                    result += "["+"패배"+"]\n"
                result += "K/D/A : " + str(LOLSearchProgress.SummonerDetailMatchJsonData[match].kills[i]) + "/" +\
                                                        str(LOLSearchProgress.SummonerDetailMatchJsonData[match].deaths[i]) + "/" +\
                                                        str(LOLSearchProgress.SummonerDetailMatchJsonData[match].assists[i]) + "  "
                result += "챔피언 : " + LOLSearchProgress.SummonerDetailMatchJsonData[match].champion_id[i] + "  "
                result += "소환사 주문 : " + LOLSearchProgress.SummonerDetailMatchJsonData[match].spell1[match] + ", " + \
                    LOLSearchProgress.SummonerDetailMatchJsonData[match].spell2[match] + "\n"
                for o in range(5):
                    result += LOLSearchProgress.SummonerDetailMatchJsonData[match].champion_id[o] + "\t" + \
                            LOLSearchProgress.SummonerDetailMatchJsonData[match].summonerName[o] + "\t\t"
                    result += LOLSearchProgress.SummonerDetailMatchJsonData[match].champion_id[o+5] + "\t" + \
                            LOLSearchProgress.SummonerDetailMatchJsonData[match].summonerName[o+5] + "\n"
                    
        result += "\n"
        result += str(count) + "번 쨰 매치 결과\n"
    bot.sendMessage('765390664', result)


bot = telepot.Bot("634548632:AAEv50ueRuWzIKOPrMT2KgUzRkyttRPJlzs")

bot.message_loop(handle)
print('Listening...')
    

while 1:
  time.sleep(10)


