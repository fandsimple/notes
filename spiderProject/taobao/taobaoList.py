#!/usr/bin/python
# -*- coding: utf-8 -*-





'https://market.m.taobao.com/app/tb-source-app/shop-auction/pages/auction?_w&sellerId=394419907&shopId=61193233&disablePromotionTips=true&shop_navi=allitems&displayShopHeader=true'


'https://market.m.taobao.com/app/tb-source-app/shop-auction/pages/auction?shopId=61193233'



import requests

headers = {
    'authority': 'h5api.m.taobao.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'referer': 'https://h5.m.taobao.com/awp/core/detail.htm?id=6760338930&spm=a2141.7631671.content.2',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '_m_h5_tk=6d79c6dc0bc63e33d4184f5fbb6649a0_1580278908851; _m_h5_tk_enc=7936ab85c1a9c9162330d6519780fd28; cna=9PS3FltrhVICAXSzsT9f3DGu; _samesite_flag_=true; cookie2=1875d4c74bf8b725ff4b6c95cf274cda; t=b5587e3b9447d35f3f692ad600288ada; _tb_token_=3ee8ddef7375a; l=cBjQ9VuIQSzOH4Q_BOCwlurza77O_IRxluPzaNbMi_5Iy6T69__OoqguzF96DjWd97TB4fQqfZv9-etXw2ZBAwlvPIr1.; isg=BMLCuU4JKKyhFjTwOrIEFQb4E84kk8atd49IQQzb7jXgX2LZ9CMWvUieCl0jfD5F',
}

params = (
    ('jsv', '2.5.7'),
    # ('appKey', '12574478'),
    ('t', '1580271890029'),
    # ('sign', '3f867c4ebb3855bb006693a7ca9f98ec'),
    ('api', 'mtop.taobao.detail.getdetail'),
    ('v', '6.0'),
    ('isSec', '0'),
    ('ecode', '0'),
    ('AntiFlood', 'true'),
    ('AntiCreep', 'true'),
    ('H5Request', 'true'),
    ('ttid', '2018@taobao_h5_9.9.9'),
    ('type', 'jsonp'),
    ('dataType', 'jsonp'),
    ('callback', 'mtopjsonp1'),
    ('data', '{"id":"6760338930","spm":"a2141.7631671.content.2","itemNumId":"6760338930","itemId":"6760338930","exParams":"{\\"id\\":\\"6760338930\\",\\"spm\\":\\"a2141.7631671.content.2\\"}","detail_v":"8.0.0","utdid":"1"}'),
)

response = requests.get('https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/', headers=headers, params=params)
print(response.text)
