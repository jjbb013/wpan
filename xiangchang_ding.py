#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import time
import random
import requests
import json
import re
from dingtalkchatbot.chatbot import DingtalkChatbot

webhook_all = {
    '上海': 'https://oapi.dingtalk.com/robot/send?access_token=e3236ba265e3ef4bf68af0e9c50663080c445dc11943ec731fda94089f551213',
    '浙江': 'https://oapi.dingtalk.com/robot/send?access_token=fd41231b0787ad99a1167c3e463a15a9998e1f44c74949217e6d3cabff88b797',
    '广东': 'https://oapi.dingtalk.com/robot/send?access_token=de8582eb47bdeb3e33c61882d30d72bbef456847bbb4ef2a9400423b607c3b70',
    '重庆': 'https://oapi.dingtalk.com/robot/send?access_token=a8f81b3bd2f3779370a84da66c09dcabddaf28d2d3dced6205669a3b4679c105',
    '黑龙江': 'https://oapi.dingtalk.com/robot/send?access_token=f8803b3976f32bcce802d8f0d07e73e9c09c7330f58e7f5eafea0048d6245bcd',
    '宁夏': 'https://oapi.dingtalk.com/robot/send?access_token=69ae955cde4a067858f1e3089ce2e44ab15a833009fe8386a636c67a06533099',
    '湖南':'https://oapi.dingtalk.com/robot/send?access_token=819d72c360bc73c988425c75b1e5c2a874f443ffa263ad40b2cdfeb89b0e5da6',
    '贵州':'https://oapi.dingtalk.com/robot/send?access_token=1d7db4130f74c1b273e6989f8ed5fbf12e6e66bc38011a114275f169b4fdc185',
    '青海':'https://oapi.dingtalk.com/robot/send?access_token=89e5a81ff727c5f4215d7239243cf61524f12e366112fae90a39f9f69995325c',
    '北京':'https://oapi.dingtalk.com/robot/send?access_token=ef478e0691c2b8acf1ef4d428db9f4ed140c2f1390c6def59654ae39352a5ea1',
    '天津':'https://oapi.dingtalk.com/robot/send?access_token=ad4b1bc9c93868889ac17f09dae7dba2fb77c81e3dd5ad9de14c51d2e9ca00a9',
    '广西':'https://oapi.dingtalk.com/robot/send?access_token=53728b055a1c43d2aac836754c1b5ba64263760a22df87fb7844e9e91e81f48e',
    '辽宁':'https://oapi.dingtalk.com/robot/send?access_token=d4db4009a9bc857bbb3fe93a7445bdbe44faf18a0e948815c39df0d50fa236b6',
    '山东':'https://oapi.dingtalk.com/robot/send?access_token=d1927bef9ad3186b351e6e1b947d281f86ee7f37ecdb70838d13ad182f1300b8',
    '山西':'https://oapi.dingtalk.com/robot/send?access_token=0fe4bba2a5a5c149c244075f982fa1218b958b15357984744484d28c3252e795',
    '陕西':'https://oapi.dingtalk.com/robot/send?access_token=2f375d62dac8179bb774517e511b51865c637bab545d7a9999b3c75c435f6eec',
    '新疆':'https://oapi.dingtalk.com/robot/send?access_token=4d2f1c3094a43a3c067b42bd8ba668d8e0acd7e38b0dbeff582c2886d0280685',
    '福建':'https://oapi.dingtalk.com/robot/send?access_token=3c074fe50103d0d5ac006f4092998e3edb28b056a57e9e12ba7ba8532f3dec5d',
    '河北':'https://oapi.dingtalk.com/robot/send?access_token=e7b77ae52b61811af541ba3e184af2bbb45ef6ccbeda975eddb04e1f12696056',
    '河南':'https://oapi.dingtalk.com/robot/send?access_token=747688fc75fd63224804cf3a0007d7b95dda652fb9d0e3a1036d8194f9591775',
    '湖北':'https://oapi.dingtalk.com/robot/send?access_token=9c3d1e6e2791a8a00e116bd440f8a0e69d6ded74deb2d7765e7a1230bb2a116e',
    '四川':'https://oapi.dingtalk.com/robot/send?access_token=5d4dee98cd8c90e3d766a7acde2dcc8a3128e5af1becf6b9830728811302a2b2',
    '安徽':'https://oapi.dingtalk.com/robot/send?access_token=c4451ee195a540eae384e2f43cb3e778cc775a9f5dbfadad172356470ac305e5',
    '江西':'https://oapi.dingtalk.com/robot/send?access_token=19d4b3c52859a4528ac3738d9fa022903530b7c402369a29dc2a708ff97459d0',
    '海南':'https://oapi.dingtalk.com/robot/send?access_token=a0754cc0433514596b9017b2c3cd98900d7480b2931ef17ab1183b93fc7c253d',
    '内蒙古':'https://oapi.dingtalk.com/robot/send?access_token=6b3badb331f25fb03f0da1b8a3c43bb516a4d0e3d6b32dfe3c7f1ec266ca83d2',
    '西藏':'https://oapi.dingtalk.com/robot/send?access_token=46ef6b149ceffc22ae17d90729024dd6b06f82c3bc2a8cc46ed6a1bfd1c31903',
    '江苏':'https://oapi.dingtalk.com/robot/send?access_token=51a226f8e35e2a89aa06723de6d108ba31565a57f2f42fa6c35385ae987da86b',
    '吉林':'https://oapi.dingtalk.com/robot/send?access_token=e6b9560fdcb1b6b2af194251ca6c6b9c5568c2499fcfe3f8a81c67487d923d6e',
    '甘肃':'https://oapi.dingtalk.com/robot/send?access_token=b4fb75c3935ccb1bbd21d504033a0e93eec79aef68db7577828ed5ca1363f8d1',
    '遵义':'https://oapi.dingtalk.com/robot/send?access_token=1d7db4130f74c1b273e6989f8ed5fbf12e6e66bc38011a114275f169b4fdc185',
    '仁怀':'https://oapi.dingtalk.com/robot/send?access_token=1d7db4130f74c1b273e6989f8ed5fbf12e6e66bc38011a114275f169b4fdc185',
    '解放碑':'https://oapi.dingtalk.com/robot/send?access_token=a8f81b3bd2f3779370a84da66c09dcabddaf28d2d3dced6205669a3b4679c105',
}

def get_last_len():
    with open("/usr/will/ListLen.txt", "r") as file:
        file = int(file.read())
    return file

def send_message(message, webhook):

    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook, secret="自营店")  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

    # Text消息@所有人
    xiaoding.send_text(msg=message, is_at_all=False)
def pushToWechat(messageqq):
    wxpushurl = 'http://www.pushplus.plus/send?'
    wxbody = {
        "token":"9c28de81ba3446058e78c659b9891a98",
        "title":"自营店预约通知",
        "content":messageqq + '微信:will_pan_world',
        "topic":"MaoTai",
        "template":"markdown",
        "timestamp":""
    }
    a = requests.post(url=wxpushurl,json=wxbody)
    print(a.json())

if __name__ == '__main__':

    # 自营店服务器地址
    url_chat = ["http://fen_bu_chat_face_3.xiangchangshu.com/chat-face/message/getPrivateMessage",
                "http://fen_bu_chat_face_5.xiangchangshu.com/chat-face/message/getPrivateMessage",
                "http://fen_bu_chat_face_2.xiangchangshu.com/chat-face/message/getPrivateMessage",
                "http://fen_bu_chat_face_4.xiangchangshu.com/chat-face/message/getPrivateMessage"]
    # 自营店请求头(这个Token是15510976080的
    headers_1 = {'token': '73341a15f218f52d8271d7c21d6cea13', }
    # 自营店请求Body
    body = [{"messageId": "1"}, {"messageId": "22"}, {"messageId": "333"}, {"messageId": "4444"},
            {"messageId": "55555"}]
    # 请求所有返回数据
    text = requests.post(url=random.choice(url_chat), json=random.choice(body), headers=headers_1)

    # 将获取到的文件转换为Json
    content = text.json()
    # 所有自营店通知的数量
    Len_of_zyd = len(content['data'])
    print("目前通知的数量为" + str(Len_of_zyd) + '次')

    # 获取上次登记的数量
    last_len = get_last_len()
    print('上次通知的数量为' + str(last_len) + '次')
    messageGroup = []
    for i in range(last_len, Len_of_zyd):

        # 显示最后一个自营店通知，从Json中找到Key data列表 下的第n个字典 下的content字符串
        result = str(content['data'][i]['content'])

        # 从字符串中找出自营店酒类信息
        if '自营店' in result:
            result1 = re.search(pattern='.+自营店.*\n.+\n.+\n.+', string=result, flags=re.M)
            result2 = re.search(pattern='.+自营店',string=result,flags=re.M)
            messageGroup.append(result2.group())
            for key in webhook_all:
                if key in result1.group():
                    webhook = webhook_all[key]
                    message = result1.group()+'\n'+'\n'+'注：'+'\n'+'未标注[全国]说明仅限当地身份证预约，非当地身份证无法看到预约列表'+'\n'+'\n'+'43度飞天茅台不建议预约（无利润）'+'\n'+'\n'+'有疑问请钉钉/微信私聊群主'+'***群内禁言***'
                    send_message(message=message, webhook=webhook)
                    print('\n' + result1.group() + '\n' + '已发送到钉钉')

                else:
                    pass
        else:
            pass
    webhookqq = 'https://oapi.dingtalk.com/robot/send?access_token=c825f71ca46e1fae9d3541db26b801548da2586bd2193c4821399b38f7eb2e37'
    messageqq = str(messageGroup)+'已开放预约'+'\n'+'注：'+'若希望仅收到部分省份通知请私聊群主'
    messageqq = messageqq.replace("\'","")
    send_message(message=messageqq, webhook=webhookqq)
    if '自营店' in messageqq:
        pushToWechat(messageqq)
    else:
        print('本次无更新推送')
    with open('/usr/will/ListLen.txt', 'w') as file:
        file = file.write(str(Len_of_zyd))
        print('已经保存文件并记录总数为' + str(Len_of_zyd) + '次')


