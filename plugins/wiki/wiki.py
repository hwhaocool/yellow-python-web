#coding:utf-8

from flask import Flask, render_template, url_for, render_template_string, request
import urllib
import markdown
import json
from collections import OrderedDict

class ToolWiki:
    __input = []

    __template = """|Type|CRUD|Value|Description|
|-|-|-|-|
|接口|`%s`|`%s`|%s|
|方法||`%s`||
|request body||%s||
|reponse body||%s||
"""

    __exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    def __init__(self):
        """构造方法"""
        pass

    def index(self):
        return render_template("wiki.html")
        pass

    def convert(self, ori_data):
      body_list = ori_data.split("&")
      print body_list

      interface = {}

      for data in body_list:
          if data.startswith("url"):
              url = data[4:]
              url = urllib.unquote(url)
              interface["url"] = url
          elif data.startswith("type"):
              in_type = data[5:]
              if in_type == "add":
                  interface["type"] = "新增"
              else:
                  interface["type"] = "更新"
          elif data.startswith("desc"):
              desc =  data[5:]
              interface["desc"] = urllib.unquote(desc)
          elif data.startswith("method"):
              interface["method"] = data[7:]
          elif data.startswith("request"):
              interface["request"] = data[8:]
          elif data.startswith("reponse"):
              interface["reponse"] = data[8:]

      return self.output(interface)

    def output(self, data):
        """输出"""
        result = OrderedDict()
        result["data"] = self.__template % ( \
            data.get("type", "error"), \
            data.get("url", "error"), \
            data.get("desc", "error"), \
            data.get("method", "error"), \
            data.get("request", "error"), \
            data.get("reponse", "error")
        )
        return json.dumps(result, indent=4, ensure_ascii=False)