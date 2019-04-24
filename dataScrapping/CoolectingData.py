import os
import json
import googleapiclient.discovery
import pandas as pd
import pprint 
import matplotlib.pyplot as pd
import csv

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAmmVvu2Zl3iu-2k2CTiDuaI5gP7OLrmqc"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        maxResults=50,
        relatedToVideoId="15Sjjl_24x0",
        q="surfing",
        type="video",
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

            Description.append(search_result['snippet']['description'])

    youtube_dict = {'title':title,'videoId':videoId, 'Description':Description}

    #return youtube_dict
    
    #ReadableDict = json.loads(request.text)
    print(len(videoId))
    print(type(response))
    print(Description)
    print(list(response.keys()))
    print(len(youtube_dict))
    #print(list(response))
    #for item in response['response']['items']:

    #    print("Video Tittle: ", (item[title]))

    with open("youtube1.csv", "w", encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in youtube_dict.items():
            writer.writerow([key, value])
    
if __name__ == "__main__":
    main()