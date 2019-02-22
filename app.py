import json
from cmdb.types import get_instance

# 模拟字段保存的json字符串
jsonstr = """
{
    "type":"cmdb.types.IP",
    "value":"192.128.1.25",
    "option":{
        "prefix":"192.128."

    }
}
"""


obj = json.loads(jsonstr)
print(obj)

# 结果为 {'type': 'cmdb.types.IP', 'value': '192.168.0.1'}



print(get_instance(obj['type'], **obj['option']).stringify(obj['value']))