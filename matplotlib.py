import matplotlib.pyplot as plt
import numpy as np

students = ["Vamshi", "Shruthi", "Sandy", "Sanjana", "Ravi"]
marks = [85, 92, 78, 88, 95]   
age = [16, 17, 16, 17, 16]     

plt.figure(figsize=(8,5))
plt.bar(students, marks, color="skyblue")
plt.title("Students Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8,5))
plt.plot(students, marks, marker="o", color="red", linewidth=2)
plt.title("Students Marks - Line Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,6))
plt.pie(marks, labels=students, autopct="%1.1f%%", startangle=140, colors=["gold","lightgreen","lightcoral","skyblue","violet"])
plt.title("Students Marks - Pie Chart")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(students, marks, color="purple", s=[m*2 for m in marks], edgecolor="black")
plt.title("Students Marks - Scatter Plot (size proportional to marks)")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.barh(students, marks, color="orange")
plt.title("Students Marks - Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()

all_marks = np.random.randint(50, 101, 50)
plt.figure(figsize=(8,5))
plt.hist(all_marks, bins=10, color="green", edgecolor="black")
plt.title("Distribution of Student Marks - Histogram")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
 