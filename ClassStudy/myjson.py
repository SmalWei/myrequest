import os.path
##  将文件写入到json字符串中去
# import json
# dic1 = {1:1,2:2,3:"段伟"}
#
# with open("test.json", "a+", encoding='utf-8') as f:
#     # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
#     json.dump(dic1, f, indent=4,ensure_ascii=False)

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir,'123.txt')
print(path)