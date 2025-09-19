
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\user\Desktop\seaborn\student_marks_advanced (1).xlsx"  
data = pd.read_excel(file_path, sheet_name="Sheet1")

subjects = ["Maths", "Science", "English", "History", "Computer"]

plt.style.use("seaborn-v0_8")
sns.set_theme(palette="viridis")

avg_marks = data[subjects].mean()
plt.figure(figsize=(7,5))
plt.bar(subjects, avg_marks, color="skyblue")
plt.title("Average Marks per Subject")
plt.ylabel("Average Marks")
plt.show()

plt.figure(figsize=(5,5))
data["Result"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90, colors=["#66c2a5","#fc8d62"])
plt.title("Pass vs Fail Students")
plt.ylabel("")
plt.show()

class_avg = data.groupby("Class")["AverageMarks"].mean()
plt.figure(figsize=(7,5))
plt.plot(class_avg.index, class_avg.values, marker="o", color="purple")
plt.title("Average Marks by Class")
plt.xlabel("Class")
plt.ylabel("Average Marks")
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(data["Maths"], data["Science"], alpha=0.7, color="green")
plt.title("Maths vs Science Marks")
plt.xlabel("Maths")
plt.ylabel("Science")
plt.show()

plt.figure(figsize=(7,5))
plt.hist(data["TotalMarks"], bins=10, edgecolor="black", color="orange")
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(data[subjects + ["TotalMarks"]].corr(), annot=True, cmap="viridis", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="Gender", y="TotalMarks", data=data, hue="Gender", palette="viridis", legend=False)
plt.title("Total Marks by Gender")
plt.show()

plt.figure(figsize=(7,5))
sns.countplot(x="Class", data=data, hue="Class", palette="viridis", legend=False)
plt.title("Number of Students per Class")
plt.show()

plt.figure(figsize=(7,5))
sns.violinplot(x="Gender", y="English", data=data, hue="Gender", palette="muted", legend=False)
plt.title("Distribution of English Marks by Gender")
plt.show()

sns.pairplot(data[subjects + ["Gender"]], hue="Gender", palette="viridis")
plt.suptitle("Pairplot of Subjects by Gender", y=1.02)
plt.show()
