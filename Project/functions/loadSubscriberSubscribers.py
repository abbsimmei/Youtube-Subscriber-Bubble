
#At the channelId is the id of the channel that then return who they are subscribed to.


# -*- coding: utf-8 -*-

# Sample Python code for youtube.subscriptions.list
# See instructions for running these code samples locally:
    # https://developers.google.com/explorer-help/code-samples#python

import os
import csv
import json

import googleapiclient.discovery

def fetchSecondarySubs():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    with open("api/api.json", "r", encoding="utf-8") as key_file:
        api_key_data = json.load(key_file)
        DEVELOPER_KEY = api_key_data["developer_key"]

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)


    with open("storage/firstSubs/channels.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        
        # Iterate over each row and print the channel name and ID
        tempID = 0
        for row in reader:
            tempID += 1
            if row:  # Ensure the row is not empty
                print(f"Channel Name: {row[0]} | Channel ID: {row[1]}")
                
                loopBool = True
                nextPageToken = ""

                with open(f"storage/secondarySubs/{row[1]}.csv", mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)

                    while loopBool == True:
                        request = youtube.subscriptions().list(
                            part="Snippet",
                            channelId=row[1],
                            maxResults=50,
                            pageToken=nextPageToken
                        )
                        response = request.execute()
                        
                        #Add the amount loaded in this itereration to the amountLoaded variable.
                        #print("Page info: " + str(response))
                        print(response["pageInfo"]["totalResults"])
                        #Looping through every channel loaded this itereration. Will also storage it to a document. 
                        for item in response['items']:
                            print("Channel Name: " + item["snippet"]["title"] + "| Channel id: " + item["snippet"]["resourceId"]["channelId"])
                            writer.writerow([item["snippet"]["title"], item["snippet"]["resourceId"]["channelId"]])

                        #Checking if next page token exists. If it doesn't we have found all the persons subscriber and we set the loopBool to false.
                        try:
                            nextPageToken = response["nextPageToken"]
                            print("Next page token: " + response["nextPageToken"])
                        except:
                            loopBool = False
            #if tempID > 2:
            #    break         
                #Temporary Break. Remove to load everone's data!



#if __name__ == "__main__":
#    main()