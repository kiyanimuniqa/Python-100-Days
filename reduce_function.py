from functools import reduce
numbers=[2,3,4]
new_numbers=reduce(lambda a,b:a*b,numbers)
print(new_numbers)

words=["i","love","python"]
new_words=reduce(lambda a,b:a+" "+b, words)
print(new_words)

numbers=[10,45,22,89,30]
new_numbers=reduce(lambda a,b:a if a>b else b,numbers)
print(new_numbers)