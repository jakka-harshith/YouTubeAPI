from connection import *
curr = mycursor

def createDatabase():
    curr.execute("Create Database IF NOT EXISTS youtubeAPI")
    curr.execute("use youtubeAPI")
    channel_desc = """Create Table if not exists channelDesc(
                channelSlNo Integer,
                channelId VARCHAR(255),
                channelTitle TEXT,
                channelStartDate VARCHAR(255),
                channelViewCount BIGINT,
                channelSubscriberCount BIGINT,
                channelVideoCount BIGINT,
                channelCountry VARCHAR(255),
                PRIMARY KEY (channelId)
                );"""
    curr.execute(channel_desc)
    vid_desc = """Create Table if not exists videoDesc(
                videoSlNo Integer,
                videoId VARCHAR(255),
                channelId VARCHAR(255),
                videoTitle TEXT,
                videoPublishedTime VARCHAR(255),
                videoViewCount BIGINT,
                videoLikeCount BIGINT,
                videoDislikeCount BIGINT,
                videoCommentCount BIGINT,
                PRIMARY KEY (videoSlNo, videoId),
                FOREIGN KEY (channelId) REFERENCES channelDesc(channelId)
                );"""
    curr.execute(vid_desc)
    print("Database and Tables are Successfully created")

def insertVideoData(videoInsertValue):
    videoInsert = """Insert into youtubeAPI.videoDesc (videoSlNo, videoId, channelId, videoTitle, videoPublishedTime, videoViewCount, videoLikeCount, videoDislikeCount, videoCommentCount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    curr.execute(videoInsert, videoInsertValue)
    mydb.commit()


def insertChannelData(channelInsertValue):
    channelInsert = """Insert into youtubeAPI.channelDesc (channelSlNo, channelId, channelTitle, channelStartDate, channelViewCount, channelSubscriberCount, channelVideoCount, channelCountry) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    curr.execute(channelInsert, channelInsertValue)
    mydb.commit()


def updateChannelData(channelInsertValue):
    channelUpdate = """Update channelDesc SET channelViewCount = %s, channelSubscriberCount = %s, channelVideoCount = %s WHERE channelId = %s"""

    channelUpdateValue = (channelInsertValue[4], channelInsertValue[5], channelInsertValue[6], channelInsertValue[1])

    curr.execute(channelUpdate, channelUpdateValue)
    mydb.commit()