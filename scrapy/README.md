# clctn.scrapy

[toc]

## pipelines.py

一个`scrpay` `pipelines'的模版，用于快速创建`pipeline`

用法：pass

### MongoPipeline

一个MongoDB的连接与插入pipeline。

* 它从crawler中读取连个参数：MONGO_URI,MONGO_DB,用于连接MongoDB数据库。

* 在spider开始的时候，连接数据库。

* 在数据库中插入item

* 在spider结束的时候，关闭数据库连接。

用法：

    class MongoPipeline(MongoPipline):
        pass
        