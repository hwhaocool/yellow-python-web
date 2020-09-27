#coding:utf-8

import re
import sys
import json
from flask import Flask, render_template, url_for, render_template_string
import urllib

from collections import OrderedDict

class ToolP2S:
    __input = []

    def __init__(self):
        """构造方法"""
        pass

    def index(self):
        return render_template("p2s.html", interfaceUrl="/p2s/convert")
        pass

    def convert(self, data):
      if data.startswith("data"):
        p = data[5:]

      new_data = urllib.unquote(p)

      self.__input = new_data.split("\n")
      pass
      return self.output()

    def input(self):
        """输入"""
        print(u"请输入多行，最后一行多按一下回车 即可结束输入")
        print(u"Please input multi lines, last line input q to end")

        stopword = "q"

        for line in iter(raw_input, stopword):
            key = line.decode(sys.stdin.encoding)
            self.__input.append(key)

        pass

    def output(self):
        """输出"""
        msg_pattern = re.compile("^message\s+([a-zA-Z0-9_]+)")

        field_regex = "\s+([a-zA-Z0-9_]+)\s*=\s*\d+\s*;\s*//(.+)"
        string_pattern = re.compile("^string" + field_regex)
        int32_pattern = re.compile("^int32" + field_regex)
        int64_pattern = re.compile("^int64" + field_regex)
        double_pattern = re.compile("^double" + field_regex)
        date_pattern = re.compile("^date" + field_regex)
        obj_pattern = re.compile("^([a-zA-Z0-9_]+)" + field_regex)
        list_obj_pattern = re.compile("^repeated\s+([a-zA-Z0-9_]+)" + field_regex)

        obj_list_json = OrderedDict()
        obj_json = OrderedDict()

        is_message_start = False
        message_name = ""
        message_description = ""

        for data in self.__input:
          data = data.strip()
          if not is_message_start and data.startswith("//"):
            message_description = data[2:]

          elif msg_pattern.match(data):
            message_name = msg_pattern.match(data).group(1)
            is_message_start = True
            obj_json["type"] = "object"
            obj_json["description"] = message_description
            obj_json["properties"] = OrderedDict()

          elif data.startswith("string") and string_pattern.match(data):
            #string
            m = string_pattern.match(data)
            field_name = m.group(1)
            field_desc = m.group(2)

            if not field_desc:
              field_desc = ""

            field_json = {
              "type": "string",
              "description" : field_desc
            }

            obj_json["properties"][field_name] = field_json

          elif data.startswith("int32") and int32_pattern.match(data):
            # integer
            m = int32_pattern.match(data)
            field_name = m.group(1)
            field_desc = m.group(2)

            if not field_desc:
              field_desc = ""

            field_json = {
              "type": "integer",
              "description" : field_desc
            }

            obj_json["properties"][field_name] = field_json

          elif data.startswith("int64") and int64_pattern.match(data):
            m = int64_pattern.match(data)
            field_name = m.group(1)
            field_desc = m.group(2)

            if not field_desc:
              field_desc = ""

            field_json = {
              "type": "integer",
              "format": "int64",
              "description" : field_desc
            }

            obj_json["properties"][field_name] = field_json

          elif data.startswith("double") and double_pattern.match(data):
            #double
            m = double_pattern.match(data)
            field_name = m.group(1)
            field_desc = m.group(2)

            if not field_desc:
              field_desc = ""

            field_json = {
              "type": "number",
              "format": "double",
              "description" : field_desc
            }

            obj_json["properties"][field_name] = field_json

          elif data.startswith("date") and date_pattern.match(data):
            # date
            m = date_pattern.match(data)
            field_name = m.group(1)
            field_desc = m.group(2)

            if not field_desc:
              field_desc = ""

            field_json = {
              "type": "string",
              "format": "date-time",
              "description" : field_desc
            }

            obj_json["properties"][field_name] = field_json

          elif data.startswith("repeated") and list_obj_pattern.match(data):
            # list<Object>
            m = list_obj_pattern.match(data)
            field_type = m.group(1)
            field_name = m.group(2)
            field_desc = m.group(3)

            if not field_desc:
              field_desc = ""

            field_json = OrderedDict()
            field_json["type"] = "array"
            field_json["description"] = field_desc

            if "string" == field_type:
              field_json["items"] = {
                "type": "string"
              }
            elif "int32" == field_type:
              field_json["items"] = {
                "type": "integer"
              }
            else:
              field_json["items"] = {
                "$ref": "#/definitions/" + field_type
              }

            obj_json["properties"][field_name] = field_json

          elif obj_pattern.match(data):
            # Object
            m = obj_pattern.match(data)
            field_type = m.group(1)
            field_name = m.group(2)
            field_desc = m.group(3)

            if not field_desc:
              field_desc = ""

            field_json = {
              "$ref": "#/definitions/" + field_type,
              "description" : field_desc
            }
            obj_json["properties"][field_name] = field_json

          elif data.startswith("}"):
            # one message end

            obj_list_json[message_name] = obj_json
            obj_json = OrderedDict()
        pass

        print("==========   result is      ==========")
        print obj_list_json
        result = json.dumps(obj_list_json, indent=4, ensure_ascii=False)
        return result

if __name__ == '__main__':
    print(
      u'''
********  工具介绍   *************
*    将 Protobuf 语句转成 swagger *
*    Convert Protobuf to swagger  *
*                                 *
*********************************
'''
    )

    s = ToolP2S()
    s.input()
    s.output()