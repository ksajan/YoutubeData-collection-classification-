# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import googleapiclient.discovery
#from apiclient.discovery import build
#from apiclient.errors import HttpError
#from oauth2client.tools import argparser
import pandas as pd
import pprint 
import matplotlib.pyplot as pd

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAmmVvu2Zl3iu-2k2CTiDuaI5gP7OLrmqc"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        relatedToVideoId="UBuH1b0Dqm0",
        type="video",
        #category = "videoCategory"
    )
    response = request.execute()
    title = []
    videoId =[]
    Description = []
    Category = []  


    for search_result in response.get("items", []):
    	if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title']) 

            videoId.append(search_result['id']['videoId'])

    youtube_dict = {'title':title,'videoId':videoId}

    #return youtube_dict
    
    #ReadableDict = json.loads(request.text)
    print(type(response))
    print(list(response.keys()))
    print(youtube_dict)
    #print(list(response))
    #for item in response['response']['items']:

    #    print("Video Tittle: ", (item[title]))
if __name__ == "__main__":
    main()