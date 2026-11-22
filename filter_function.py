# numbers=[5,10,15,20,25,30]
# new_numbers=list(filter(lambda number:number>10,numbers))
# print(new_numbers)

# names=["ali","sara","ahmed","usman","ayesha"]
# new_names=list(filter(lambda name: name.startswith("a"),names))
# print(new_names)

# numbers=[12,7,18,21,30,33]
# new_numbers=list(filter(lambda number:number%3==0,numbers))
# print(new_numbers)

numbers=[1,2,3,4,5,6,7,8,9,10]
new_numbers=list(filter(lambda number:number%2==0,numbers))
print(new_numbers) 
NEW_NUMS=list(map(lambda new_number: new_number**2,new_numbers))
print(NEW_NUMS)