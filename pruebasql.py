import datetime
import requests
from datetime import date, timedelta
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from rasa_sdk.events import AllSlotsReset
import mysql.connector
import pymysql
global SiPaga
global NoPaga
global razon
global tipo_contacto
global compromiso_p
global derivacion
global fecha_com
global entrega_info
SiPaga=None
NoPaga=None
razon=None
tipo_contacto=None
compromiso_p=None
derivacion=None
fecha_com=None
entrega_info=None
class DataBase:
    def __init__(self):
        self.connection=pymysql.connect(host='172.16.1.141',
                             user='cron',
                             password='T3c4dmin1234.',
                             database='asterisk',
                             )
        self.cursor = self.connection.cursor()
        print("Conexion exitosa!")

    def select_user(self, uniqueid):
        sql = "select T0.vendor_lead_code, T0.first_name,T0.address1,T0.lead_id,T0.address2,T0.city,T0.owner,T1.list_name,T0.email,T2.campaign_name from vicidial_list_archive T0 inner join vicidial_lists T1 on T0.list_id=T1.list_id inner join vicidial_campaigns T2 on T1.campaign_id=T2.campaign_id where T0.lead_id ='{}' union ALL select T0.vendor_lead_code, T0.first_name,T0.address1,T0.lead_id,T0.address2,T0.city,T0.owner,T1.list_name,T0.email,T2.campaign_name  from vicidial_list T0 inner join vicidial_lists T1 on T0.list_id=T1.list_id inner join vicidial_campaigns T2 on T1.campaign_id=T2.campaign_id where T0.lead_id ='{}'".format(uniqueid,uniqueid)
        
        try:

            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print(user)
            #global monto
            #global nombre
            #global fechaVencimiento
            #global Campania
            #global oferta
            #global primernombre
            #print("user:",user)
            #primernombre = user[1]
            #monto = user[4]
            #nombre = user[2]
            #fechaVencimiento = user[5]
            #Campania = user[9]
            #oferta = user[8]
            """
            global monto
            global nombre
            global fechaVencimiento
            monto = user[3]
            nombre = user[2]
            fechaVencimiento = user[5]
            Campania = user[8]
            #print("user: ", user)
            print("Rut:" , user[0])
            print("Nombre:" , nombre)
            print("Deuda monto:" , monto)
            print("fecha Vencimiento: " , fechaVencimiento)
            print("Campaña: ", Campania)
            """             
        except Exception as e:
            raise

    def select_all_users(self):
        sql = 'SELECT id, rut, name, email FROM usuarios'
        
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            print(users)
            for user in users:      
                  print("Id:" , user[0])
                  print("rut:" , user[1])
                  print("name:" , user[2])
                  print("fecha-vencimiento: " , user[5])
                 
        except Exception as e:
            raise

    def update_user(self,tipo_contacto,razon,compromiso_p,derivacion,fecha_com,entrega_info,uniqueid):
        sql = "UPDATE bot_movatec SET tipo_contacto='{}',motivo='{}',compromiso_p='{}',derivacion='{}',fecha_com='{}',entrega_info='{}' WHERE lead_id='{}'".format(tipo_contacto,razon,compromiso_p,derivacion,fecha_com,entrega_info,uniqueid)
       # sql = "UPDATE usuarios SET name='{}' WHERE id = {}".format(name,id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 
    def call_resultado(self,uniqueid):
        sql = "SELECT * from bot_movatec where lead_id='{}'".format(uniqueid)
       # sql = "UPDATE usuarios SET name='{}' WHERE id = {}".format(name,id)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            #users = self.cursor.fetchall()
            print("user: ",user)
            #print("user2: ",users)
            #print(uniqueid)
            #print(Razón)
        except Exception as e:
            raise 
    def tipo_contacto(self,uniqueid):
        sql = "SELECT tipo_contacto, max(fecha_llamada) from bot_movatec where lead_id='{}'".format(uniqueid)
       # sql = "UPDATE usuarios SET name='{}' WHERE id = {}".format(name,id)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            users = self.cursor.fetchall()
            print("user: ",user)
            print("user2: ",users)
            #print(uniqueid)
            #print(Razón)
        except Exception as e:
            raise 
    def close(self):
        try:
            self.connection.close()
            print("Sesion cerrada exitosamente!")
            #agi.verbose("Database cerrada exitosamente!")
        except Exception as e:
            raise

database = DataBase()
#today_date = date.today()
#print("Dia de hoy : ", today_date)
#td = timedelta(3)
#fechaPago=(today_date + td)
#print(fechaPago)
database.select_user(134)
#razon="Enfermo"
#database.update_user(3,razon,3,"Si",fechaPago,"Si",93)
#database.update_user(3,razon,3,"Si",fechaPago,"Si",531861)
#print("nombre .. :",nombre)
#print("monto .. :",monto)

#Razón = "estoy enfermo"
#uniqueid = 499082
#database.update_user(3,razon,3,uniqueid)
#database.call_resultado(93)
#database.update_user(3,"sin plata",3,"Si",None,"No",565409)




database.close()
