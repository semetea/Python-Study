import pandas

df1 = pandas.read_csv("supermarkets.csv")  # how to read file using pandas

# openpyxl -> library to read excel files
df8 = pandas.read_csv("data.txt", header=None)  # if data file has no header
df8.columns = ["ID", "Address", "City"]  # can assign header
df9 = df8.set_index("ID")  # can set ID as index
df8.set_index("ID", inplace=True, drop=False)
