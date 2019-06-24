import pymongo

#Connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["studentdB"]
mycol = mydb["studentInfo"]

#backend

def addStdRec(StdID, FirstName, SurName, DoB, Age, Gender, Address, Mobile):
    mydict ={"_id":StdID,"FirstName":FirstName,"SurName":SurName,"DoB":DoB,"Age":Age,"Gender":Gender,"Address":Address,"Mobile":Mobile}
    x = mycol.insert_one(mydict)
    

def viewData():
    
    x = mycol.find()
    return x

def deleteRec(StdID):
    mycol.remove({"_id":StdID})
    
    
def dataUpdate(StdID, FirstName="", SurName="", DoB="",Age="",Gender="",Address="",Mobile=""):
     query={"_id":StdID}
     if(len(StdID)!=0):
         newvalues ={"$set":{"StdID":StdID,"FirstName":FirstName,"SurName":SurName,"DoB":DoB,"Age":Age,"Gender":Gender,"Address":Address,"Mobile":Mobile}}
         mycol.update(query,newvalues)
     
def searchData(StdID):
    x = mycol.find({"_id":StdID})
    return x

    



















