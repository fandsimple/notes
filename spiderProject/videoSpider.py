#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import subprocess
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s', level=logging.DEBUG)


def m3u8VideoSpider(url, fileName):
    '''
    :param url: m3u8文件网络地址
    :param fileName: 文件名
    :return:
    '''
    cmd = "ffmpeg -i %s -c copy %s.mp4" % (url, fileName)
    (cmdStatus, output) = subprocess.getstatusoutput(cmd)
    if cmdStatus:
        logging.warning('url:%s  fileName:%s 下载失败' % (url, fileName))
        return
    logging.info('url:%s  fileName:%s 下载成功' % (url, fileName))


def downloadVideo(downloadInfoMap):
    '''
    :param downloadInfoMap: 字典：{'网络m3u8地址':'fileName'}
    '''
    threadList = []
    for url, fileName in downloadInfoMap.items():
        threadList.append(threading.Thread(target=m3u8VideoSpider, args=(url, fileName)))
    for threadSingle in threadList:
        threadSingle.start()
    for threadSingle in threadList:
        threadSingle.join()
    logging.info('下载完成！！！！')


if __name__ == '__main__':
    downloadInfoMap = {
        'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/37a1f8425285890797904684558/drm/voddrm.token.MjYwOGM4OWUxYTE2ZmQ1YjgxcDlmekdmWVlMQkZHMTBNNnFxMnR2VnFTSlB5WEpkRFdMR0svNUJnSGkrODBKaw.v.f230.m3u8': '第零篇--课程介绍哈哈',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/ce74d1e15285890797584942358/drm/voddrm.token.MTQ2NTkwZjViZTk2NmZmOVhZc0tzSEY2TXE1Zmx6YXpjMWltSWEzUElZSVROa0xQWlBBYmNZQ0EzVTVwZ2U1Zg.v.f230.m3u8': '第一篇--追根究底——探寻JavaScript反爬虫的根本原因',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/3e7dc05e5285890797904965228/drm/voddrm.token.YmYwMWI5ZjlmODY1NWNmM3ZtK3JsUWIwQm8yTWh1dFpTZG02dS9Ma3lWbjFycXA4Ni9NeW1lMDJXRTNJRXRuag.v.f230.m3u8': '第二篇--浮沙之上——课程中⽤到的JavaScript语法和知识',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/761e12535285890797905013790/drm/voddrm.token.YWRhNjgxN2U2MmRkZDAxMjNZVG9xMzhoNEtsMGVIMmpsTFJKZ2Z5VmlZZ0V4MGdnZFFLY0JBeDdwcHI4eEZsLw.v.f230.m3u8': '第三篇--奇⻔遁甲——调用JavaScript执行代码[上]',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/3eb1f21f5285890797904991842/drm/voddrm.token.MzcxNGNmNDhhZmZjN2U4MHFDNlhVbjBWYUtPVmUyQk44bUVUWEJ3bi9ITlJWeHFXbWpCSUE3WndEQXR6NEZZcg.v.f230.m3u8': '第三篇--奇⻔遁甲——调用JavaScript执行代码[下]',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/8662b5775285890797905708027/drm/voddrm.token.ZTQwYTNiNTMxMGYwMGJlZEhxa0kvQnppWjhYR3pzay9jcm9RRnJBTTBMY0d3OFlqYVNtbGpQNTVLT0VWRFVxbg.v.f230.m3u8': '第四篇--蓄势待发——浏览器开发者⼯具的介绍和使⽤技巧【第一节】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/84776a5a5285890797905663219/drm/voddrm.token.Mjk0YTY0N2I3MWVkMzVkMVcwUyswOEdIcGlTcmd2WmM4U0U0cVFaQTRnSElWb0pTdGJidnplOEdhRWU5TEZwcQ.v.f230.m3u8': '第四篇--蓄势待发——浏览器开发者⼯具的介绍和使⽤技巧【第二节】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/8933f2215285890797905873934/drm/voddrm.token.Yzk3Zjk2ZjU4YmQwMmRmYnR5UVlPZzJnOWZJbWVvZ3dUdE5wOFZHK29SQWZtTmduUE1LUjFMb1JjaEg0TnlOSQ.v.f230.m3u8': '第四篇--蓄势待发——浏览器开发者⼯具的介绍和使⽤技巧【第三节】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/8b1d8fbd5285890797905915555/drm/voddrm.token.YWI0MjczMDUyMDYzYjZlZmxwckNFQ1hXc1FITGdmSklmYUdycjlEbmpvWmJUVTBuRnBMaDhla1BGTFI2aHVmNw.v.f230.m3u8': '第四篇--蓄势待发——浏览器开发者⼯具的介绍和使⽤技巧【第四节】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/8b790d3e5285890797905967018/drm/voddrm.token.MzRiMTgzMmI3MzYzZGUwMHpoNVpxS0NvUkZZNEtNMm4yNjB2UmQ2UTh0cTR1RFhkQlNOT2hGQVBVcktmYklReg.v.f230.m3u8': '第四篇--蓄势待发——浏览器开发者⼯具的介绍和使⽤技巧【总结】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/8b9d54655285890797905987581/drm/voddrm.token.Y2NlOGYwMmMxODA2NDA5Yzg0dXU4MHNUa0hab3NERWlTQm5CTjFyTDd5UUNYWnpUOHhwZGtQNDluWExobjdGRQ.v.f230.m3u8': '第五篇--磨⼑霍霍——常用⼯具的介绍和使⽤技巧【Charles】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/c34dff385285890797906042477/drm/voddrm.token.YzBhNTUxN2U0Yjk1NDBmOGx1Q2VIaWJtZnE0ajZ5Z3E3b0lHM21mREVWSmZoOERnOFZkdE5oQWhoaGRZVGV4SA.v.f230.m3u8': '第五篇--磨⼑霍霍——常用⼯具的介绍和使⽤技巧【EditThisCookie】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/c32d24de5285890797906028749/drm/voddrm.token.YmNjOGQxMjdiMDdmMmEyN3ZMd2xMTGxPSGZqdUlYTStHYWxxN1NSb3JxalhRNkFWMzUzMUkvbnBmWUlBeDFPUA.v.f230.m3u8': '第五篇--磨⼑霍霍——常用⼯具的介绍和使⽤技巧[Toggle_JavaScript]',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/c395d8515285890797906081512/drm/voddrm.token.ZGYwMWZjM2VlNmJkNjBhYW1CYzdzK0FvSWVVNmhFUXU0MHB3OGFmYXlIcGpqSVZwSy9sNTBjalZjL0ZYaGxrZw.v.f230.m3u8': '第五篇--磨⼑霍霍——常用⼯具的介绍和使⽤技巧【Tampermonkey】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/c7c3b3b25285890797906215604/drm/voddrm.token.MmQzNjllMThlYTU0NmVjMURYcmRhUWRKaHZxQmxacEVieE9NSmJ4Nm5tMm50TUdJdTJ1QmtsMmZLNUZXb2RMRg.v.f230.m3u8': '第六篇--初窥⻔径——阻挠爬⾍⼯程师的⽆限debugger[上]',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/c7f8d8975285890797906243374/drm/voddrm.token.MDlkNWE0ZjE5OGU4MzFjMlNERlVScm5lZ2lLZkplNElLZHlTMFJNRUMyODJGdzVCanBmZUN5UWtsTGpsSFNFag.v.f230.m3u8': '第六篇--初窥⻔径——阻挠爬⾍⼯程师的⽆限debugger[下]',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/c80dc7e15285890797906258927/drm/voddrm.token.M2ZlZjZiZGFjNTdjOWM3OER6c09TdGJvN0FHdmtldVRNSGpvYllIbjdoY2RRLzByS1Bsb2pPOHMwM0tLWEtPMg.v.f230.m3u8': '第七篇--⽕眼⾦睛——定位加密参数对应代码位置的⽅法',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/3ca204195285890797928323742/drm/voddrm.token.MTAyMWQwZGQ2MDExNmM0M1pJYUx2U05SamwrRlZYSmREODltc0N0alpWbk5XTEJGek4wYWNmd3JkSnBTS20wWg.v.f230.m3u8': '第八篇--拨开云雾——代码混淆的原理【上】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/3cfc76805285890797928373573/drm/voddrm.token.NTIyNDhkYTEyNjYzNjc2ZEpHSVpWSlBkWEdiQ2J3Myt5M3laTkJTNDRQeGJFQWdhT2doTkN6MndsME11dWpuMQ.v.f230.m3u8': '第八篇--拨开云雾——代码混淆的原理【下】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/92caf3f85285890797929700165/drm/voddrm.token.NmZiMDM1YmE4YTQ2YTMyZlE4ZTU2Y3krQnhhN0ZVcjg1amtVVnpJTCs2TTNzemRBYnFYT0xuS2xFcGV0OC9rMA.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【第一节】【推荐新手观看】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/92cca9be5285890797929703537/drm/voddrm.token.OTg2ZmIxMWMxNTkyMmIyNGhmZjNHRkVxdVorbW04aHFtc3hDUG5TV3VQcnRwa0cvb3Z3aGovN3FrSlJsZkpDSA.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【第二节】【样例一】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/930518255285890797929737249/drm/voddrm.token.ZTJiMjQ4YzVkMTdiNDc1NklRVDh3T0ZtL1h6RTVJQk1CRlAxb0RpM2haVHBRVkxWOUhIT2l1aFpWU3E4Ky9EdQ.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【第三节】【样例二】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/934e9c0e5285890797929779495/drm/voddrm.token.MTU4NzUzYTMxZDg2YzEwYjVMU3djZjZ2UmlUYWtBUVNWM3hzUEhRV0g1NVN0TCtHUUYzN0dtZE1jVEI1QWJmKw.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【第四节】【样例三】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/957a9a9c5285890797929850208/drm/voddrm.token.N2VlZTIwYTA0ZTJiNDBhM3BPZ1Zkem82RnYyYUE3OWo5M1UxTnh1RjBldkhtZC9Oc3RDWWVCZ1VacVVhN1hxbA.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【第五节】【样例四】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/978b34825285890797929917174/drm/voddrm.token.N2JmYWZjM2QxOTRlYjE1OVJyQTFieGRlVk83bmxnOTIraDAvanpFcllQejdURXlOYWhVK2xJWlR1dVkxWlMzeA.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【第六节】【样例五】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/98072a815285890797929982360/drm/voddrm.token.OTQ4MGI4OWI4NDcwOWI4MCtEQ2o4ZXN0NElHV1dTemJwSHhDTWxtb2JXTmtTclVtbm1Xbjd6ZzltUFczL1VSNA.v.f230.m3u8': '第九篇--⼀击即中——处理常见代码混淆操作的⽅法【总结】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/07305af65285890797931042783/drm/voddrm.token.NDUwZTg0ZTYwZDM2ZmE5NFFzZGl0bGJwTXBRbjJoc0hsUmNNNHlpUllxLyttNGJkcWtWWGNTNFNzckVJWEp2Vg.v.f230.m3u8': '第十篇--知⼰知彼——掌握常⻅的编码和加密',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/e8229f095285890797978957803/drm/voddrm.token.NWE5YjVkNGViYTA0N2VhY1pGVDJmRGtKY3VyYm1CUG1CSVBIV1pXUzlFWUwvRW9QeVU4dU9RT1A4aDMzSmpUeg.v.f230.m3u8': '第十二篇--⼀叶障⽬——服务端返回的神秘字符串',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/e830ddaa5285890797978960783/drm/voddrm.token.MWVlZmU2NzU3OWE2ZTk4MHgxRFFLMzFOTHFERUNIbkFJMUszSFRWREtvTTNHSFRmZDZ6ZjJ6VThVamlQaWs1bA.v.f230.m3u8': '第十三篇--螳臂当⻋——解密AES并不是每次都奏效【第一节】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/e80ec4cd5285890797978944199/drm/voddrm.token.ZjIwNWRkYTUwNGY3M2ViOEJBaUlWSEpxSEhTb0F2L1lYdmwzb3o0U3lZSWdYMnRwUkltWHpudWo1L21XOFVqSQ.v.f230.m3u8': '第十三篇--螳臂当⻋——解密AES并不是每次都奏效【第二节】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/e80ebf7b5285890797978944010/drm/voddrm.token.NmNmMWZkYjM1ZGM3ZjhmMVY1WWlBcUVvUThTZFZXT0JsMnZFa1pTT2wwMTZqME9nYm4zY2hYR2N4Qkc2eUZpcw.v.f230.m3u8': '第十三篇--螳臂当⻋——解密AES并不是每次都奏效【总结】',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/1ffa30805285890797979037516/drm/voddrm.token.MGVhNzM4YjkxOTY4M2Q4ZjNVVis0SnVjMG56YjVGNGxSZllyWTRkZlVKMnptVXVJOUp1b003MGpyT1NRWjZ2eQ.v.f230.m3u8': '第十四篇--插翅难逃——纵然CSS加身，也难逃命运的安排',
        # 'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/e856bc555285890797978983987/drm/voddrm.token.NGUzMzhiZDY2YWZjNzFiMjBwOGRPTHM0ejl3clpFL002bXVoMWdVS2F2aHJyUDFMVjJWcEdySHVoQk40NmJ3Yw.v.f230.m3u8': '第十五篇--真假猴王——Base64竟有如此威⼒',

    }
    # import base64
    # import json
    # downloadInfoStr = json.dumps(downloadInfoMap)
    #
    # encodeStr = base64.b64encode(downloadInfoStr.encode('utf-8'))
    # print(base64.b64decode(encodeStr))
    downloadVideo(downloadInfoMap)


