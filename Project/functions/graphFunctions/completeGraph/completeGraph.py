import os
import glob
import csv
import json

def compGraph1(subMinimum, subLimit, channelName):

    f = open("storage/TotalSubs/totalSubsPerChannel.json", "r", encoding="utf-8")

    youtuberDict = json.loads(f.read())

    # Get all CSV files in the storage folder
    csv_files = glob.glob(os.path.join("storage/secondarySubs", "*.csv"))

    file_count = 0

    connectionList = []

    for file in csv_files:
        # Count rows first
        with open(file, mode="r", newline="", encoding="utf-8") as f:
            total_rows = sum(1 for row in csv.reader(f) if row)
        #print(f"Total rows in this file before processing: {total_rows}")

        if int(total_rows) <= int(subLimit):
            with open(file, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                filteredYoutuber = []

                for row in reader:
                    try:
                        #Filters out every youtuber with less or equal to 50 shared subs
                        if youtuberDict[row[1]][1] <= int(subMinimum):
                            continue
                        #Filters out myself since that would break the premise of the graph
                        if youtuberDict[row[1]][0] == str(channelName):
                            continue
                        #print(youtuberDict[row[1]][1])
                        filteredYoutuber.append(row[1])
                    except KeyError:
                        print("KeyError!!")
            
                

                # Gå igenom varje id och matcha det med alla andra. När du har gjort en loop glöm icke att ta bort första så att den
                # inte nämns två gånger. Sedan kanske spara det nånstans för att sedan lägga ihop totalen. 
                while filteredYoutuber:
                    item = filteredYoutuber.pop(0)
                    for item2 in filteredYoutuber:
                        connectionList.append(item + "," + item2)

                #print(len(connectionList))

            file_count += 1
        #if file_count == 2:
        #    break  #Can you please when the loop is finished write

    connectionDict = {}

    for connection in connectionList:
        if connection in connectionDict:
            connectionDict[connection] += 1
        else:
            connectionDict[connection] = 1


    #print(len(connectionDict))




    # Write the dictionary to a JSON file
    with open("storage/Connections/connections.json", "w", encoding="utf-8") as json_file:
        json.dump(connectionDict, json_file, indent=4, ensure_ascii=False)