from bs4 import BeautifulSoup

from lib.spider.base_spider import *
from lib.zone.area import *

detail = 'https://cq.lianjia.com/ershoufang/106107212059.html'

headers = create_headers()
BaseSpider.random_delay()
response = requests.get(detail, timeout=10, headers=headers)
html = response.content
soup = BeautifulSoup(html, "lxml")

# # 获得小区基本信息
# house_introduction = soup.find_all('div', id='introduction')
# # 基本信息-基本属性
# base_info = house_introduction[0].find('div', class_='base')
# base_info_elements = base_info.find_all('li')
# for element in base_info_elements:
#     print("************")
#     result = element.text
#     print(result[0:4] + ":" + result[4:])
#
# # 基本信息-交易属性
# base_deal = house_introduction[0].find('div', class_='transaction')
# base_deal_elements = base_deal.find_all('li')
# for element in base_deal_elements:
#     print("************")
#     result = element.text.replace(" ", "").replace("\n", "").strip()
#     print(result[0:4] + ":" + result[4:])
#
# # 房源特色
# house_special = soup.find_all('div', class_='introContent showbasemore')
# # print(house_special[0].text)
# house_special_elements = house_special[0].find_all('div', class_='baseattribute clear')
# for element in house_special_elements:
#     print("************")
#     result = element.text.replace(" ", "").replace("\n", "").strip()
#     print(result[0:4] + ":" + result[4:])

# # 房源照片
# house_pic = soup.find_all('div', class_='content-wrapper housePic')
# # print(house_pic[0].text)
# house_pic_list = house_pic[0].find('div', class_='list')
# house_pic_name_elements = house_pic_list.find_all('span')
# house_pic_src_elements = house_pic_list.find_all('img')
# for index in range(len(house_pic_src_elements)):
#     print("************")
#     print(house_pic_name_elements[index].text + ":" + house_pic_src_elements[index].get('src'))

# 小区信息
house_community = soup.find_all('div', class_='communityName')
house_community_detail = house_community[0].find_all('a')
print(house_community_detail[0].get('href'))