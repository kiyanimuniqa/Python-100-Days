# #list of numbers and i apply the lambda and mapping function to multiply each number with 10
numbers=[1,2,3,4,5]
new_numbers= list(map(lambda number:number*10,numbers))
print(new_numbers)

#list of names in small letters and convert them into capital letters:
names=['ali','sara','isha']
new_names=list(map(str.upper,names))
print(new_names)
# add 5 to the list and find the square:
numbers=[10,20,30,40]
new_numbers=list(map(lambda number: (number+5)**2,numbers))
print(new_numbers)

prices=[100,200,300]
new_prices=list(map(lambda price:(price/100)*80,prices))
print(new_prices)