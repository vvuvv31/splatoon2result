import os
import requests
import json
from time import sleep
import iksm

#path = "/www/wwwroot/82.157.137.92/splatoonresult/"
#path = "D:/Program_Python/webresult/"
path = ''
url = "https://app.splatoon2.nintendo.net/api/results"
obstext = path + "result.txt"

def get_iksm():
    if os.path.exists(path + "iksm.txt"):
        read_iksm = open(path + "iksm.txt","r")
        iksm_session = read_iksm.read()
        read_iksm.close()
        cookie = {"iksm_session" : iksm_session}
        return cookie
    else:
        iksm.save_cookie()
def Updateresult():
    cookies = get_iksm()
    r = requests.get(url, cookies=cookies)
    jsondata = json.loads(r.text)
    if "results" in jsondata:
        with open(obstext, 'w', encoding="utf-8") as f:
            if jsondata["results"][0]["my_team_result"]["key"] == "victory":
                winlose = "win   "
            elif jsondata["results"][0]["my_team_result"]["key"] == "defeat":
                winlose = "lose   "
            kcount = jsondata["results"][0]["player_result"]["kill_count"]
            acount = jsondata["results"][0]["player_result"]["assist_count"]
            dcount = jsondata["results"][0]["player_result"]["death_count"]
            scount = jsondata["results"][0]["player_result"]["special_count"]
            res =winlose + str(kcount + acount) + "(" + str(acount) + ")" + " " + str(dcount) + " " + str(scount)
            if jsondata["results"][0]["type"] == "league":
                league_data = '全队' +str(jsondata["results"][0]["my_estimate_league_point"])+ '我方'+ str(jsondata["results"][0]["estimate_gachi_power"]) + '对面' + str(jsondata["results"][0]["other_estimate_league_point"]) 
            elif jsondata["results"][0]["type"] == "gachi":
                if "estimate_x_power" in jsondata["results"][0]:
                    x_power = ''
                    if jsondata["results"][0]["x_power"] == None:
                        x_power = "等待定分"
                    else: 
                        x_power = str(jsondata["results"][0]["x_power"])
                    league_data = 'X power:'+ x_power + '   推定' + str(jsondata["results"][0]["estimate_x_power"])

                elif jsondata["results"][0]["udemae"]["name"] != "X":
                    udemae = jsondata["results"][0]["udemae"]["name"]
                    league_data = udemae + '   推定' + str(jsondata["results"][0]["estimate_gachi_power"])
            elif jsondata["results"][0]["type"] == "regular":
                league_data = ''
            else:
                league_data = ''
            f.write(res+'\n'+league_data)
 #           f.write(str(jsondata["results"][0]))
            return winlose, res, league_data
    else:
        print("无cookie或cookie过期，重新获取cookie中")
        iksm.save_cookie()
        print("成功更新cookie，让我先休息30秒")
        print("zzZZZZZZ")
        sleep(30)
        return 'waiting   ', 'waiting for updating', ''


