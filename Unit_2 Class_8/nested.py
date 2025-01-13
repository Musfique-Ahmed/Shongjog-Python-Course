# Dictionary inside dictionary
student_info = {
    "Tafsir": {"Age": 14, "BG": "A+"},
    "Ahan": {"Age": 16, "BG": "B+"},
    "Abdullah": {"Age": 10, "BG": "A-"},
    "Putul": {"Age": 12, "BG": "B+"},
    "Ahnaf": {"Age": 14, "BG": "A+"},
}

print(student_info["Tafsir"]["Age"])
print(student_info["Ahan"]["BG"])
print(student_info.values())

# List inside dictionary:
student_marks = {
    "Manha": [90, 85,78, 91,99], 
    "Raisa": [91, 84,78, 95,99], 
    "Hamzaa": [93, 80,78, 95,100]
}
print(student_marks["Hamzaa"][0])
print(sum(student_marks["Hamzaa"]))

# Dictionary inside a list:
student_grade = [
    {"Name": "Nilim", "grade": "A+"},
    {"Name": "Wasif", "grade": "A+"},
    {"Name": "Anisha", "grade": "A+"}
]

print(student_grade[1]["Name"])