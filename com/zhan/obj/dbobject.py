#encoding: utf-8

import requests
from requests import PreparedRequest as pr

url = "http://192.168.41.106:8093/coursemall/getcampaignlist"
r = requests.post(url,params={"ActivityId":1005,"CourseId":1005,"PassportId":"顶替","ConsultContent":"12312"}, verify=False)
print r.text
print r.status_code
print dir(r.request)