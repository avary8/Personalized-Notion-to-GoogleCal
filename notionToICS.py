import pandas as pd
import csv

filePath = "C:\\Users\\avamc_srsebwe\\OneDrive - University of Florida\\projects\\calendar\\"
justFile = "Fall22_9-12.csv"
fileName = filePath + justFile
newFileName = filePath + "NEW" + justFile

col_names = ['Subject', 
             'Start Date',
             'Start Time',
             'End Date',
             'End Time',
             'All Day Event',
             'Description']

names = []
tags = []
start = []
startTime = []
deadline = []
deadTime = []
allDay = []
status = []
description = []

#add in seeing if completed. add special char like ~  to change color to gray in google app script

with open (fileName) as notion_csv:
    notionReader = csv.reader(notion_csv, delimiter = ',')
    next(notionReader)
    for row in notionReader:
        names.append(row[0])
        tags.append(row[10])
        #not doing start because it makes the calendar ugly. but still running it to get values to format for description 
        start.append(row[8]) 
        deadline.append(row[9])
        if row[3] == "Completed":
            status.append("~")
        elif row[5] == "Open":
            status.append("*")
        else:
            status.append("")



for i in range(0, len(names)):
#this is being ignored because start is ignored     
    #if start[i] == deadline [i]:
        #allDay.append(bool(True))
    #else:
        #allDay.append(bool(False))

    allDay.append(bool(False))
  
    temp = start[i].split('~')
    temp2 = deadline[i].split('~')
    #start[i] = temp[0]
    deadline[i] = temp2[0]
    #startTime.append(temp[1])
    deadTime.append(temp2[1])

    description.append(temp[0] + " - " + temp2[0])

    temp.clear()
    temp2.clear()

    #added because not doing start 
    start[i] = deadline[i]
    startTime.append(deadTime[i])

for i in range(0, len(tags)):
    temp = tags[i].split(',')
    names[i] = status[i] + temp[0] + ": " + names[i]
    temp.clear()

with open (newFileName, 'w') as ical_csv:
    icalWriter = csv.writer(ical_csv, lineterminator = '\n')
    icalWriter.writerow (col_names)
    row = []

    for i in range(0, len(names)):
        row.append(names[i])
        row.append(start[i])
        row.append(startTime[i])
        row.append(deadline[i])
        row.append(deadTime[i])
        row.append(allDay[i])
        row.append(description[i])

        icalWriter.writerow(row)
        row.clear()
        
    
        



# col_names = ['Subject', 
#              'Start Date',
#              'Start Time',
#              'End Date',
#              'End Time',
#              'All Day Event']


# notion_csv = pd.read_csv (fileName)
# ics_csv = pd.DataFrame(columns = col_names)
# ics_csv.to_csv(newFileName, index = False)

# names = notion_csv['Name']
# tags = notion_csv['Tags']
# start = notion_csv['sort by open']
# deadline = notion_csv['sort by deadline']
# allDay = []
# for i in range(0, len(start)):
#     if start[i] == deadline [i]:
#         allDay.append(bool(True))
#     else:
#         allDay.append(bool(False))

# namess = []
# namess.append(notion_csv.get_value(1, 0, takeable = True))



# with open(newFileName, 'r') as file:
#     csvWriter = csv.writer(file, delimiter = ',')
#     for i in range(0, len(names)):
#         csvWriter.writerow(str(names[i]))
