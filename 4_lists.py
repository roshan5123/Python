#A Python list is, in simple words, a collection of different items that are organized in a specific order

guns = ['shotgun', 'pistol', 'revolver', 'bazooka', 'machine gun']

print(guns)

['shotgun', 'pistol', 'revolver', 'bazooka', 'machine gun']



print("*******************************")
#accessing elements

print(guns[0])

print(guns[2])

print(guns[4])

print(guns[-1])

print(guns[-2])

print(guns[-3])

print(guns[-4])

print(guns[-5])

print("***************************************")
#3 List Modificaton
guns[0]="AK-47"
print(guns)

print("**************************************************")
#4 Append

guns.append('Ak-47')

print(guns)

 

guns.append('sten gun')

print(guns)

print("***************************************************")

guns=[]
guns.append('Ak-47')

guns.append('sten gun')

guns.append('shotgun')

guns.append('pistol')

guns.append('revolver')

guns.append('bazooka')

guns.append('machine gun')

print(guns)

print("********************************************")

print("Removing Elements")

del guns[0]
print(guns)


popped_guns =guns.pop()
print(guns)
print(popped_guns)

popped_guns = guns.pop(0)
print(guns)
print(popped_guns)


print("***********")

guns = ['shotgun', 'pistol', 'revolver', 'bazooka', 'machine gun']

print(guns)

 
#remove method
guns.remove('revolver')

print(guns)


#sort method
guns.sort()
print(guns)


guns = ['shotgun', 'pistol', 'revolver', 'bazooka', 'machine gun']
print(sorted(guns))
print(guns)


#reverse order
guns.reverse()
print(guns)

#list length

IPL_teams=["MI","CSK","RCB","KKR","DC","SRH","RR","PBKS"]
print(len(IPL_teams)) #same
print(IPL_teams.__len__()) #same

print("***************************************************")

#Numerical Lists
#range

for num in range(1,7):  #Remember to put a colon here
    print(num)


num=list(range(1,8))
print(num)

square_num = []

for num in range(1, 22):

    square = num**2

    square_num.append(square)

 

print(square_num)

print("***************************************")
#List Slicing
fruits = ['orange', 'dragon fruit', 'jackfruit', 'strawberry', 'apple']

print(fruits[0:3])


books = ['great expectations', 'god of flies', 'tempest', 'middle march', 'bleak house', 'hard times']

favorite_books = books[:] #Important

 

print("These are the books I have in my library:")

print(books)

 

print("These are my favorite books:")

print(favorite_books)