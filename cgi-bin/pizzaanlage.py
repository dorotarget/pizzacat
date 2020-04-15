#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class Formular_einlesen:
      def __init__(self):
         self.name=""
         self.groesze=""
         self.beschreibung=""
         self.preis=""

      def db(self):
         db_connection = mysql.connector.connect(host="localhost", user="root", passwd="")
         cursor_pizza = db_connection.cursor()
         try:
            cursor_pizza.execute("use pizzastars")
         except (Exception):
            cursor_pizza.execute("create database pizzastars; use pizzastars")
         while 1:
               try:
                  cursor_pizza.execute("insert into pizza (name, groesze, beschreibung, preis) Values ('"+self.name+"','"+self.groesze+"','"+self.beschreibung+"','"+self.preis+"')") 
                  db_connection.commit() 
                  break
               except (Exception):
                  cursor_pizza.execute("create table pizza (pizza_id int not null auto_increment primary key, name varchar, groesze int, beschreibung varchar, preis double not null)")
                  continue
         db_connection.close()


      def fehler(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
               <title> Fehlermeldung </title>\
               <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
               </head>\
               <body>\
               <h1>Es ist ein Fehler aufgetreten:</h1>\
               <p>Bitte alle Felder ausf&uuml;llen!</p>\
               <p>\
               <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
               </p>\
               </body>\
               </html>')

      def auswertung(self):
            form = cgi.FieldStorage()
            if "name" in form:
                  self.name = form["name"].value
            if "groesze" in form:
                  self.groesze = form["groesze"].value
            if "beschreibung" in form:
                  self.beschreibung = form["beschreibung"].value
            if "preis" in form:
                  self.preis = form["preis"].value
            if  (self.name=="" or self.groesze=="" or self.beschreibung=="" or self.preis==""):
               self.fehler()
            else:
               self.ausgabe()
      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
                  <title>Pizzaanlage erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                  </head>\
                  <body>\
                  <h1>'+self.name+' kostet '+self.preis+' !</h1>\
                  <p><div class = "text">Hier sind die Pizzadaten: '+self.name+' '+self.groesze+' cm, '+self.beschreibung+', '+self.preis+'€.</div></p>\
                  <p>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  </p>\
                  </body>\
                  </html>')
            self.db()

objekt=Formular_einlesen()
objekt.auswertung()
