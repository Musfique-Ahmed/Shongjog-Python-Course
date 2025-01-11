#Task-5
n = 5
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")

#Task-6
user_input = "Python"
for i in user_input[::-1]:
    print(i, end="")

#Task-7
lst = [-10, 15, -20, 25, 30, -5]
for i in lst:
    if i > 0: 
        print(i)

# task-8
n= 5
fact = 1
for i in range(2,n+1):
    fact = fact * i
print(fact)

#task-9:
lst = [3, 8, 2, 9, 4, 7]
lasrge = lst[0] #9
for i in lst: #3,8,
    if i > lasrge:#3>3, 8>3? i=8
        lasrge = i

print(lasrge)