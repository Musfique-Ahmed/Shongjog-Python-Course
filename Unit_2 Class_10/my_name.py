file= open("farah.txt","r")
# print(file.read())
content  = file.readlines()

file.close()
# file= open("farah.txt","a")
# file.write("hgadjkslkgjuhkj")
# file.close()

file = open("senior_employee.txt", "a")

employee_info = {}

for info in content:
    info = info.strip()
    info = info.split()
    print(info)
    
    employee_info[info[0]] = []

    employee_info[info[0]].append(info[1])
    employee_info[info[0]].append(info[2])
    employee_info[info[0]].append(info[3])

    if int(info[1]) > 40:
        file.write(f"{info[0]} {info[3]}\n")

file.close()
print(employee_info)