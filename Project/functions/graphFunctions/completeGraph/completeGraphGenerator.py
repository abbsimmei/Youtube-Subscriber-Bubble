import json
import csv

def compGraph2(subMinimum, channelName):

    f = open("storage/Connections/connections.json", "r", encoding="utf-8")

    connectionsDict = json.loads(f.read())

    # Clear the files before writing headers
    with open("generatedGephiFiles/complete/completeNodes.csv", mode="w", newline="", encoding="utf-8") as file:
        writerNode = csv.writer(file)
        writerNode.writerow(["Id", "Label", "modularity_class", "Size"])  

    with open("generatedGephiFiles/complete/completeEdges.csv", mode="w", newline="", encoding="utf-8") as fileEdge:
        writerEdge = csv.writer(fileEdge)
        writerEdge.writerow(["Source", "Target", "Type", "Id", "Label", "Weight"])  


    #Generating the Node and Edge files
    with open("generatedGephiFiles/complete/completeNodes.csv", mode="a", newline="", encoding="utf-8") as file:
            writerNode = csv.writer(file)

            with open("generatedGephiFiles/complete/completeEdges.csv", mode="a", newline="", encoding="utf-8") as fileEdge:
                writerEdge = csv.writer(fileEdge)

                f = open("storage/TotalSubs/totalSubsPerChannel.json", "r", encoding="utf-8")

                youtuberDict = json.loads(f.read())
                
                filteredYoutuberDict = {}

                #Creating a list (filteredYoutuberDict) with all the channels over 50 subs and giving them an ID that will be used in gephi
                id = 0
                for youtuberID in youtuberDict:
                    youtuber = youtuberDict[youtuberID]
                    if youtuber[1] <= int(subMinimum):
                        continue 
                    if youtuber[0] == str(channelName):
                        continue
                    
                    filteredYoutuberDict[youtuberID] = youtuber + [id]

                    id += 1
                
                #Writing in the ID and name to the completeNodes.csv
                for youtuberID in filteredYoutuberDict:
                    youtuber = filteredYoutuberDict[youtuberID]
                    writerNode.writerow([youtuber[2], youtuber[0], "", youtuber[1]])
                
                edgeID = 0
                #Looping every connection, finding their id's and writing them into the Edge file. 
                for connection in connectionsDict:


                    splited = connection.split(",")

                    channel1 = filteredYoutuberDict[splited[0]]
                    channel2 = filteredYoutuberDict[splited[1]]

                    #if connection == "UC4-79UOlP48-QNGgCko5p2g,UCX6OQ3DkcsbYNE6H8uQQuVA":
                    #    print("hello!!")
                    #    print(channel1)
                    #    print(channel2)
                    #    print([channel1[2], channel2[2], "Undirected", edgeID,"", connectionsDict[connection]])
                    
                    writerEdge.writerow([channel1[2], channel2[2], "Undirected", edgeID,"", connectionsDict[connection]])

                    edgeID += 1
                    #if edgeID == 5:
                    #    break

    print (edgeID)

            
            



