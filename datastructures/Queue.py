class Queue:
    def __init__(self):
        self.ds = []
    def add(self,i):
        self.ds.append(i)
    def remove(self):
        if len(self.ds)>0:
            x = "Removed "+str(self.ds.pop(0))
        else:
            x = "Empty Queue!!"
        return x
    def front(self):
        if len(self.ds)>0:
            return self.ds[0]
        else:
            return "Empty Queue!!"
    def rear(self):
        if len(self.ds)>0:
            return self.ds[-1]
        else:
            return "Empty Queue!!"
    def display(self):
        if len(self.ds)>0:
            print(str(list(map(str,self.ds))))
        else:
            print("Empty Queue!!")
