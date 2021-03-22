# conding=utf-8
import pymysql
# 连接数据库 并添加cursor游标
conn = pymysql.connect(host='cdb-jwotda20.cd.tencentcdb.com',port=10013,user='root',password='a123456789z',database='second_house_cq',charset='utf8')
cursor = conn.cursor()

# house_message: insert
pic = "pic"
name = "测试"
city_name = "cq"
area_name = "yubei"
unitPrice = 100
price = 1000
location = "位置"
desc = "描述"
c_name = "小区"
c_url = "http"
insert_house_message = "INSERT INTO `house_message` (`picture`, `name`, `city`, `area`, `unit_price`, `price`, `location`, `description`, `community_name`, `community_url`) VALUES ('%s', '%s', '%s', '%s', %d, %d, '%s', '%s', '%s', '%s')" % (pic, name, city_name, area_name, unitPrice, price, location, desc, c_name, c_url)
print(insert_house_message)
cursor.execute(insert_house_message)
conn.commit()

# house_base_field: insert
# key = "key"
# value = "value"
# h_id = 1
# insert_house_base = "INSERT INTO `house_base_field` (`key`, `value`, `h_id`) VALUES ('%s', '%s', %d)" % (key, value, h_id)
# print(insert_house_base)
# cursor.execute(insert_house_base)
# conn.commit()

# house_business_field: insert
# key = "key"
# value = "value"
# h_id = 1
# insert_house_business = "INSERT INTO `house_business_field` (`key`, `value`, `h_id`) VALUES ('%s', '%s', %d)" % (key, value, h_id)
# print(insert_house_business)
# cursor.execute(insert_house_business)
# conn.commit()

# house_special: insert
# key = "key"
# value = "value"
# h_id = 1
# insert_house_special = "INSERT INTO `house_special` (`key`, `value`, `h_id`) VALUES ('%s', '%s', %d)" % (key, value, h_id)
# print(insert_house_special)
# cursor.execute(insert_house_special)
# conn.commit()

# house_picture: insert
# description = "描述"
# picture = "图片"
# h_id = 1
# insert_house_picture = "INSERT INTO `house_picture` (`description`, `picture`, `h_id`) VALUES ('%s', '%s', %d)" % (description, picture, h_id)
# print(insert_house_picture)
# cursor.execute(insert_house_picture)
# conn.commit()

conn.close()
cursor.close()