class LinkedTuple:
    def __init__(self):
        self.items = list()


    def add(self,key,value):
        self.items.append((key,value))

    def get(self,key):
        for k,v in self.items:
            if key ==k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self,key,value):
        index = hash(key) % len(self.items)
        self.items[index].add(key,value)
        return

    def get(self,key):
        index = hash(key) % len(self.items)
        print(self.items[index].get(key))
        return self.items[index].get(key)


dict = LinkedDict()


dict.put("hi",30)
print(dict.items[hash("hi") % len(dict.items)].get("hi"))
dict.get("hi")
