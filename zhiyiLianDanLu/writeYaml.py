import  yaml


def test_yaml2():
    data = {
        "url": "/live-api/v2/streamer/collect-list",
        "json": {
            "avgRewardTopOneNumLast7DaysMax": 0,
            "avgRewardTopOneNumLast7DaysMin": 0,
            "avgWatchNumLast7DaysMax": 0,
            "avgWatchNumLast7DaysMin": 0,
            "endDate": "2020-11-11",
            "fansNumMax": 0,
            "fansNumMin": 0,
            "gender": 0,
            "myMonitor": 1,
            "rankStatus": 1,
            "rewardNumMax": 0,
            "rewardNumMin": 0,
            "startDate": "2020-11-11",
            "totalSaleAmountMax": 0,
            "totalSaleAmountMin": 0
        },
        "headers": {
            "gray_df_token": "94dc4e29e52c4548a3e5517714ae2f55175352cb3f7"

        },
        "form": "json",
        "method": "post"
    }

    with open("./apiYaml/v2_streamer_collect-list.yaml","w") as f:
        yaml.safe_dump(data=data, stream=f)
