# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json

import googleapiclient.discovery

def subRatioFunc(subMinimum):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"


    with open("api/api.json", "r", encoding="utf-8") as key_file:
        api_key_data = json.load(key_file)
        DEVELOPER_KEY = api_key_data["developer_key"]
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)


    #Change the location later to: storage
    folder_path = "storage"

    
    f = open(folder_path + "/TotalSubs/totalSubsPerChannel.json", "r", encoding="utf-8")

    youtuberDict = json.loads(f.read())

    subscriberRatioDict = {}

    tempID = 0
    for channel in youtuberDict:

        if youtuberDict[channel][1] > subMinimum:
            #tempID += 1

            print(channel)
            print(youtuberDict[channel][1])

            
            request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel
            )
            response = request.execute()

            print(response)
            
            ratio = int(youtuberDict[channel][1])/int(response["items"][0]["statistics"]["subscriberCount"])

            subscriberRatioDict[channel] = {"name": youtuberDict[channel][0], "sharedSubs": youtuberDict[channel][1], "totalSubs": response["items"][0]["statistics"]["subscriberCount"], "viewCount": response["items"][0]["statistics"]["viewCount"], "videoCount": response["items"][0]["statistics"]["videoCount"]   ,"ratio":ratio}

            #print(subscriberRatioDict)

        #if tempID > 5:
        #    break

        # Define the JSON file path
    json_file_path = os.path.join(folder_path + "/subRatio", "ratioPerChannel.json")

    # Write the dictionary to a JSON file
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(subscriberRatioDict, json_file, indent=4, ensure_ascii=False)

#if __name__ == "__main__":
#    subRatioFunc(10)