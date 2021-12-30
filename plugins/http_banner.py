import re
import requests


def request_info(url):

    req = requests.get(url)

    charset = re.findall("charset=[\"\']?(.*?)[\"\']?[\"\>\'\s]", req.text, re.IGNORECASE)
    if not charset:
        if 'Content-Type' in req.headers:
            charset = re.findall("charset=(.*)", req.headers["Content-Type"])
    if charset:
        charset = charset[0]
    else:
        # charset = chardet.detect(req.content)['encoding']
        charset = "utf-8"

    body = req.content.decode(charset, errors="replace")
    status_code = str(req.status_code) or ""
    server = req.headers["Server"] if "Server" in req.headers else ""
    title = re.findall("<title[\s\S]*?>([\s\S]*?)</title>", body, re.IGNORECASE)
    if title:
        title = title[0]
    elif "X-Powered-By" in req.headers:
        title = req.headers["X-Powered-By"]
    else:
        title = ""

    return status_code + " | " + server + " | " + title


def run(host, **kwargs):
    info = request_info(host)
    return info
