import sqlite3
import pandas as pd

# reading from the csv file only using the columns CSA_name and walkability index
csvFile = pd.read_csv('EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv', usecols=['CSA_Name', 'NatWalkInd'])

# get rid of duplicates with the same CSA_Name column 
csvFile = csvFile.drop_duplicates(subset=['CSA_Name'])

# sending the data to a sqlite db
sqliteConnection = sqlite3.connect('sql.db')
curse = sqliteConnection.cursor()

#curse.execute("CREATE TABLE walkability (Location, Walkability)")

data_rows = csvFile.values.tolist()

data_to_add = [(d_row[0], d_row[1]) for d_row in data_rows]
curse.executemany("INSERT INTO walkability VALUES(?, ?)", data_to_add)

sqliteConnection.commit()


res = curse.execute("SELECT * FROM sqlite_master")
print(*res)