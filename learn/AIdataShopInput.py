# 批量收录店铺，字段漏爬店铺统计
# 注意事项：该脚本是基于所有店铺已爬取店铺进行统计。若统计Q4新增收录，可自由编辑sql(例如添加时间筛选条件等)

import pymysql
from loguru import logger


def checkData():
    # 数据库连接
    db = pymysql.Connect(
        host='rm-bp1i0eqq1p7jzd9j2188.mysql.rds.aliyuncs.com',
        port=3306,
        user='j',  # 数据库账号
        password='J',  # 数据库密码
        db='spider',  # 库名
        charset='utf8mb4'
    )

    cur = db.cursor()

    try:
        sql = "select count(id),count(id)-count(shop_id),count(id)-count(shop_name),count(id)-count(seller_id),count(id)-count(seller_name)\
            ,count(id)-count(shop_url),count(id)-count(shop_icon),count(id)-count(main_industry),count(id)-count(rate_url),count(id)-count(main_ratio)\
                ,count(id)-count(seller_credit),count(id)-count(deposit),count(id)-count(from_place),count(id)-count(good_rate),count(id)-count(describe_info)\
                    ,count(id)-count(fans_num),count(id)-count(phone),count(id)-count(ifashion),count(id)-count(shop_tags),count(id)-count(credit_level)\
                        ,count(id)-count(item_num),count(id)-count(item_id),count(id)-count(shop_type),count(id)-count(start_time)\
                             from tb_shop_info \
                                 where status = 1"
        cur.execute(sql)
        res = cur.fetchall()[0]
        llist = ["总店铺未", "店铺id", "店铺名称", "旺旺id", "旺旺名称", "店铺url", "店铺logo", "主营行业", "rate 链接", "行业占比", "卖家信用", "保证金额",
                 "所在地", "店铺好评率" \
            , "宝贝、物流、态度描述", "店铺粉丝数", "店铺服务电话", "ifashion店铺", "店铺标签", "店铺等级", "店铺商品总量", "店铺其中一个商品id", "店铺类型", "开店时间"]
        for i in range(len(llist)):
            logger.info("{}缺失数:{}", llist[i], res[i])


    except Exception:
        logger.info('异常')

    db.close()


if __name__ == "__main__":
    checkData()


