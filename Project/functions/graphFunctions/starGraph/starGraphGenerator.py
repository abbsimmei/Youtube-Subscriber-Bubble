import json
import csv


def starGraph(subMinimum, channelName):

    f = open("storage/TotalSubs/totalSubsPerChannel.json", "r", encoding="utf-8")

    youtuberDict = json.loads(f.read())

    #Generating the Node and Edge files
    with open("generatedGephiFiles/star/starNodes.csv", mode="w", newline="", encoding="utf-8") as file:
            writerNode = csv.writer(file)
            writerNode.writerow(["Id", "Label", "modularity_class", "Size"])

            with open("generatedGephiFiles/star/starEdges.csv", mode="w", newline="", encoding="utf-8") as fileEdge:
                writerEdge = csv.writer(fileEdge)
                writerEdge.writerow(["Source", "Target", "Type", "Id", "Label", "Weight"])


                #Looping through every youtuber
                numID = 1
                edgeID = 0
                for youtuberID in youtuberDict:
                    youtuber = youtuberDict[youtuberID]

                    # In order not to overload the Graph Software I limit the amount of youtubers I show in the graph by the amount of mentions they have.
                    # After some tests I found that 50 gave about 500 different channels which is a lot but not as much as 200000
                    if youtuber[1] <= int(subMinimum):
                        continue

                    # Here I ensure the Swinceball, which I want to be able to access easily has the ID of 0. 
                    if youtuber[0] == str(channelName):
                        writerNode.writerow([0, youtuber[0], 0, youtuber[1]])
                        continue
                    
                    writerEdge.writerow([numID, 0, "Undirected", edgeID,"", youtuber[1]])
                    writerNode.writerow([numID, youtuber[0], 0, youtuber[1]])

                    numID += 1
                    edgeID += 1
            
            

