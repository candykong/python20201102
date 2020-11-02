#!/usr/bin/python
# -*- coding：UTF-8 -*-

from learn.DBselect import dbConnect


class DbMonitor:
    def __init__(self):
         print("start...")

    #查询单个账号监控的主播数量
    def selectCount(self,userId1):
        sql="select count(*) from `ai_ks_live`.`ks_user_collect` where `user_id`=%s and `status`=1" %userId1
        print(sql)
        count= dbConnect.dbConnection(sql)
        return count

    # 查询团队监控的主播数量
    def selectTeamCount(self,userId1,userId2):
        sql = "select count(*) from `ai_ks_live`.`ks_user_collect` where `user_id` in (%s,%s)and `status`=1" %(userId1,userId2)
        count= dbConnect.dbConnection(sql)
        return count

    #查询某时间段内的视频
    def selectVideoID(self):
        sql = "select `photo_id` from `ai_ks_live`.`ks_video_info` where `publish_time`>SUBDATE(now(),INTERVAL 24 hour) and `deleted_status`=0 limit 220;"
        videoID= dbConnect.dbConnection(sql)
        return videoID

    #查询监控视频的播放数量
    def getVideoViewCount(self,videoId):
        sql = "select `view_count` from `ks_live_spider_extra`.`ks_user_video_monitor` where `photo_id`='%s';" %videoId
        videoID= dbConnect.dbConnection(sql)
        return videoID

    #查询某个用户监控的视频ID
    def getMonitorVideoID(self,userID):
        sql="select `photo_id` from `ks_live_spider_extra`.`ks_schedule_photo_monitor` where `monitor_user_id`=%s and `create_time`>'2019-12-24 10:00:00' and `status`=2;" %userID
        videoID = dbConnect.dbConnection(sql)
        return videoID




