# 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#
# [
# 	[1, 82, 65535],
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]
# 请将上述内容写到 numbers.xls 文件中

import xlwt,json

with open('source/0015/city.txt','r') as f:
    data = json.load(f)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
    for index, (key, value) in enumerate(data.items()):
        sheet1.write(index, 0, key)
        sheet1.write(index, 1, value)
    workbook.save('source/0015/city.xls')