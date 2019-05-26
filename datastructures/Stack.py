class Stack:
    def __init__(self):
        self.ds = []
    def push(self,i):
        self.ds.append(i)
    def pop(self):
        if len(self.ds)>0:
            x = "Popped "+str(self.ds.pop())
        else:
            x = "Empty stack!!"
        return x
    def top(self):
        if len(self.ds)>0:
            return self.ds[-1]
        else:
            return "Empty stack!!"
    def display(self):
        if len(self.ds)>0:
            print(str(list(map(str,self.ds))))
        else:
            print("Empty stack!!")
