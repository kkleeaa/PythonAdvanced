students= ["Klea", "Blini", "Alma","Stina"]

for emri in students:
    print(emri)
fjalia= "sot eshte dite e bukur"
for shkronja in fjalia:
    print(shkronja)

for numri in range(1,5):
    print(numri)
numrat=[1,2,5,8,4,63,26,90,0]
maximumi=numrat[0]
for numri in numrat:
    if numri>maximumi:
        maximumi=numri

print("Maximum is",maximumi)

count=1
while count<=5:
    print("itertion",count)
    count+=1

numbersList=[3,4,5,34,5,6,8,9]
target=20

for numri in numbersList:
    print(numri)
    if numri > target:
        print("Ka gabim")
        break
for numri in numbersList:
    print(numri)
    if numri > target:
        print("Ka gabim")
        continue
while True:
    user_input=input("Enter a positive number")
    if user_input.isnumeric():
        numri=int(user_input)
        if numri<0:
            print("Invalid input. Please try again")
            break
print("You added a valid positive number",numri)

num_list=()
for n in range (0,100):
    if n%2==0:

        num_list.append(n)


print(num_list)
















