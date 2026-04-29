#MY code 
class MyHashMap:
    def __init__(self):
        self.data = {}

    def put(self, key: int, value: int) -> None:
        if key in self.data: 
            self.data[key] = value
        else:
            return None

    def get(self, key: int) -> int:
        if key in self.data:
            return self.data[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.data:
            del self.data[key]
#CORRECT
class MyHashMap:
    def __init__(self):
        self.data = {}

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        if key in self.data:
            return self.data[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.data:
            del self.data[key]

#need for self.data to create an empty dict PER INSTANCE. ask yourself why?
#
