# Class Task:

"""Task 1: Data Cleaning
Replace all None values with "Unknown".

employees = {
    "Ali": "HR",
    "Sara": None,
    "Usman": "IT",
    "Hina": None
}"""

employees = {"Ali": "HR", "Sara": None, "Usman": "IT", "Hina": None}
for name, pos in employees.items():
    if employees[name] is None:
        employees[name] = "Unknown"
print("Task 1:", employees)


"""Task 2: Word Frequency Counter
Count how many times each word appears in a sentence using a dictionary."""


sentence = "hello world hello python world"
word_count = {}
words = sentence.split()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Task 2:", word_count)


"""Task 3: Dataset Summary
Create a dictionary summarizing total students, average marks, and top scorer."""

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 78}
]
total = len(students)
all_marks = [std["marks"] for std in students]
average = sum(all_marks) / total
top_scorer = max(students, key=lambda x: x["marks"])
print(f"Task 3: Total={total}, Average={average}, Top={top_scorer['name']}")


"""Task 4: Data Mapping
Convert two lists into a dictionary using zip().

keys = ["Name", "Age", "City"]
values = ["Ali", 23, "Karachi"]"""

keys = ["Name", "Age", "City"]
values = ["Ali", 23, "Karachi"]
result = {k: v for k, v in zip(keys, values)}
print("Task 4:", result)

"""Task 5: Frequency of Features
Given a list of categories, count the frequency of each unique value.

features = ["Male", "Female", "Male", "Female", "Other"]"""

features = ["Male", "Female", "Male", "Female", "Other"]
frequency = {item: features.count(item) for item in set(features)}
print("Task 5:", frequency)