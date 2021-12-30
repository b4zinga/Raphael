import requests


def run(host, **kwargs):
    url = host + "/apisix/admin/migrate/export"
    req = requests.get(url)
    if req.status_code == 200 and "\"Routes\"" in req.text:
        return True
