import requests
import os
import json


# 1.拿到网页全部数据
# 2.转换成可解析的格式
# 3.找到对应的信息下载存储 ??没下载
# 4.与模板信息合并
# 5.成功后利用url的变量名变化规则通过输入拿到全部城市地铁的信息

url = 'http://map.amap.com/service/subway?_1536627018129&srhdata=1100_drw_beijing.json'
url_1 = 'https://api.zmis.me/v1/crh/line.generate'

def get_data(url):
    data = requests.get(url)    #获取url界面的信息
    return data.json()     #将文本信息变成字典

#转换成需要成的格式
def cut_positon(str):
    position = []
    longtitude = ""
    latitude = ""
    judge = 0
    for i in str:
        if i!=',' and judge == 0:
            longtitude += i
        else:
            judge = 1
        if judge == 1 and i != ',':
            latitude += i
    position.append(longtitude)
    position.append(latitude)
    return position


def input_station(station_list):
    station = []
    station_id = 0
    for item in station_list:
        station.append({
            "id": station_id,
            "station_name":item["n"],
            "longtitude": cut_positon(item["sl"])[0],
            "latitude":cut_positon(item["sl"])[1],
            "type": 0, #无法获取该信息
            "directive": 0 #无法获取该信息
        })
        station_id += 1
    return station


def deal_data(data):
    data_done = {}
    data_done["resize"] = 1
    data_done["circle"] = {"radis": 4,
                           "color": "#000",
                           "border_width": 6}
    data_done["list"] = []
    line_id = 0
    for item in data["l"]:     #需要 线路ID、名称  分支？   站点ID，名称，经纬度第几个分支 是否弯曲
        data_done["list"].append({
                                    "train_id":line_id, #依次递增
                                    "train_name":item["kn"],
                                    "type": 1,
                                    "max_group": 0,#未获取到，默认为0 无法获取该信息
                                    "color": "#FF7F00",
                                    "width": 8,
                                    "station":input_station(item["st"])
        })
        line_id += 1
    return data_done
#发送
r = requests.post(url_1,json=deal_data(get_data(url)))

#本地核验
print(r.json())




