import time
import datetime
import json
from send_mail import send_mail
from get_require import get_require


if __name__ == "__main__":
    with open("information.json", 'r', encoding='UTF-8') as f:
        information = json.load(f)
        f.close()

    while True:
        cur_time = time.localtime(time.time())
        message_time = "现在的时间是 {:}年 {:}月{:}日 {:}:{:}\n\n".format(cur_time.tm_year, cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour, cur_time.tm_min)
        
        if cur_time.tm_hour == information["time"]["hour"] and cur_time.tm_min == information["time"]["min"]:   # 按读取的结果发送消息
        # if cur_time.tm_hour == 12 and cur_time.tm_min == 15:   # 默认 12:15 发消息
        # if (True):                    # 如果想要直接发送消息，注释上方的的if，此处的if不注释
            res = get_require()         # 调用天气API，取回当前天气信息
            
            message_weather = "\
        本次的天气预报到了哦~~\n\n\n \
            天气：{:}\n\n \
            实际温度：{:}℃； 体感温度：{:}℃\n\n \
            下雨情况：{:}； 相对湿度：{:}%；风力大小为：{:}级 \
                            \n\n\n".format(res["text"], res["temp"], res["feel_temp"], res["rain"], res["humidity"], res["windScale"])

            fxLink = res["fxLink"]
            time_now = "{:}月{:}日 {:}:{:}  ".format(cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour, cur_time.tm_min)
            message_total = message_weather + message_time + "可以进入 " + fxLink + " 网址，查看更详细的信息的哦~ \n\n" + time_now

            print(message_total)
            temp = {"subject":time_now + "的日常天气预报~", "main_message":message_total}
            send_mail(temp)      # 发送邮件
            time.sleep(75)





        
        print(message_time, '\n\n')
        time.sleep(20)

# @Author : Li Xiang
# @Address : liawom@foxmail.com