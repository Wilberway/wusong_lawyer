
import random

url_gdsf = "http://wsbs.gdsf.gov.cn/front/search.ered?reqCode=lawyerDetail&lawyerid=%s"

def read_proxies(path):
    lines = open(path)
    ips = lines.readlines()
    for ip in ips:
        yield ip.strip()

def get_proxies_id():
    proxies = [i for i in read_proxies('./tools/proxies.txt')]
    thisip = random.choice(proxies)
    print("proxie ip:" + thisip)
    if thisip[0:5] == 'https':
        return {"https": thisip}
    else:
       return {"http": thisip}
