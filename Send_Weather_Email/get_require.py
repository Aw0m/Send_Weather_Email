import requests
import json
"""
属性

Response.status_code	检查请求是否成功	     200 代表正常，404 代表网页不存在。
Response.encoding	    定义编码	            如果编码不对，网页就会乱码的。
Response.content	    把数据转成二进制	     用于获取图片、音频类的数据。
Response.text	        把数据转为字符串	     用于获取文本、网页原代码类的数据。

"""

def get_require():

    URL = "https://devapi.heweather.net/v7/weather/now?location=106.46,29.56&key=869c5f86e0704a5087554f4efd021ef6"         #* 浏览器的网页

    res = requests.get(URL)

    if res.status_code != 200:
        print("get url wrong -- ", res.status_code)
        return 0

    else:
        print("get url successfully!")

        res.encoding = "utf-8"
        temp_weather = json.loads(res.text)         # 获得字典形式
        
        fxLink = temp_weather["fxLink"]             # 该城市的天气预报和实况自适应网页

        now_weather = temp_weather["now"]

        temp = now_weather["temp"]                  # 实际温度（摄氏度）
        feel_temp = now_weather["feelsLike"]        # 体感温度（摄氏度）
        text = now_weather["text"]                  # 天气气象的描述 【如：阴】

        wind_scale = now_weather["windScale"]       # 风力大小

        humidity = now_weather["humidity"]          # 相对湿度
        precip = now_weather["precip"]              # 降水量

        rain = {0.1:"还没有雨呢", 10:"小雨", 25:"中雨", 50:"大雨", 100:"暴雨", 250:"大暴雨"}
        for x, y in rain.items():
            if float(precip) < x:
                temp_rain = y
                break
        else:
            temp_rain = "特大暴雨"

        return {"fxLink":fxLink, "temp":temp, "feel_temp":feel_temp, "text":text, "windScale":wind_scale, "humidity":humidity, "rain":temp_rain}

        