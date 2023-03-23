from flask import Flask #載入 Flask
from flask import request #載入 requeast
from flask import redirect #載入 redirect
import json #載入json
# 建立application 物件,設定靜態檔案的路徑處理
app=Flask(
    __name__,
    static_folder="stickt",#靜態檔案的資料名稱
    static_url_path="/"#靜態檔案對應的網路路徑
)

@app.route("/zh-tw/")
def index_chinese_Taiwan():
    return json.dumps({"language":"zh-tw","text":"您好 flask"},ensure_ascii =False)# 指示ascii編碼不處理中文

@app.route("/zh-ja/")
def index_Japan():
    return json.dumps({"language":"ja","text":"こんにちはフラスコ"},ensure_ascii =False) # 指示ascii編碼不處理日文

@app.route("/en-us/")
def index_English():
    return json.dumps({"language":"en-us","text":"Hello flask"})#回傳網站首頁的內容

#建立路徑 / 對應的處理函式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    lang = request.headers.get("accept-language")
    lang_priority = lang.split(",")[0]
    print(lang_priority) #輸出第一個語言偏好
    
    if lang_priority ==("ja"):
        return redirect("/zh-ja/")
    
    elif lang_priority ==("zh-TW"):
        return redirect("/zh-tw/")
    
    else :
        return redirect("/en-us/")
#建立路徑 /data 對應的處理函式
@app.route("/data")
def getData():
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referer"))
    return "Data Here"

#動態路由:建立路徑 /user/使用者名稱 對印的處理函式
@app.route("/user/<name>")
def getUser(name):
    if name == "108410013":
        return "Hello"+name+" 姓黃 名博裕"
    elif name == "趙彥銘":
        return "趙彥銘真高"
    else: return name+"名單內查無此人"

#建立路徑/getSum 對應的處理函式
# 利用要求字串(Query String) 提供彈性: /getSum?min=最小數值&max=最大數值    
@app.route("/getSum")
def getSum(): # min+(min+1)+(min+2)+(min+3)+max
    maxNumber=request.args.get("max", 100)
    maxNumber=int(maxNumber)
    minNumber=request.args.get("min",1)
    minNumber=int(minNumber)
    print("最小值 最大值",minNumber,maxNumber)
    #以下運算min+(min+1)+(min+2)+(min+3)+....+max 總和的迴圈邏輯
    result= 0
    for n in range (minNumber,maxNumber+1):
        result+=n
    return "最小值加總到最大值: "+str(result)

#啟動網站伺服器
app.run(port=777)

 