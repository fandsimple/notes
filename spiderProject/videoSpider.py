#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import subprocess
import logging



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
        'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/37a1f8425285890797904684558/drm/voddrm.token.MjYwOGM4OWUxYTE2ZmQ1YjgxcDlmekdmWVlMQkZHMTBNNnFxMnR2VnFTSlB5WEpkRFdMR0svNUJnSGkrODBKaw.v.f230.m3u8': '第零篇--课程介绍',
        'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/ce74d1e15285890797584942358/drm/voddrm.token.MTQ2NTkwZjViZTk2NmZmOVhZc0tzSEY2TXE1Zmx6YXpjMWltSWEzUElZSVROa0xQWlBBYmNZQ0EzVTVwZ2U1Zg.v.f230.m3u8': '第一篇--追根究底——探寻JavaScript反爬虫的根本原因',
        'https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/3e7dc05e5285890797904965228/drm/voddrm.token.YmYwMWI5ZjlmODY1NWNmM3ZtK3JsUWIwQm8yTWh1dFpTZG02dS9Ma3lWbjFycXA4Ni9NeW1lMDJXRTNJRXRuag.v.f230.m3u8': '第二篇--浮沙之上——课程中⽤到的JavaScript语法和知识',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
        '': '',
    }



