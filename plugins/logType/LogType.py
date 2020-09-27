#coding:utf-8


import sys, os
import re
from MyMarkDown import MyMarkDown
from flask import Flask, render_template, url_for, render_template_string

class LogType:


    #public static enum LogType 的正则表达式
    __log_enum_pattern = re.compile("public\s+static\s+enum\s+LogType\s*{")
   
    
    def __init__(self):
        pass

    def getB(self):
        print("get b")
        return getFileContent("b")

    def getC(self):
        print("get c")
        return getFileContent("c")

    def getFileContent(self, log_type):
        if log_type == "b":
            file_path = "/home/jenkins/workspace/xxx/api/constant/Constants.java"
            type_name = "B"
        else:
            file_path = "/home/jenkins/workspace/xxx/constant/Constants.java"
            type_name = "C"

        c_file = open(file_path, 'r+')

        is_found = False

        my_mark_down = MyMarkDown()

        for data in c_file.readlines():
            data = data.decode("utf-8").strip()

            if not is_found:
                if data.startswith("public") and self.__log_enum_pattern.match(data):
                    is_found = True
                    my_mark_down.addLineByString(data)
            else:
                # print data
                if data.startswith("private"):
                    #end
                    break
                my_mark_down.addLineByString(data)

        c_file.close()

        return render_template("log.html", type=type_name, content=my_mark_down.getAll())

if __name__ == '__main__':
    pass