import sys
from googleapiclient.discovery import build
from datamodel import *

yt_key = "AIzaSyCPiEUCoO8Hn6TPkqsHgFmAIKDmqU4lEkQ"

youtube = build('youtube', 'v3', developerKey = yt_key)

videoStats = []


numberRec = sys.argv[1]


def chanStat():
    request = youtube.channels().list(
            part = ["Snippet","Statistics"],
            id = channelId
    )

    response = request.execute()
    channelStats = response
    return channelStats


def vidStat(numberRec):
    request = youtube.videos().list(
            part = ["Snippet", "Statistics"],
            chart = "mostPopular",
            maxResults= numberRec
    )

    response = request.execute()
    videoStats.append(response)
    return videoStats

if __name__ == "__main__":
    createDatabase()
    video_stat = vidStat(numberRec)
    # print(video_stat)

    for i in video_stat[0]["items"]:
        curr.execute("Select * from videoDesc")
        vidRecCnt = len(curr.fetchall())
        print("Number of Videos: ", vidRecCnt)


        videoSlNo = vidRecCnt + 1
        videoId = i["id"]
        channelId = i["snippet"]["channelId"]
        videoTitle = i["snippet"]["title"]
        videoPublishedTime = i["snippet"]["publishedAt"]
        videoViewCount = i["statistics"]["viewCount"]
        videoLikeCount = i["statistics"]["likeCount"]
        videoDislikeCount = i["statistics"]["dislikeCount"]
        videoCommentCount = i["statistics"]["commentCount"]

        print("****************************************************************************************************************************************************")
        # print("videoId = "+ videoId)
        # print("channelId = "+ channelId)
        # print("videoTitle = "+ videoTitle)
        # print("publishedTime = "+ videoPublishedTime)
        # print("viewCount = "+ videoViewCount)
        # print("likeCount = "+ videoLikeCount)
        # print("dislikeCount = "+ videoDislikeCount)
        # print("commentCount = "+ videoCommentCount)

        channel_stat = chanStat()
        curr.execute("Select * from channelDesc")
        chanRecCnt = len(curr.fetchall())
        print("Number of Channels: ", chanRecCnt)
        chdesc = channel_stat["items"][0]["snippet"]
        chstat = channel_stat["items"][0]["statistics"]

        channelSlNo = chanRecCnt + 1
        channelTitle = chdesc["title"]
        channelStartDate = chdesc["publishedAt"]
        channelViewCount = chstat["viewCount"]
        channelSubscriberCount = chstat["subscriberCount"]
        channelVideoCount = chstat["videoCount"]

        if "country" in chdesc.keys():
            channelCountry = chdesc["country"]
        else:
            channelCountry = "NA"
        # print("\n")
        # print("channelTitle =" + channelTitle)
        # print("channelStartDate =" + channelStartDate)
        # print("channelViewCount =" + channelViewCount)
        # print("channelSubscriberCount =" + channelSubscriberCount)
        # print("channelVideoCount =" + channelVideoCount)
        # print("channelCountry =" + channelCountry)
        # print("*****************************************************************************************************************************************************")
        

        channelInsertValue = (channelSlNo, channelId, channelTitle, channelStartDate, channelViewCount, channelSubscriberCount, channelVideoCount, channelCountry)
        videoInsertValue = (videoSlNo, videoId, channelId, videoTitle, videoPublishedTime, videoViewCount, videoLikeCount, videoDislikeCount, videoCommentCount)

        print("Channel Insert Value = ", channelInsertValue)
        print("Video Insert Value = ", videoInsertValue)

        curr.execute("Select channelDesc.channelId from channelDesc")

        listRec = curr.fetchall()

        channelIds = []
        for chaId in listRec:
            channelIds.append(chaId[0])

        print("Channels in DB: ",channelIds)

        if channelId in channelIds:
            updateChannelData(channelInsertValue)
            print("Updated the table successfully for the Id ", channelId )
        else:
            insertChannelData(channelInsertValue)
            print("Inserted the record in the table successfully for the Id ", channelId )
        insertVideoData(videoInsertValue)
        
        
print("All the records of the trending videos have been inserted into the Database.")