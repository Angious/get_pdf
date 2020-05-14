#-*- codeing = utf-8 -*-
#@Author: Angious
#@Time : 2020/5/4 16:53
#@File : get_jpg.py
#@Software : PyCharm

import requests

url1 = 'http://app.readoor.cn/app/bv/getBookInfo?b_id=81219&level=1&sign=O' \
       'DEyMTksNzE1MzQzMSwxNTg4NTg2NzgwLGEyMjkwNGQ5ZjUxODMyNTRlNGMyYTk4OTY0MDJiMjVh&appid=1535595605'

url2 = 'http://data2.readoor.cn/files/5904365ab9f997/pdf/5855315e46ae33/3/'
resp = requests.get(url1).json()
resp = resp['page_list_h']
print(resp)

#print(len(resp))
path = 'D:\Code\Python_project\get_pdf\img\\'

def save_file(path, file_name, data):
    file = open(path + file_name, "wb")
    file.write(data)
    file.flush()
    file.close()


for i in range(0,len(resp)):
    s = str(resp[i])
    geturl = url2 + s
    file_name = str(i+1)+'.jpg'
    data = requests.get(geturl).content
    save_file(path, file_name, data)