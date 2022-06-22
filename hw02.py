# Title: DS5100 HW02
# Name: Aubrey Winger
# UserID: alw8ef

#Task 1
grades = {"Jon":95,"Mike":84,"Jaime":99}
print(grades)

#Task 2
found = False
for key in grades:
    if key=="Mike":
        found = True
        print("Grade found for Mike:", end=" ")
        print(grades[key])
if found == False:
    raise IndexError
        
#Task 3
found = False
for key in grades:
    if key=="Jeff":
        found = True
        print("Grade found for Jeff:", end=" ")
        print(grades[key])
if found == False:
    raise IndexError
        
#Task 4
names = ["Alex", "Patrick", "Tom", "Joe", "Alex"]
print(names)

#Task 5 
names.sort()
print(names)

#Task 6
names_set = {"Alex", "Patrick", "Tom", "Joe", "Alex"}
print(names_set)

#Task 7a
td = [2, 4, 1, 3, 1]
print(td)

#Task 7b
td_odd=[]
for i in td:
    if i%2!=0:
        td_odd.append(i)
print(td_odd)

#Task 7c
td_greatOne=[]
for j in td:
    if j>1:
        td_greatOne.append(j)
print(td_greatOne)
        

        
    


