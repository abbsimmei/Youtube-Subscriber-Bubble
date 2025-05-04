
# This is the code which loaded who my subscribers are. :D


# -*- coding: utf-8 -*-

# Sample Python code for youtube.subscriptions.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import csv

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def fetchSubs():

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    #Client secret so that I get access to the API
    client_secrets_file = "api/secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    #Asks how many subscribers we want to load. 
    amountSubs = input("How many subscribers do you want to load, Max (1000) : ")
    if int(amountSubs) > int(1000):
        amountSubs = int(1000)

    amountLoaded = 0

    nextPageToken = ""

        #While the amountLoaded is less than the target we will continue loading more. 
    with open("storage/firstSubs/channels.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        while int(amountSubs) > int(amountLoaded):
            
            #Creating the request.
            request = youtube.subscriptions().list(
                part="subscriberSnippet",
                maxResults=amountSubs,
                mySubscribers=True,
                pageToken=nextPageToken
            )
            response = request.execute()

            #Add the amount loaded in this itereration to the amountLoaded variable.
            print("Page info: " + str(response["pageInfo"]))
            amountLoaded = int(amountLoaded) + int(response["pageInfo"]["resultsPerPage"])

            #Changing the token for next page according to this itereration.
            try:
                print("Next page token: " + response["nextPageToken"])
                nextPageToken = response["nextPageToken"]
            except:
                print("Reached the end")

            #Looping through every channel loaded this itereration. Will also storage it to a document. 
            for item in response['items']:
                print("Channel Name: " + item["subscriberSnippet"]["title"] + "| Channel id: " + item["subscriberSnippet"]["channelId"])

                #Writing to the channels.csv. There are two things which i add.
                #Name of the subscriber
                #Their ID
                writer.writerow([item["subscriberSnippet"]["title"], item["subscriberSnippet"]["channelId"]])



        

#if __name__ == "__main__":
#    main()