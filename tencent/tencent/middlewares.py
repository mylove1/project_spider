#!/usr/bin/env python
# -*- coding:utf-8 -*-

from settings import USER_AGENT_LIST
import random
import base64
class UserAgentMiddlewares(object):
    # 处理request的函数
    def process_request(self,request,spider):
        # 从USER_AGENT_LIST中随机选取一个
        user_agent = random.choice(USER_AGENT_LIST)
        # 将请求头设置为获取到的user_agent
        request.headers.setdefault("User-Agent",user_agent)


class ProxyMiddlewares(object):
    def process_request(self,request,spider):
        # 验证代理写法1
        # proxy = "616353084:j57da14r@43.226.164.60:16816"
        # request.meta["proxy"] = "http://" + proxy
        # 验证代理写法2
         user_psw = "616353084:j57da14r"
         base64_user_psw = base64.b64encode(user_psw)
         request.headers["proxy-Authorization"] = "Basic" + base64_user_psw
