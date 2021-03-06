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
            query_kunde_suchen = ("select adresse_id, nachname, kunde_id from kunde where vorname='"+self.vorname+"' and email='"+self.email+"' ")
            db_cursor.execute(query_kunde_suchen)
            kunde=db_cursor.fetchall()
            db_connection_pizzastars.commit()
            if not kunde:
                self.nicht_gefunden()
            else:
                  datensatz=kunde[0]
                  #print(datensatz)
                  self.adresse_id=datensatz[0]
                  self.nachname=datensatz[1]
                  self.kunde_id=datensatz[2]
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
                  self.ausgabe()

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
            print ("""
   <head>


        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/normalize.css"/>
        <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/grid.css">
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.css">
        <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/resources/css/style.css">
       <!-- <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/resources/css/queries.css"> -->
        <link href='https://fonts.googleapis.com/css?family=Lato:100,300,400,300italic' rel='stylesheet' type="text/css">
        <title> Fehler</title>
    </head>


    <body>
        <div class="header-einloggen">
        <header>
                <nav>
                    <div class="row">
                        <img src="http://localhost/pizzacats/resources/css/img/logo.png" alt="Pizzacats logo" class="logo2">

                        <ul class="main-nav">
                            <li><a href="http://localhost/pizzacats/index.html">Home </a></li>
                            <li><a href="http://localhost/pizzacats/ueberuns.html">Über uns </a></li>
                            <li><a href="http://localhost/pizzacats/kundenanlage.html"> Registrieren</a></li>
                            <li>
                                <form action="http://localhost:8888/cgi-bin/pizzaliste_ohnebestellung.py">
                                    <input class="input-in-nav" type="submit" value="Pizzamenü">
                                </form>
                            </li>

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

        <section class="section-unterwegs">

            <div class="row">
                <h2>Es ist ein Fehler aufgetreten!</h2>
                <p class="long-copy zentriert">
                Sie sind leider nicht in unserer Datenbank. Registrieren Sie sich bitte.<br> Oder überprüfen Sie ihre Eingabe.

                </p>

            </div>

            <label>&nbsp;</label>
            <div class="button-block-2">
                <a class="btn btn-full" href="http://localhost/pizzacats/kundenanlage.html">Registrieren</a>
                <a class="btn btn-ghost" href="http://localhost/pizzacats/einloggen.html">Neueingabe</a>
            </div>

        </section>



        </body>
</html>
    """)

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

      def ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ("""

                  <html xmlns="http://www.w3.org/1999/xhtml">
   <head>


        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
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
        <header>
            <div class="row">
                <img src="http://localhost/pizzacats/resources/css/img/logo.png" alt="Pizzacats logo" class="logo2">
            </div>

            <nav>
                <div class="row">
                    <ul class="main-nav">
                        <li><a href="http://localhost/pizzacats/index.html">Home </a></li>
                        <li><a href="http://localhost/pizzacats/bestellweiter.html">Bestellen </a></li>
                        <li><a href="http://localhost/pizzacats/kundenanlage.html"> Registrieren</a></li>
                        <li>
                            <form action="http://localhost:8888/cgi-bin/pizzaliste_ohnebestellung.py">
                                <input class="input-in-nav" type="submit" value="Pizzamenü">
                            </form>
                        </li>
                        <li><a href="http://localhost/pizzacats/ueberuns.html">Über uns </a></li>

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
            print('<p class="long-copy">'+self.vorname+' '+self.nachname+', Sie haben sich angemeldet!</p><p> Wir liefern an '+self.strasse+' '+str(self.hausnummer)+', '+str(self.postleitzahl)+', '+self.ort+'</p></div> ')
            print("""
                    <div class="row">


                            <label>&nbsp;</label>
                        <div class="button-block-2">
                            <div class="col span-1-of-2">
                                <form action="http://localhost:8888/cgi-bin/pizzaliste.py" class="contact-form">
                                <input type="submit" value="Jetzt bestellen"> """)
            print('                    <input type="hidden" id="kundeId" name="kundeId" value="'+str(self.kunde_id)+'">')
            print("""                    </form>
                            </div>
                            <div class="col span-1-of-2">
                            <a class="btn btn-ghost" href="index.html">Home</a>
                            </div>
                        </div>
                    </div>

                  </body>
                  </html>""")

kundensuche=Kunde_suchen()
kundensuche.form_validieren()
