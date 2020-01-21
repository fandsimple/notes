# 爬虫进阶笔记

## js操作

- js执行库

  - execjs

    ```
    下图为execjs中js引擎的选择，我们选择node.js
    ```

    ![image-20200121110700270](/Users/fanding/gitProjects/notes/spider/img/image-20200121110700270.png)

  ![image-20200121113631436](/Users/fanding/gitProjects/notes/spider/img/image-20200121113631436.png)

![image-20200121113716159](/Users/fanding/gitProjects/notes/spider/img/image-20200121113716159.png)

[
{
    "domain": ".xiaoe-tech.com",
    "expirationDate": 1611129177.973164,
    "hostOnly": false,
    "httpOnly": true,
    "name": "cookie_channel",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "internaljump",
    "id": 1
},
{
    "domain": ".xiaoe-tech.com",
    "expirationDate": 1894953177.972998,
    "hostOnly": false,
    "httpOnly": true,
    "name": "XIAOEID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "afad437026e11513f675d2843e1c1715",
    "id": 2
},
{
    "domain": "apppit6dcs05916.pc.xiaoe-tech.com",
    "expirationDate": 1735113177.973208,
    "hostOnly": true,
    "httpOnly": true,
    "name": "anonymous_user_key",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "dV9hbm9ueW1vdXNfNWUyNmFkZDllNTVhNF9SYlBmQUFqTGRQ",
    "id": 3
},
{
    "domain": "apppit6dcs05916.pc.xiaoe-tech.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "app_id",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "\"appPit6DCs05916\"",
    "id": 4
},
{
    "domain": "apppit6dcs05916.pc.xiaoe-tech.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "dataUpJssdkCookie",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "{\"wxver\":\"\",\"net\":\"\",\"sid\":\"\"}",
    "id": 5
},
{
    "domain": "apppit6dcs05916.pc.xiaoe-tech.com",
    "expirationDate": 1579679993.384519,
    "hostOnly": true,
    "httpOnly": true,
    "name": "pc_user_key",
    "path": "/",
    "sameSite": "unspecified",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "20615cf367431ba6346b1b493da089f0",
    "id": 6
},
{
    "domain": "apppit6dcs05916.pc.xiaoe-tech.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "userInfo",
    "path": "/",
    "sameSite": "unspecified",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "{\"app_id\":\"appPit6DCs05916\",\"user_id\":\"u_5e1aa6fb6bd01_yhWgJjLpnR\",\"wx_name\":\"念恋\",\"wx_nickname\":\"念恋\",\"wx_avatar\":\"http://wechatavator-1252524126.file.myqcloud.com/appPit6DCs05916/image/compress/u_5e1aa6fb6bd01_yhWgJjLpnR.png\",\"wx_gender\":1,\"birth\":null,\"address\":null,\"job\":null,\"company\":null,\"wx_account\":\"\",\"phone\":\"15735183437\",\"pc_user_key\":\"20615cf367431ba6346b1b493da089f0\"}",
    "id": 7
}
]