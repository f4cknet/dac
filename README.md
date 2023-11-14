## 数据操作越权检工具


    
    -data-access-control-broken
        -app/                        flask应用，当前只有一个models文件，生成数据表：result，用户存储扫描结果
        -broken_access_control/      检测主程序
            -config.py               越权检测配置文件
            -detect_senstive/        敏感数据检测（暂时用不到）
            -task/                   celery定时任务文件夹
                -celery_app.py       celer配置信息，celery应用实例
                -start_check.py      任务函数（重放函数，判断越权函数）
            -sql/                    sql相关
                -basesql.py          pymysql上下文管理封装
                -sql_dml.py          sql dml操作函数
            -dac_read_check.py       数据越权读检测（暂时用不到）
            -dac_write_check.py      数据越权写检测（流量重放）
            -extract_metalfow.py     解析流量样本相关函数
            -get_flow.py             获取存在的流量样本
            -main.py                 本地运行入口
            -request_overwrite.py    请求方法封装（封装requests.post()和requsts.put()方法、替换登陆态、在body中增加kdtId、kdt_id）
            -reset_authentication.py 重置登陆态，给request_overwrite.py中替换登陆态方法调用
            -simlar.py               判断响应内容相似度