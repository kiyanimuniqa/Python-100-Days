class vector():
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return (f"{self.i}i + {self.j}j + {self.k}k")
#addition
    def __add__(self,x):
        return vector(self.i + x.i, + self.j + x.j, self.k + x.k)
#subtraction
    def __sub__(self,x):
        return vector(self.i - x.i, + self.j - x.j, self.k - x.k)
#multiplication
    def __mul__(self,x):
        return vector(self.i * x.i, + self.j * x.j, self.k * x.k)
  
v1=vector(10,6,9)
v2=vector(2,3,3)

print(f" vector 1: {v1}")
print(f" vector 2: {v2}")

print(f"Addition : {v1 + v2}")
print(f"subtraction : {v1 - v2}")
print(f"Multiplication : {v1 * v2}")