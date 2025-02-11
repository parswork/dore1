from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017", serverSelectionTimeoutMS=5000)
class mongoDb():
    def __init__(self) -> None:
        self.mydb = client["database"]
        self.coll = self.mydb['dataext']

    #-----------------list_user
    #list_data
    # id:lit_user_1997
    #list_user: []
    def configData(self,data):
        data1= {
                    "_id": data[0], 
                    "list_user": "{}".format(data[1]), 
                  
                }
        return data1
    #----------- user
    #----------id:userid
    #----------username:username
    #----------phonenumber:phonenumber
    #----------rt:rtahsili
    #----------email:email
    #---------arr:arr
    
    def configData1(self,data):
        data1= {
                    "_id": int(data[0]), 
                    "username": "{}".format(data[1]), 
                    "phonenumber":"{}".format(data[2]), 
                    "rt": "{}".format(data[3]),
                    "email": "{}".format(data[4]),
                    "arr": "{}".format(data[5]),
                    
                    
                  
                }
        
           
        return data1
   
    def saveData(self,data):
        
        try:
             self.coll.insert_many(data)
             return True
             
        except:
            return False
    def readInformation(self,item_search,item):
          if item_search=="_id":
             model=self.coll.find_one({"{}".format(item_search): int(item)})
          else:
                model=self.coll.find_one({"{}".format(item_search): "{}".format(item)})
         
          if model==None:
              return False
          return model
    def readInformation1(self,item_search,item):
          if item_search=="_id":
             model=self.coll.find_one({"{}".format(item_search): item})
          else:
                model=self.coll.find_one({"{}".format(item_search): "{}".format(item)})
         
          if model==None:
              return False
          return model
    def search(self,item,key):
        information=[]
        for doc1 in self.coll.find({"{}".format(item):"{}".format(key)}):
            information.append(doc1)
        return information
    def update(self,id,item,key):
        model=self.coll.update_one({"_id":"{}".format(id)},{"$set":{"{}".format(item):"{}".format(key)}})
        if model==None:
            return False
        return True
    def delete(self,id):
        model=self.coll.delete_one({"_id" : "{}".format(id)})
        if model==None:
            return False
        return True
    def getAllData(self):
        all_data = []
        for doc in self.coll.find():
            all_data.append(doc)
        return all_data


        