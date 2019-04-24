from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint 
import matplotlib.pyplot as pd

DEVELOPER_KEY = "AIzaSyAmmVvu2Zl3iu-2k2CTiDuaI5gP7OLrmqc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"





def youtube_search(q, max_results=50,order="relevance",relatedToVideoId="15Sjjl_24x0" ):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    order = order,
    relatedToVideoId=relatedToVideoId,
    part="id,snippet", # Part signifies the different types of data you want 
    maxResults=max_results,).execute()



#     videos=channelId=channelTitle=categoryId=videoId=viewCount=likeCount=dislikeCount=commentCount=favoriteCount=category=tags  = []
    title = []
    videoId = []
    category = []
    Description = []
    
    
    for search_result in search_response.get("items", []):
        #pprint.pprint(search_result)
  
  
        if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title']) 

            videoId.append(search_result['id']['videoId'])
            
            Description.append(search_result['snippet']['description'])
            
            response = youtube.videos().list(
                part='statistics, snippet',
                id=search_result['id']['videoId']).execute()


    youtube_dict = {'title':title,'videoId':videoId, 'Description':Description}
    print(search_result)
    return youtube_dict

call = youtube_search("music")
print(call)