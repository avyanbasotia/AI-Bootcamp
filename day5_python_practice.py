import os

from pathlib import Path

print(os.getcwd())

file_path = Path(__file__).parent / "day5_notes.txt"

print("file_path:",file_path)

# 'with' auto-closes the file

with open(file_path, "r") as file:

    contents = file.read()

print(contents)

#this code reads line by line

with open("day5_notes.txt", "r") as file:

    for line in file:

        print("Line:", line.strip())

with open("output.txt", "w") as file:

    file.write("This file was created\n")

    file.write("by my program!\n")

with open("output.txt", "a") as file:

    file.write("Adding one more line.\n")

import csv

students = [

    ["Name", "Grade", "Score"],

    ["Priya", 9, 97],

    ["Marcus", 9, 84],

]

with open("students.csv", "w",

          newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)
# Step 1: Read the CSV and collect scores

students = []

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        students.append({

            "Name": row["Name"],

            "Score": int(row["Score"])   # string -> number!

        })

# Step 2: Calculate the class average

total = sum(s["Score"] for s in students)

average = total / len(students)

# Step 3 & 4: Find above-average students, write results

with open("above_average.txt", "w") as file:

    file.write(f"Class average: {average:.1f}\n")

    for s in students:

        if s["Score"] > average:

            file.write(f"- {s['Name']} ({s['Score']})\n")


