import re
import requests
import json

headers = {
    'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

pattern="vid=.*&"
baseurl="https://m.v.qq.com/play.html?vid=g00448n91zg&cid=mzc0020016b6v6q"
pageurl="https://dm.video.qq.com/barrage/base/{}"
dmurl="https://dm.video.qq.com/barrage/segment/{}/{}"
vid=re.findall(pattern,baseurl)[0][4:-1]
response=requests.get(url=pageurl.format(vid),headers=headers)
segment_list = json.loads(response.text)["segment_index"]
total_count=0
with open("{}.txt".format(vid), "a") as file:
    for segment_id in segment_list: 
        segment=segment_list[segment_id]
        print("正在爬取timestame{}的弹幕，已爬取共{}条弹幕".format(segment["segment_start"], total_count))
        response = requests.get(url=dmurl.format(vid, segment["segment_name"]),headers=headers)
        dm_list_json = json.loads(response.text)["barrage_list"]
        for dm in dm_list_json:
            file.write(dm["content"]+"\n")
            total_count+=1