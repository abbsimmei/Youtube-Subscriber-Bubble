import json
import csv

def starRatioGraph(channelName):
    with open("storage/subRatio/ratioPerChannel.json", "r", encoding="utf-8") as f:
        youtuberDict = json.load(f)

    amount = input("How many channels do you want to show on the graph? ")

    # Sort dictionary by ratio descending and get top 500
    topRatio = dict(sorted(
        youtuberDict.items(), 
        key=lambda x: x[1]["ratio"], 
        reverse=True
    )[:int(amount)])

    with open("generatedGephiFiles/ratio/starRatioNodes.csv", mode="w", newline="", encoding="utf-8") as file:
        writerNode = csv.writer(file)
        writerNode.writerow(["Id", "Label", "modularity_class", "Size"])

        with open("generatedGephiFiles/ratio/starRatioEdges.csv", mode="w", newline="", encoding="utf-8") as fileEdge:
            writerEdge = csv.writer(fileEdge)
            writerEdge.writerow(["Source", "Target", "Type", "Id", "Label", "Weight"])

            numID = 1
            edgeID = 0

            for youtuberID in topRatio:
                youtuber = topRatio[youtuberID]

                # Skip if SwinceBall — we want it to be ID 0
                if youtuber["name"] == str(channelName):
                    writerNode.writerow([0, youtuber["name"], 0, youtuber["ratio"]])
                    continue

                writerEdge.writerow([numID, 0, "Undirected", edgeID, "", youtuber["ratio"]])
                writerNode.writerow([numID, youtuber["name"], 0, youtuber["ratio"]])

                numID += 1
                edgeID += 1