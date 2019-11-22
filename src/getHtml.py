import requests
import lxml
from lxml import etree

html = requests.get("https://blog.csdn.net/IT_XF")
# print(html.text)

etree_html = etree.HTML(html.text)
# content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a/text()')
content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div/h4/a/text()')
for one in content:
    replace = one.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)


