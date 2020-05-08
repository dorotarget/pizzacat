#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class Kunde_suchen:
      def __init__(self):
            self.vorname=""
            self.nachname=""
            self.email=""
            self.adresse_id=""
            self.strasse=""
            self.hausnummer=""
            self.ort=""
            self.postleitzahl=""
            self.adresse_id = -1 # Konvention: nicht gesetzt
            self.kunde_id = -1 # Konvention

      def kunde_in_db_suchen(self):
            db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
            query_db = ("USE pizzastars")
            db_cursor = db_connection_pizzastars.cursor()
            db_cursor.execute(query_db)
            kunde=[]
            query_kunde_suchen = ("select adresse_id, nachname from kunde where vorname='"+self.vorname+"' and email='"+self.email+"' ")
            db_cursor.execute(query_kunde_suchen)
            kunde=db_cursor.fetchall()
            #print(kunde)
            #print("Hallo")
            db_connection_pizzastars.commit()
            if not kunde:
                  #print("hallo")
                  nicht_gefunden()
            else:
                  datensatz=kunde[0]
                  #print(datensatz)
                  self.adresse_id=datensatz[0]
                  self.nachname=datensatz[1]
                  #print(self.adresse_id)
                  query_adresse_suchen = ("Select strasse, hausnummer, postleitzahl, ort from adresse where adresse_id='"+str(self.adresse_id)+"' ")
                  db_cursor.execute(query_adresse_suchen)
                  adressliste=db_cursor.fetchall()
                  adressdaten=adressliste[0]
                  #print(adressdaten)
                  self.strasse=adressdaten[0]
                  self.hausnummer=adressdaten[1]
                  self.postleitzahl=adressdaten[2]
                  self.ort=adressdaten[3]
                  #print(self.strasse)
                  #print(self.hausnummer)
                  #print(self.postleitzahl)
                  #print(self.ort)
                  db_connection_pizzastars.commit()
                  #self.kunde_id = db_cursor.lastrowid
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

      def nicht_gefunden(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
               <title> Fehlermeldung </title>\
               <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
               </head>\
               <body>\
               <h1>Es ist ein Fehler aufgetreten:</h1>\
               <p>Sie sind nicht in der Datenbank. Bitte erstellen Sie einen Account!</p>\
               <p>\
               <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
               </p>\
               </body>\
               </html>')

      def form_validieren(self):
            form = cgi.FieldStorage()
            if "vorname" in form:
                  self.vorname = form["vorname"].value
            if "email" in form:
                  self.email = form["email"].value
            if  (self.vorname==""  or self.email==""):
               self.fehler_ausgeben()
            else:
               self.kunde_in_db_suchen()
               self.ausgabe()

      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
                  <title>Datenhinterlegung erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/style.css"/>\
                  </head>\
                  <body>\
                  <h1>'+self.vorname+' '+self.nachname+', Sie haben sich erfolgreich angemeldet!</h1>\
                  <p><div class = "text">Herzlich willkommen, '+self.vorname+' '+self.nachname+'</p>\
                  <p><div class = "text"> Wir liefern an '+self.strasse+' '+str(self.hausnummer)+', '+str(self.postleitzahl)+', '+self.ort+'</p>\
                  <form action="http://localhost:8888/cgi-bin/pizzaliste.py">\
                  <input type="hidden" id="kundeId" name="kundeId" value="'+str(self.kunde_id)+'">\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  <input type="submit" value="Weiter zur Bestellung" />\
                  </form>\
                  </p>\
                  </body>\
                  </html>')

kundensuche=Kunde_suchen()
kundensuche.form_validieren()
