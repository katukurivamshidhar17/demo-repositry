
import numpy as np
import pandas as pd
labels=['a','b','c']
mydata=[10,20,30]
arr=np.array(mydata)
d={'a':10,'b':20,'c':30}
print("labels:",labels)
print("mydata:",mydata)
print("Dictionary:",d)
print("array:",arr)


#  indexing and slicing
ser1 = pd.Series([1, 2, 3, 4], index=['CA', 'OR', 'CO', 'AZ'])
ser2 = pd.Series([1, 2, 5, 4], index=['CA', 'OR', 'NV', 'AZ'])

print("\nIndexing by name of the item or object:")
print("Value of CA in ser1:", ser1['CA'])
print("Value of AZ in ser1:", ser1['AZ'])
print("Value of NV in ser2:", ser2['NV'])

print("\nIndexing by number:")
print("Value of CA in ser1:", ser1[0])
print("Value of AZ in ser1:", ser1[3])
print("Value of NV in ser2:", ser2[2])

print("\nIndexing by the range:")
print("Values of OR, CO, and AZ in ser1:\n", ser1[1:4])

#adding or merging two series with common indices
ser1 = pd.Series([1, 2, 3, 4], index=['CA', 'OR', 'CO', 'AZ'])
ser2 = pd.Series([1, 2, 5, 4], index=['CA', 'OR', 'NV', 'AZ'])
ser3 =ser1+ser2
print(ser3)
print(ser1*ser2)
print(ser3)

# creating and accessing the data frame

matrix_data = np.random.randint(1, 100, size=(5, 4))   
row_labels = ['A', 'B', 'C', 'D', 'E']
column_headings = ['W', 'X', 'Y', 'Z']

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
print("\nDataFrame:")
print(df)

#adding the data frame and dropping the data frame to it

#  Add a new column
df["Total"] = df["W"] + df["X"] + df["Y"] + df["Z"]
print("\nDataFrame after adding 'Total' column:")
print(df)

#  Dropping a column
df_dropped_col = df.drop("Y", axis=1)
print("\nDataFrame after dropping column 'Y':")
print(df_dropped_col)

#  Dropping a row
df_dropped_row = df.drop("C", axis=0)
print("\nDataFrame after dropping row 'C':")
print(df_dropped_row)

# Subsetting (filtering rows)
subset = df[df["Total"] > 200]
print("\nSubset of rows where Total > 200:")
print(subset)

# Using .loc (label-based indexing)
print("\nUsing .loc to select rows A to C and columns W and X:")
print(df.loc["A":"C", ["W", "X"]])

# Using .iloc (position-based indexing)
print("\nUsing .iloc to select first 3 rows and first 2 columns:")
print(df.iloc[0:3, 0:2])


# Creating a  DataFrame for  missing values
data_with_nan = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 35, 40, np.nan],  
    "City": ["New York", "London", None, "Tokyo", "Paris"], 
    "Score": [85, 90, np.nan, 70, 95]      
}

df_nan = pd.DataFrame(data_with_nan)

print("Original DataFrame with Missing Values:")
print(df_nan)

# Detect missing values
print("\nCheck for missing values (True = missing):")
print(df_nan.isnull())

# Count missing values per column
print("\nCount of missing values in each column:")
print(df_nan.isnull().sum())

# Drop rows with any missing values
df_dropna = df_nan.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropna)


# Fill missing values with defaults(fiilna method is used for none values)
df_fillna = df_nan.fillna({
    "Age": df_nan["Age"].mean(),   
    "City": "Unknown",              
    "Score": 0                       
})
print("\nDataFrame after filling missing values:")
print(df_fillna)


# adding group by method to dataframes
data_groupby = {
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "Name": ["kajal", "anushkha", "kalyanidarshini", "ivana", "thammana", "shardha", "divyabharathi"],
    "Salary": [60000, 45000, 50000, 65000, 47000, 52000, 70000],
    "Experience": [2, 5, 3, 7, 2, 4, 10]
}

df_group = pd.DataFrame(data_groupby)

print("Original Employee DataFrame:")
print(df_group)

# Group by Department - Average Salary
print("\nAverage Salary by Department:")
print(df_group.groupby("Department")["Salary"].mean())

# Group by Department - Maximum Experience
print("\nMaximum Experience by Department:")
print(df_group.groupby("Department")["Experience"].max())

# Group by Department - Summary of Salary & Experience
print("\nDepartment-wise Summary (Salary & Experience):")
print(df_group.groupby("Department")[["Salary", "Experience"]].agg(["mean", "max", "min"]))


#adding,merging and concatenation to dataframe

# Create two numeric DataFrames
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Math": [85, 90, 78, 92],
    "Science": [88, 76, 95, 89]
})

df2 = pd.DataFrame({
    "ID": [3, 4, 5, 6],
    "Math": [80, 70, 88, 77],
    "Science": [85, 91, 82, 79]
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# 1. ADDITION of DataFrames (element-wise)
print("\nAddition of df1 and df2 (aligns by index and columns):")
print(df1.add(df2, fill_value=0))

# 2. MERGING on 'ID' column
print("\nMerge DataFrames on 'ID' (inner join):")
print(pd.merge(df1, df2, on="ID", suffixes=('_df1', '_df2')))

# 3. CONCATENATION (stacking DataFrames)
print("\nConcatenation of df1 and df2 (row-wise):")
print(pd.concat([df1, df2], ignore_index=True))


#adding multiple dataframes to merge to sort out the keys
#Creating  two DataFrames with multiple keys
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Subject": ["Math", "Math", "Science", "Science"],
    "Score": [85, 90, 78, 92]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3, 4, 3],
    "Subject": ["Math", "Math", "Science", "Science", "Math"],
    "Teacher": ["Mr. A", "Mr. B", "Ms. C", "Ms. D", "Mr. E"]
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

# Merging on two keys: ID and Subject
merged = pd.merge(df1, df2, on=["ID", "Subject"], how="inner")

print("\nMerged DataFrame on keys ['ID', 'Subject']:")
print(merged)

#unquie and header for a data frame
# Creating a dataframe for srh team
data = {
    "Player": ["Abhishek Sharma", "Rahul Tripathi", "Aiden Markram", "Heinrich Klaasen", "Bhuvneshwar Kumar",
               "Umran Malik", "Mayank Agarwal", "Washington Sundar", "Marco Jansen", "T Natarajan"],
    "Team": ["SRH"] * 10, 
    "Runs": [450, 320, 280, 400, 50, 30, 200, 150, 120, 60],
    "Wickets": [5, 2, 3, 0, 15, 12, 0, 8, 10, 14]
}

srh_df = pd.DataFrame(data)

print("Full SRH DataFrame:")
print(srh_df)

# head()
print("\nFirst 5 rows using head():")
print(srh_df.head())

# unique()
print("\nUnique Team(s):")
print(srh_df["Team"].unique())









