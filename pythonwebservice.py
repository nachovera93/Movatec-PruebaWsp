import datetime
import requests
from datetime import date, timedelta
import pymysql


import requests
import json
url = "http://172.16.1.72/webservice-php-json/index.php"

payload={'action': 'get','id': '99'}
files=[
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)


my_bytes_value = response.content
my_new_string = my_bytes_value.decode("utf-8").replace("'", '"')
data = json.loads(my_new_string)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)

global nombre
global monto
global fecha
global primernombre
global rut
global campania
nombre=data["data"][0]["address1"]
monto=data["data"][0]["address2"]
fecha=data["data"][0]["city"]
primernombre=data["data"][0]["first_name"]
rut=data["data"][0]["vendor_lead_code"]
campania=data["data"][0]["campaign_name"]

class DataBase:
    def __init__(self):
        self.connection=pymysql.connect(host='172.16.1.13',
                             user='root',
                             password='T3c4dmin1234.',
                             database='asterisk',
                             )
        self.cursor = self.connection.cursor()
        print("Conexion exitosa!")

   
    def insert_data(self,primernombre,nombre,monto,fecha):
        sql = "INSERT INTO `vicidial_list` VALUES ('', '2022-03-07 22:54:15', '0000-00-00 00:00:00', 'NEW', '', '170011111', '11461', 10006, -4.00, 'N', '56', '967414029', '', '{}', '', '', '{}', '{}', '', '{}', '', '', '11111111', '', '', '0000-00-00', '', '', '', '', 0, '2008-01-01 00:00:00', 0, '78574270', 0);".format(primernombre,nombre,monto,fecha)
    
        try:
            self.cursor.execute(sql)
            self.connection.commit()
           
            
        except Exception as e:
            raise 

    def close(self):
        try:
            self.connection.close()
            print("Sesion cerrada exitosamente!")
        except Exception as e:
            raise

database = DataBase()
database.insert_data(primernombre,nombre,monto,fecha)
database.close()





