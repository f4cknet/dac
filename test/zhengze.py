import re

# 给定文本
text = """
"version_label": [
    "blue"
],
"db.command": [
    "select"
],
"yz.kdt_id": [
    "491391"
],
"idc": [
    "qabb"
],
   {
        "db.command": [
            "select","update"
        ],
],
            "db.command": [
            "update"
        ],
"error": [
    "false"
],

"segment_id": [
    "staff-core-0ad73139-7237858142-2d48a83c"
],
"db.name": [
    "store_sam"
]
},
"logs": [
    {
        "db.host": "rds-single0-1.qa.s.qima-inc.com:3008"
    },
    {
        "get_conn_time": "208616"
    },
    {
        "db.command": [
            "select","update"
        ],
        "db.statement": "select\n \n        `platform_tenant`,\n        `kdt_id`,\n        `admin_id`,\n        `account`,\n        `staff_no`,\n        `shop_id`,\n        `staff_id`,\n        `name`,\n        `link_phone`,\n        `status`,\n        `commercial_status`,\n        `cashier_store_id`,\n        `identity`,\n        `avatar`,\n        `thumb_avatar`,\n        `sales_role`,\n        `wecom_auth_status_self`,\n        `wecom_auth_status_third`,\n        `wecom_is_bind_yz_staff`,\n        `wecom_user_status`,\n        `wecom_mobile_is_synced`,\n        `extend_json`,\n        `operator`,\n        `operator_id`,\n        `create_time`,\n        `update_time`\n \n        from\n \n        staff\n \n         WHERE staff.platform_tenant=?\n \n            and `kdt_id`=?\n \n \n \n \n                and `admin_id` in\n                (\n                    ?\n                )\n \n \n \n \n \n \n                and `status` in\n                (\n                    ?\n                ,\n                    ?\n                ,\n                    ?\n                ,\n                    ?\n                )\n \n \n                and `identity` in\n                (\n                    ?\n                ,\n                    ?\n                ,\n                    ?\n                ,\n                    ?\n                ,\n                    ?\n                )"
    },
            "db.command": [
            "update"
        ],
    {
        "db.params": "491391,8102418709,0,1,2,3,1,2,3,4,5"
    }
],
"startTimeNano": 1699257938782338185,
"durationNano": 10193659,
"bizTags": [
    "yz.kdt_id:491391"
]
"""

# 使用正则表达式匹配 "db.command" 的内容
# match = re.search(r'"db\.command": \[[^\]]*"update"[^\]]*\]', text)
#
# if match:
#     result = True
# else:
#     result = False
#
# print(result)
#
# matches = re.findall(r'"db\.command": \[[^\]]*"update"[^\]]*\]', text)
#
# if matches:
#     print("匹配到的所有内容为:")
#     for match in matches:
#         print(match)
# else:
#     print("未找到匹配的内容")