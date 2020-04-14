#!C:/Python35/python.exe
import cgi
from pymysql import *

class Formular_einlesen:
      def __init__(self):
            self.liste=['','','','']
            self.datenbank=""
            self.tabelle=""
            self.attribut=""
            self.wert=""
            self.ausgabe=[]

      def dbauslesen(self):
            con = connect(host="localhost", user="root", passwd="")
            cur = con.cursor()
            cur.execute("use %s" %self.datenbank)
            cur.execute("select * from %s where %s = '%s'"%(self.tabelle, self.attribut, self.wert))
            res = cur.fetchall()
            for row in res:
                  self.ausgabe.append(row)
            con.close()
            
      def fehlerausgabe(self):
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
            if "Datenbank" in form:
                  self.datenbank = form["Datenbank"].value
            if "Tabelle" in form:
                  self.tabelle = form["Tabelle"].value
            if "Attribut" in form:
                  self.attribut = form["Attribut"].value
            if "Wert" in form:
                  self.wert = form["Wert"].value
            if  (self.datenbank=="" or self.tabelle=="" or self.attribut=="" or self.wert==""):
               self.fehlerausgabe()
            else:
                  self.dbauslesen()
                  print ("Content-Type: text/html")
                  print()
                  print( '<!DOCTYPE html>')
                  print ('<head>\
                        <title>Anmeldung erfolgreich</title>\
                        <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                        </head>\
                        <body>\
                        <h1>Herzlich willkommen!</h1>\
                        <p><div class = "text">Hier sind ihre Daten : '+str(self.ausgabe[0][1])+'</div></p>\
                        <p>\
                        <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                        </p>\
                        </body>\
                        </html>')
            
objekt=Formular_einlesen()
objekt.auswertung()
