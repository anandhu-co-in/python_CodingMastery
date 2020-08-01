
class HashTable:
    def __init__(self,len=50):
        self.keymap=[None]*len
        self.length=len

    def hash(self,key,):
        total = 0
        primeNumber = 31
        for i in range(0, min(len(key), 100)):
            char = key[i]
            total = (total * primeNumber + ord(char) - 96) % self.length
        return total


    def set(self,key,value):
        index= self.hash(key)
        if self.keymap[index]==None :
            print("Index {} is now empty".format(index))
            self.keymap[index]=[]
        print("Setting new data at in index {}".format(index))
        self.keymap[index].append([key,value])

    def get(self,key):
        index=self.hash(key)
        if self.keymap[index]!=None:
            for i in range(0, len(self.keymap[index])):
                if self.keymap[index][i][0]== key:
                    print("Found {} at position {}.{} with data {}".format(key,index,i,self.keymap[index][i][1]))
                    return

        print("Key {} is not Found".format(key))



myHashTable=HashTable(5)

myHashTable.set("key1","q")
myHashTable.set("key2","q")
myHashTable.set("key3","b")
myHashTable.set("key4","c")
myHashTable.set("key5","d")
myHashTable.set("key6","e")

print(myHashTable.keymap)




#Complexity for insertion, deletion, access O(1), WITH WORST CASE HAS FUNCTION O(N)






# BELOW ALGO TO GET LIST OF UNIQUE KEYS, And unique values
#
# keys()
# {
#     let
# keysArr = [];
# for (let i = 0; i < this.keyMap.length; i++)
# {
# if (this.keyMap[i])
# {
# for (let j = 0; j < this.keyMap[i].length; j++){
# if (!keysArr.includes(this.keyMap[i][j][0])){
# keysArr.push(this.keyMap[i][j][0])
# }
# }
# }
# }
# return keysArr;
# }
# values()
# {
# let
# valuesArr = [];
# for (let i = 0; i < this.keyMap.length; i++){
# if (this.keyMap[i]){
# for (let j = 0; j < this.keyMap[i].length; j++){
# if (!valuesArr.includes(this.keyMap[i][j][1])){
# valuesArr.push(this.keyMap[i][j][1])
# }
# }
# }
# }
# return valuesArr;
# }












