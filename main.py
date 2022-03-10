# coding:utf-8
import result
import time
from bottle import template
#path = "/www/wwwroot/82.157.137.92/splatoonresult/"
#path = "D:/Program_Python/webresult/"
path = ''
color = "color:#FF0000"
def generate(color ,player_result,league_data):
    template_demo = """
    <html>
    <style>
    .one{  
        line-height:30%;
    }
    </style>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <meta http-equiv="refresh" content="30" >
    </head>
    <body>
<br/>
<div style = line-height:100%>
    <div style="color:#ffffff">
        <h1>last match</h1>
    </div>


    <div style={{!color}}>
        <h1>{{ player_result }}</h1>
    </div>
</div>
<div style = line-height:85%>
    <div style={{!color}}>
        <h2>{{!league_data}}</h2>
    </div>
</div>
    </body
    </html>
    """

    html = template(template_demo, color= color, player_result = player_result, league_data=league_data)
    filename = path + "result.html"

    with open(filename, 'wb') as f:
        f.write(html.encode('utf-8'))
def main():
    generate()

def timer():
    for i in range(30, 0, -1):
        print("距离下次更新还有{}秒！\n".format(i), end="", flush=True)
        time.sleep(1)

if __name__ == '__main__':
    while True:
        winlose, player_result, league_data= result.Updateresult()
        if winlose == "win   ":
            color = "color:#FF0000"
        elif winlose == "lose   ":
            color = "color:#00FF00"
        else:
            color = "color:#FFFFFF"
        generate(color, player_result,league_data)
        timer()
    
