import csv

def compEdgeClean(minWeight):
    with open("generatedGephiFiles/complete/completeEdges.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = list(csv.reader(file))

    modifiedRows = []
    header = reader[0]
    data_rows = reader[1:] 

    for row in data_rows:
        print("Original:", row)
        print("Weight: ", row[5])

        if int(row[5]) >= int(minWeight):
            modifiedRows.append(row)
        else:
            print("EXECUTE ROW")

    with open("generatedGephiFiles/complete/completeEdges2.csv", mode="w", newline="", encoding="utf-8") as fileEdge:
        writerEdge = csv.writer(fileEdge)
        writerEdge.writerow(header)  
        writerEdge.writerows(modifiedRows)


