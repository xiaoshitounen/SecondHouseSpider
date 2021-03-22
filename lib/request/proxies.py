def create_proxies():
    # 隧道域名:端口号
    tunnel = "tps179.kdlapi.com:15818"

    # 用户名密码方式
    username = "t11502028379856"
    password = "slyjwdtu"

    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }

    return proxies