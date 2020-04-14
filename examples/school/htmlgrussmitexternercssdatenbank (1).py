#!C:/Python35/python.exe
import cgi
from pymysql import *

class Formular_einlesen:
      def __init__(self):
         self.vorname=""
         self.name=""
         self.strasse=""
         self.plz=""
         self.email=""

      def db(self):
         con = connect(host="localhost", user="root", passwd="")
         cur = con.cursor()
         try:
            cur.execute("use formular")
         except (Exception):
            cur.execute("create database formular; use formular")
         while 1:
               try:
                  cur.execute("insert into personendaten (Nachname, Vorname, Adresse, Postleitzahl, EMail) Values ('"+self.name+"','"+self.vorname+"','"+self.strasse+"','"+self.plz+"','"+self.email+"')") 
                  con.commit() 
                  break
               except (Exception):
                  cur.execute("create table personendaten (PNr int not null auto_increment primary key, Nachname text, Vorname text, Adresse text, Postleitzahl text, EMail text)")
                  continue
         con.close()


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
            if "Vorname" in form:
                  self.vorname = form["Vorname"].value
            if "Name" in form:
                  self.name = form["Name"].value
            if "Strasse" in form:
                  self.strasse = form["Strasse"].value
            if "PLZ" in form:
                  self.plz = form["PLZ"].value
            if "EMail" in form:
                  self.email = form["EMail"].value
            if  (self.vorname=="" or self.name=="" or self.strasse=="" or self.plz=="" or self.email==""):
               self.fehler()
            else:
               self.ausgabe()
      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
                  <title>Anmeldung erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                  </head>\
                  <body>\
                  <h1>Herzlich willkommen, '+self.vorname+' '+self.name+' !</h1>\
                  <p><div class = "text">Hier sind ihre Daten : '+self.vorname+' '+self.name+', '+self.strasse+', '+self.plz+', '+self.email+'</div></p>\
                  <p>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  </p>\
                  </body>\
                  </html>')
            self.db()

objekt=Formular_einlesen()
objekt.auswertung()
