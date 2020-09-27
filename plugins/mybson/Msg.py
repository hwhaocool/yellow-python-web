#coding:utf-8

class Msg:
    def __init__(self):
        """构造方法"""
        pass


class Header:
    messageLength = 0
    requestID = 0
    responseTo = 0
    opCode = 0

    def __init__(self):
        """构造方法"""
        pass

    def __str__( self ):
        return "Header [messageLength=%d,  requestID=%d, responseTo=%d, opCode=%d]" % (self.messageLength, self.requestID, self.responseTo, self.opCode)

class OpQuery:
    header = Header()
    flags = 0
    fullCollectionName = ""
    numberToSkip = 0
    numberToReturn = 0

    query = None   #document
    returnFieldsSelector = None  #projection
