#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *


class Bestellung_aufgeben:
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
             form = cgi.FieldStorage()
             if "anzahl" in form:
                  self.anzahl = form[""].value
                  try:
                      cursor_pizza.execute("insert into bestellung (bestellung_id) Values ('LAST_INSERT_ID(id+1)')") 
                      db_connection.commit() 
                  break
                  #except (Exception):
                  #cursor_pizza.execute("create table bestellung_id (pizza_id int not null auto_increment primary key, name varchar, groesze int, beschreibung varchar, preis double not null)")
                  #continue
         db_connection.close()
         self.ausgabe()

      def insert_wird_bestellt(self):
          db_connection = mysql.connector.connect(host="localhost", user="root", passwd="")
          cursor_pizza = db_connection.cursor()
          try:
            cursor_pizza.execute("use pizzastars")
          while 1:
               try:
                  cursor_pizza.execute("insert into wird_bestellt (bestellung_id) Values ('LAST_INSERT_ID(id+1)')") 
                  db_connection.commit() 
                  break
               except (Exception):
                  cursor_pizza.execute("create table bestellung_id (pizza_id int not null auto_increment primary key, name varchar, groesze int, beschreibung varchar, preis double not null)")
                  continue
          db_connection.close()
          self.ausgabe()

               
      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
                  <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                  </head>\
                  <body>\
                  <form action="http://localhost:8888/cgi-bin/wird_bestellt_einfügen.py">\
                  <input type="submit" value="Ohne Anmeldung fortfahren" onclick = "history.back()" />\
                  </p>\
                  </form>\
                  </body>\
                  </html>')
            self.db()

objekt=Bestellung_aufgeben()
objekt.auswertung()

