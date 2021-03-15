class Item:
    def __init__(self, itemName, aisle, steelLevel, locNumber):
        self.itemName = itemName
        self.aisle = aisle
        self.steelLevel = steelLevel
        self.locNumber = locNumber



class List:
    itemArray = []
    
    def addItem(self, item):
        self.itemArray.append(item)
    
    def deleteItem(self, index):
        self.itemArray.pop(index)
    
    #will find optimal path for forklift driver based off item locations and item destinations
    #will more than likely use breadth first search to do this
    def findShortestPath
    

item1 = Item("Coke", "3" , "4" , "7")
item2 = Item("Coke", "3" , "4" , "9")

myList = List()
myList.addItem(item1)
myList.addItem(item2)

for x in myList.itemArray:
    print(x.locNumber)
