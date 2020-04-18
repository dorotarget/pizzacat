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
         self.adresse_id = -1 # Konvention

      def kunde_in_db_einfuegen(self):
            db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")  
            query_db = ("USE pizzastars")
            db_cursor = db_connection_pizzastars.cursor()
            db_cursor.execute(query_db)
            query_adresse_einfuegen = "insert into adresse (strasse, hausnummer, postleitzahl, ort) Values ('"+self.strasse+"','"+self.postleitzahl+"','"+self.hausnummer+"','"+self.ort+"')"
            db_connection_pizzastars.commit()
            self.adresse_id = db_cursor.lastrowid
            query_kunde_einfuegen = "insert into kunde (vorname, nachname, adresse_id,email) Values ('"+self.vorname+"','"+self.nachname+"','"+self.adresse_id+"','"+self.email+"')"
            db_cursor.execute(query_kunde_einfuegen) 
            db_connection_pizzastars.commit() 
            db_connection_pizzastars.close()

      def fehler_ausgeben(self):
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

      def form_validieren(self):
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
               self.fehler_ausgeben()
            else:
               self.kunde_in_db_einfuegen()
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
            

objekt=kunde_anlegen()
objekt.form_validieren()
