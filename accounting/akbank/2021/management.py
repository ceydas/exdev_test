import random


# ozan's functions
def management_people():

    names = [
        "Ahmet Yılmaz",
        "Ayşe Kaya",
        "Mehmet Ali Demir",
        "Fatma Şahin",
        "Mustafa Öztürk",
        "Emre Korkmaz",
        "Zeynep Arslan",
        "Ali İpek",
        "Selin Kılıç",
        "Hüseyin Karahan"
    ]

    return names

def generate_tasks():
    tasks = [
    "Prepare financial statements for Q1",
    "Reconcile bank accounts",
    "Calculate depreciation for fixed assets",
    "Perform inventory count",
    "Create annual budget for upcoming fiscal year",
    "Review accounts payable aging report",
    "Conduct variance analysis for sales and expenses",
    "Assist with tax preparation",
    "Perform internal audit of accounts receivable",
    "Analyze financial ratios and trends"
    ]
    
    random.shuffle(tasks)

    # shuffle the array to get a random order
    random.shuffle(tasks)
    return tasks

i = 0
def management_tasks(people):
    tasks = {}
    for person in people:
        tasks[person] = tasks[i]
        i += 1
    
    return tasks

