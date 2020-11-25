import  yaml


def test_yaml2():
    data = [{'activityGoodsId': 3425,'sellCountNum': 1500,'sellCountIncr': 100}]

    with open("./apiYaml/test_yaml","w") as f:
        yaml.safe_dump(data=data, stream=f)
