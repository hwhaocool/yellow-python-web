#coding:utf-8

from flask import Flask, render_template, url_for, render_template_string, request
import sys, os
import re
import json

from plugins.logType.LogType import LogType
from plugins.swagger.Protobuf2Swagger import ToolP2S
from plugins.wiki.wiki import ToolWiki
from plugins.mybson.MyBson import MyBson

app = Flask(__name__)

def getLog(type="b"):
    log = LogType()
    return log.getFileContent(type)

@app.route('/')
def root():
    return index()

@app.route('/index')
def index():
    return """
    If you want see LogType, please visit /b or /c
    or
    /p2s  --->  protobuf to swagger
    /wiki --->  wiki helper
    """

@app.route('/b')
def b():
    return getLog("b")

@app.route('/c')
def c():
    return getLog("c")

@app.route('/p2s')
def p2s():
    """protobuf to swagger"""
    tool = ToolP2S()
    return tool.index()

@app.route('/p2s/convert', methods=["PUT"])
def p2sConvert():
    """protobuf to swagger"""
    a = request.get_data()

    tool = ToolP2S()
    return tool.convert(a)

@app.route('/bson')
def bson():
    """protobuf to swagger"""
    tool = MyBson()
    return tool.index()

@app.route('/bson/convert', methods=["PUT"])
def bsonConvert():
    """protobuf to swagger"""
    a = request.get_data()

    tool = MyBson()
    return tool.convert(a)

@app.route('/wiki')
def wikiIndex():
    """generate interface wiki"""
    tool = ToolWiki()
    return tool.index()

@app.route('/wiki/convert', methods=["PUT"])
def wikiConvert():
    """convert form data to interface wiki"""
    a = request.get_data()

    tool = ToolWiki()
    return tool.convert(a)

if __name__ == '__main__':
    app.debug = True
    #监听 所有ip
    app.run(host='0.0.0.0', port=8083)