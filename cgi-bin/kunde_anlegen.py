#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class kunde_anlegen:
      def __init__(self):
         self.vorname=""
         self.nachname=""
         self.email=""
         self.strasse=""
         self.hausnummer=""
         self.ort=""
         self.postleitzahl=""

      def db(self):
         db_connection = mysql.connector.connect(host="localhost", user="root", passwd="")
         cursor_pizza = db_connection.cursor()
         try:
            cursor_pizza.execute("use pizzastars")
         except (Exception):
            cursor_pizza.execute("create database pizzastars; use pizzastars")
         while 1:
               try:
                  cursor_pizza.execute("insert into kunde (vorname, nachname, email) Values ('"+self.vorname+"','"+self.nachname+"','"+self.email+"')") 
                  db_connection.commit() 
                  break
               except (Exception):
                  cursor_pizza.execute("create table kunde (kunde_id int not null auto_increment primary key, vorname varchar, nachname int, adresse int, email)")
                  continue
              # while True: 
               #     try:
                #        cursor_pizza.execute("insert adresse.adresse_id into kunde.adresse_id where '"+self.strasse+"'=kunde.strasse and '"+self.hausnummer+"'=kunde.hausnummer and '"+self.ort+"'=kunde.ort and '"+self.postleitzahl+"'=kunde.postleitzahl ") 
                 #       db_connection.commit()
                  #      break
                   # except (Exception): 
                    #    cursor_pizza.execute("insert into adresse (strasse, hausnummer, ort, postleitzahl) Values ('"+self.strasse+"','"+self.hausnummer+"','"+self.ort+"', '"+self.postleitzahl+"')") 
                     #   continue

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
            if "vorname" in form:
                  self.vorname = form["vorname"].value
            if "nachname" in form:
                  self.nachname = form["nachname"].value
            if "strasse" in form:
                  self.strasse = form["strasse"].value
            if "hausnummer" in form:
                  self.hausnummer = form["hausnummer"].value  
            if "ort" in form:
                  self.ort = form["ort"].value    
            if "postleitzahl" in form:
                  self.postleitzahl = form["postleitzahl"].value                                                
            if "email" in form:
                  self.email = form["email"].value
            if  (self.vorname=="" or self.nachname=="" or self.strasse=="" or self.hausnummer=="" or self.ort=="" or self.postleitzahl=="" or self.email==""):
               self.fehler()
            else:
               self.ausgabe()
      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
                  <title>Datenhinterlegung erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                  </head>\
                  <body>\
                  <h1>'+self.vorname+' '+self.nachname+', Sie haben erfolgreich Ihre Daten hinterlegt!</h1>\
                  <p><div class = "text">Hier sind die Personendaten: '+self.vorname+' '+self.nachname+' cm, '+self.adresse+', '+self.email+'€.</div></p>\
                  <p>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  </p>\
                  </body>\
                  </html>')
            self.db()

objekt=kunde_anlegen()
objekt.auswertung()
