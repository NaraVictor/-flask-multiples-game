# dictionaries are data structures used to store key-value
# paired data

students = {
    # key           value
    "BSC/4021/16": "Emmanuel Kwao Ametepey",
    "number1": 80,
    "cup": "Nasaal Lawrencia",
    "number2": 50,
    "paper": "Suleman Mariam",
    "key": True,
    "number3": 100,
}

# delete an item
# del students["number"]

# adding a new item
students["bus"] = "KIA Bus"


# updating an existing value
# students['number'] = 12

total = ""
for x in students.values():
    if type(x) == str:
        total = total + x + ", -> "

print(total)


# lst = ['mango', 100, 'boy', 'heaven']
# del lst[1]
# for a in lst:
#     print(a)
