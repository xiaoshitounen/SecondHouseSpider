from bs4 import BeautifulSoup

from lib.spider.base_spider import *
from lib.zone.area import *
import pymysql

# 连接数据库 并添加cursor游标
conn = pymysql.connect(host='cdb-jwotda20.cd.tencentcdb.com',port=10013,user='root',password='a123456789z',database='second_house',charset='utf8')
cursor = conn.cursor()

city_name = "cq"
area_name = "jiangbei"

page = 'https://cq.lianjia.com/ershoufang/jiangbei/pg3/'

print(page)
headers = create_headers()
BaseSpider.random_delay()
response = requests.get(page, timeout=10, headers=headers)
html = response.content
soup = BeautifulSoup(html, "lxml")

# 获得信息
house_elements = soup.find_all('li', class_="clear")
for house_elem in house_elements:
    price = house_elem.find('div', class_="totalPrice")
    unitPrice = house_elem.find('div', class_="unitPrice")
    name = house_elem.find('div', class_='title')
    url = name.find('a')
    location = house_elem.find('div', class_='flood')
    desc = house_elem.find('div', class_="houseInfo")
    pic = house_elem.find('a', class_="img").find('img', class_="lj-lazy")

    # 清理数据，获得小区信息
    price = price.text.replace("万", "").strip()
    unitPrice = unitPrice.text.replace("单价", "").replace("元/平米", "").strip()
    name = name.text.replace("\n", "").strip()
    url = url.get('href')
    location = location.text.replace(" ", "").strip()
    desc = desc.text.replace("\n", "").strip()
    pic = pic.get('data-original').strip()

    print(f"picture = {pic}, name = {name}, city = {city_name}, area = {area_name}, unit_price = {unitPrice}, price = {price}, location = {location}, description = {desc}")

    # 根据URL爬取详细信息页面
    headers = create_headers()
    BaseSpider.random_delay()
    response = requests.get(url, timeout=10, headers=headers)
    html = response.content
    soup = BeautifulSoup(html, "lxml")

    # 小区信息
    house_community = soup.find_all('div', class_='communityName')
    house_community_detail = house_community[0].find_all('a')
    community_name = house_community_detail[0].text
    community_url = "https://" + city_name + ".lianjia.com" + house_community_detail[0].get('href')
    print(f"community(name = {community_name}, url = {community_url})")

    # 数据库house_community操作表
    fetch_community = "select * from house_community"
    cursor.execute(fetch_community)
    results = cursor.fetchall()
    c_id = 0
    flag = 0
    for row in results:
        flag = 1
        row_id = row[0]
        row_name = row[1]
        if community_name == row_name:
            # 小区信息已经记录过了, 直接返回
            print("小区信息已经保存：" + str(row_id))
            c_id = row_id
            break
        else:
            # 小区信息没有记录过，插入数据
            print("小区信息没有保存，插入数据")
            insert_community = "INSERT INTO `house_community` (`name`, `url`) VALUES ('%s', '%s')" % (community_name, community_url)
            cursor.execute(insert_community)
            conn.commit()
            c_id = cursor.lastrowid
            break

    if flag == 0:
        # 小区信息没有记录过，插入数据
        print("小区信息还没有插入过")
        insert_community = "INSERT INTO `house_community` (`name`, `url`) VALUES ('%s', '%s')" % (community_name, community_url)
        cursor.execute(insert_community)
        conn.commit()
        c_id = cursor.lastrowid

    # 数据库house_message操作表
    insert_house_message = "INSERT INTO `house_message` (`picture`, `name`, `city`, `area`, `unit_price`, `price`, `location`, `description`, `c_id`) VALUES ('%s', '%s', '%s', '%s', %d, %d, '%s', '%s', %d)" % (pic, name, city_name, area_name, int(unitPrice), int(price), location, desc, c_id)
    cursor.execute(insert_house_message)
    conn.commit()
    h_id = cursor.lastrowid

    # 获得小区基本信息
    house_introduction = soup.find_all('div', id='introduction')
    # 基本信息-基本属性
    base_info = house_introduction[0].find('div', class_='base')
    base_info_elements = base_info.find_all('li')
    for element in base_info_elements:
        result = element.text
        key = result[0:4]
        value = result[4:]
        print(f"base_field(key = {key}, value = {value})")
        insert_house_base = "INSERT INTO `house_base_field` (`key`, `value`, `h_id`) VALUES ('%s', '%s', %d)" % (key, value, h_id)
        cursor.execute(insert_house_base)
        conn.commit()

    # 基本信息-交易属性
    base_deal = house_introduction[0].find('div', class_='transaction')
    base_deal_elements = base_deal.find_all('li')
    for element in base_deal_elements:
        result = element.text.replace(" ", "").replace("\n", "").strip()
        key = result[0:4]
        value = result[4:]
        print(f"business_field(key = {key}, value = {value})")
        insert_house_business = "INSERT INTO `house_business_field` (`key`, `value`, `h_id`) VALUES ('%s', '%s', %d)" % (key, value, h_id)
        cursor.execute(insert_house_business)
        conn.commit()

    # 房源特色
    house_special = soup.find_all('div', class_='introContent showbasemore')
    house_special_elements = house_special[0].find_all('div', class_='baseattribute clear')
    for element in house_special_elements:
        result = element.text.replace(" ", "").replace("\n", "").strip()
        key = result[0:4]
        value = result[4:]
        print(f"special(key = {key}, value = {value})")
        insert_house_special = "INSERT INTO `house_special` (`key`, `value`, `h_id`) VALUES ('%s', '%s', %d)" % (key, value, h_id)
        cursor.execute(insert_house_special)
        conn.commit()

    # 房源照片
    house_pic = soup.find_all('div', class_='content-wrapper housePic')
    house_pic_list = house_pic[0].find('div', class_='list')
    house_pic_name_elements = house_pic_list.find_all('span')
    house_pic_src_elements = house_pic_list.find_all('img')
    for index in range(len(house_pic_src_elements)):
        description = house_pic_name_elements[index].text
        picture = house_pic_src_elements[index].get('src')
        print(f"picture(description = {description}, picture = {picture})")
        insert_house_picture = "INSERT INTO `house_picture` (`description`, `picture`, `h_id`) VALUES ('%s', '%s', %d)" % (description, picture, h_id)
        cursor.execute(insert_house_picture)
        conn.commit()

conn.close()
cursor.close()