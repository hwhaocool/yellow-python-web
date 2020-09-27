#coding:utf-8

import struct
from flask import Flask, render_template, url_for, render_template_string
from Msg import Msg, Header

import bson
from bson.codec_options import CodecOptions


class MyBson:
    def __init__(self):
        """构造方法"""
        pass

    def index(self):
        return render_template("p2s.html", interfaceUrl="/bson/convert")
        pass

    def convert(self, data):
        if data.startswith("data"):
            p = data[5:]
            print p

        #header 12字节，24 字符串
        if len(p) < 24:
            return "error, length is invalid"

        headerByteStrList = p[:32]

        header = Header()
        header.messageLength = self.getInt(headerByteStrList[:8])
        header.requestID = self.getInt(headerByteStrList[8:16])
        header.responseTo = self.getInt(headerByteStrList[16:24])
        header.opCode = self.getInt(headerByteStrList[24:])

        print "header is %s" % str(header)

        x1 = bson.BSON.encode({'a': 1}).capitalize()

        print str(x1)
        print type(x1)

        data = bson.BSON.encode({'type': 1})
        decoded_doc = bson.BSON.decode(data)
        bson.BSON.l



        print str(decoded_doc)
        print type(decoded_doc)

        options = CodecOptions(document_class=collections.OrderedDict)
        decoded_doc = bson.BSON.decode(data, codec_options=options)
        print type(decoded_doc)




    #   new_data = urllib.unquote(p)

    #   self.__input = new_data.split("\n")
      #pass
    #   return self.output()
      #return "hello"

    def getInt(self, string):
        b1 = string[:2]
        b2 = string[2:4]
        b3 = string[4:6]
        b4 = string[6:8]

        #小端
        num =  int(b1, 16)  + (int(b2, 16) << 8) + (int(b3, 16) << 16) + (int(b4, 16) << 24)
        return num


        
if __name__ == '__main__':
    print(
      u'''
********  工具介绍   *************
*    将 字符串形式的 字节 语句转成 bson *
*    Convert byte str list to swagger  *
*                                 *
*********************************
'''
    )

    s = MyBson()
    code = "data:880000001e03000000000000d40700000000000061646d696e2e24636d640000000000ffffffff61000000107361736c53746172740001000000026d656368616e69736d000c000000534352414d2d5348412d3100057061796c6f61640024000000006e2c2c6e3d726f6f742c723d236c7144304f4232356a2435717a337b524e365573603b5c00"
    
    code2="F802000004686F737473003900000002300013000000382E3132392E3135302E3231363A333731370002310013000000382E3132392E3135302E3231373A333731370000027365744E616D65000F0000006D677365742D3239353932393133001073657456657273696F6E00010000000869736D61737465720001087365636F6E646172790000027072696D6172790013000000382E3132392E3135302E3231363A3337313700026D650013000000382E3132392E3135302E3231363A333731370007656C656374696F6E4964007FFFFFFF0000000000000005036C61737457726974650087000000036F7054696D65001C000000117473000D000000C3901A5F127400050000000000000000096C61737457726974654461746500B879C57F73010000036D616A6F726974794F7054696D65001C000000117473000D000000C3901A5F127400050000000000000000096D616A6F7269747957726974654461746500B879C57F7301000000106D617842736F6E4F626A65637453697A650000000001106D61784D65737361676553697A65427974657300006CDC02106D61785772697465426174636853697A6500A0860100096C6F63616C54696D65007F7CC57F73010000106C6F676963616C53657373696F6E54696D656F75744D696E75746573001E00000010636F6E6E656374696F6E496400A7540A00106D696E5769726556657273696F6E0000000000106D61785769726556657273696F6E000800000008726561644F6E6C790000047361736C537570706F727465644D65636873002D0000000230000E000000534352414D2D5348412D323536000231000C000000534352414D2D5348412D310000016F6B00000000000000F03F0324636C757374657254696D65005800000011636C757374657254696D65000D000000C3901A5F037369676E61747572650033000000056861736800140000000019DBC28ADE9DEAC95F1FAB408E5DA13872793AAB126B6579496400ED010000514DE35E0000116F7065726174696F6E54696D65000D000000C3901A5F00"
    s.convert(code2)