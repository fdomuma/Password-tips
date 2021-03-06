
from tkinter import *
import pandas as pd

root = Tk()
root.title("Password manager")

# Search feature
searchBox = Entry(root, width=50, borderwidth=5)
searchBox.insert(0, "Look for place!")
searchBox.grid(row=0, column=1, columnspan=2)

def searchPlace():
    db = pd.read_csv("pass_db.csv", sep=";")
    keys = searchBox.get()

    rowIndex = db["Place"].str.contains(keys, case=False)
    if len(rowIndex) > 1:
        rowIndex = rowIndex[0]
    global structure, place, keyword
    structure, place, keyword = db.iloc[rowIndex.index[0]].values

    structureValue = Label(root, text=structure)
    placeValue = Label(root, text=place)
    keywordValue = Label(root, text=keyword)

    structureValue.grid(column=1, row=1, columnspan=2)
    placeValue.grid(column=1, row=2, columnspan=2)
    keywordValue.grid(column=1, row=3, columnspan=2)


searchButton = Button(root, text="Search", command=searchPlace)

searchButton.grid(row=0, column=0)


# Showing attributes
structureKey = Label(root, text="Structure: ")
placeKey = Label(root, text="Place: ")
keywordKey = Label(root, text="Keyword: ")

structureKey.grid(column=0, row=1)
placeKey.grid(column=0, row=2)
keywordKey.grid(column=0, row=3)

# Features

newButton = Button(root, text="Create password", bg="green", padx=8, pady=8)
editButton = Button(root, text="Edit", padx=8, pady=8, width=12)
deleteButton = Button(root, text="Delete", bg="red", padx=8, pady=8, width=12)

freeRow = Label(root, text="")
freeRow.grid(column=0, row=4, columnspan=3)

newButton.grid(column=0, row=5)
editButton.grid(column=1, row=5)
deleteButton.grid(column=2, row=5)

root.mainloop()