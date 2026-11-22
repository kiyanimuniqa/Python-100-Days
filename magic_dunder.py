class employe:
    name = "muniqa"
    def __len__(self):
      i=0
      for c in self.name:
        i=i+1
      return i   
e= employe()
# print(e.name)
# print(len(e))
def __str__(self):
    return ("The name of employe is {self.name}")