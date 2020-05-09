#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class Kunde_anlegen:
      def __init__(self):
         self.vorname=""
         self.nachname=""
         self.email=""
         self.strasse=""
         self.hausnummer=""
         self.ort=""
         self.postleitzahl=""
         self.adresse_id = -1 # Konvention: nicht gesetzt
         self.kunde_id = -1 # Konvention

      def kunde_in_db_einfuegen(self):
            db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
            query_db = ("USE pizzastars")
            db_cursor = db_connection_pizzastars.cursor()
            db_cursor.execute(query_db)
            query_adresse_einfuegen = "insert into adresse (strasse, hausnummer, postleitzahl, ort) Values ('"+self.strasse+"','"+str(self.postleitzahl)+"','"+str(self.hausnummer)+"','"+self.ort+"')"
            db_cursor.execute(query_adresse_einfuegen)
            db_connection_pizzastars.commit()
            self.adresse_id = db_cursor.lastrowid
            query_kunde_einfuegen = "insert into kunde (vorname, nachname, adresse_id,email) Values ('"+self.vorname+"','"+self.nachname+"','"+str(self.adresse_id)+"','"+self.email+"')"
            db_cursor.execute(query_kunde_einfuegen)
            db_connection_pizzastars.commit()
            self.kunde_id = db_cursor.lastrowid
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
            print ("""

                  <html xmlns="http://www.w3.org/1999/xhtml">
   <head>


        <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/normalize.css"/>
        <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/grid.css">
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.css">
        <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/resources/css/style.css">
       <!-- <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/resources/css/queries.css"> -->
        <link href='https://fonts.googleapis.com/css?family=Lato:100,300,400,300italic' rel='stylesheet' type="text/css">
        <title> Pizzacats</title>
    </head>


    <body>
        <div class="header-einloggen">
        <header class="header-einloggen">
                <nav>
                    <div class="row">
                        <img src="resources/img/p" alt="Omnifood logo" class="logo">

                        <ul class="main-nav">
                            <li><a href="index.html">Home</a></li>
                            <li><a href="ueberuns.html">Über uns </a></li>
                            <li>
                                <form action="http://localhost:8888/cgi-bin/pizzaliste_ohnebestellung.py">
                                    <input class="input-in-nav" type="submit" value="Pizzamenü">
                                </form>
                            </li>
                            <li><a href="#"> Pizzaquiz</a></li>

                        </ul>
                    </div>

                </nav>
                <div class="row">
                    <div class="col span-1-of-2">
                        <div class="hero-text-box">
                            <h1>Vegan. <br>Glutenfrei. <br>Italienisch.</h1>
                        </div>
                    </div>
                </div>
        </header>
        </div>


        <body>

        <section class="section-willkommen">
            <div class="row">
                <h2>Herzlich Willkommen!</h2>""")

            print('<p class="long-copy">'+self.vorname+' '+self.nachname+', Sie haben sich erfolgreich angemeldet!</p><p>Wir liefern an '+self.strasse+' '+str(self.hausnummer)+', '+str(self.postleitzahl)+', '+self.ort+'</p>')
            print("""   </div>
            <form>
                    <div class="row">


                            <label>&nbsp;</label>
                        <div class="button-block-2">
                            <div class="col span-1-of-2">
                                <form action="http://localhost:8888/cgi-bin/pizzaliste.py" class="contact-form">
                                <input type="submit" value="Jetzt bestellen">
                                <input type="hidden" id="kundeId" name="kundeId" value="'+str(self.kunde_id)+'">
                                </form>
                            </div>
                            <div class="col span-1-of-2">
                            <a class="btn btn-ghost" href="index.html">Home</a>
                            </div>
                        </div>
                    </div>

                  """)

kundenanlage=Kunde_anlegen()
kundenanlage.form_validieren()
