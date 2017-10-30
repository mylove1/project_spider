# coding:utf-8


import requests


headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

url = "http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"

data={
#"__VIEWSTATEGENERATOR":"DB1FBB6D",
#"cityName":"%E4%B8%8A%E6%B5%B7",
#"StartTime":"2017-10-27",
#"DepTime":"2017-10-28",
#"operationtype":"NEWHOTELORDER",
#"IsOnlyAirHotel":"F",
"cityId":"3",
#"cityPY":"shanghai",
#"cityCode":"021",
#"cityLat":"31.2363508011",
#"cityLng":"121.4802384079",
#"positionArea":"Location",


#"positionId":"116",
"page":"2",
}
response = requests.post(url=url,headers=headers,data=data)
html = response.content
print html
print len(html)
print response.url
