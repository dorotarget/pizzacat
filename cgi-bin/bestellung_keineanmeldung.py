#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *


class Bestellung_aufgeben:
    def __init__(self):
         self.bestellung_id = -1 # besser: "Magic Number", zu faul :-O -> zugunsten Parameter-Aufruf keine globale Variable...
         self.kunde_id = -1 # Konvention
         self.adresse_id=""
         self.vorname = ""
         self.nachname=""
         self.strasse=""
         self.hausnummer=""
         self.postleitzahl=""
         self.ort=""

    def bestellung_auswerten(self):
        form = cgi.FieldStorage()
        zeilen_formular_anzahl = int(form["number_of_rows"].value)
        if "kundeId" in form:
            self.kunde_id = form["kundeId"].value

        db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
        query_db = ("USE pizzastars")
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        # -1 Konvention für noch nicht ermittelten Wert
        query_bestellung_anlegen = ("insert into bestellung (kunde_id) Values ("+str(self.kunde_id)+")")
        db_cursor.execute(query_bestellung_anlegen)
        db_connection_pizzastars.commit()
        aktuelle_bestellung_id = db_cursor.lastrowid
        # query_bestellzeile_einfuegen = ("")
        #kunde_id=self.kunde_id

        for r in range(1,zeilen_formular_anzahl+1):    # for each row...
            pizza_id = form["pizzaId"+ str(r)].value
            einzelpreis = form["preis"+ str(r)].value
            anzahl = form["anzahl"+ str(r)].value

            if anzahl == '0':
                continue

            try:
                query_insert_bestellungszeile = "insert into wird_bestellt (bestellung_id, pizza_id, anzahl, einzelpreis) Values ('"+str(aktuelle_bestellung_id)+"','"+str(pizza_id)+"','"+str(anzahl)+"','"+str(einzelpreis)+"')"
                db_cursor.execute(query_insert_bestellungszeile)
                db_connection_pizzastars.commit()
            except Exception as e:
                print( "Fehler: "+e)
                # cursor_pizza.execute("create table pizza (pizza_id int not null auto_increment primary key, name varchar, groesze int, beschreibung varchar, preis double not null)")
                continue

        # TODO hier insert in die Datenbank
        # check https://stackoverflow.com/questions/2548493/how-do-i-get-the-id-after-insert-into-mysql-database-with-python
        # connection.insert_id()
        # close db!
        db_connection_pizzastars.close()
        self.ausgabe_bestellung(aktuelle_bestellung_id)

    def ausgabe_bestellung(self, aktuelle_bestellung_id):
        # TODO SELECT bestellung und ausgeben (wie pizzaliste) mit self.bestellungsid
        db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
        query_db = ("USE pizzastars")
        query_bestellung = ("SELECT pizza.name, pizza.pizza_id, pizza.einzelpreis, wird_bestellt.anzahl FROM wird_bestellt, bestellung, pizza WHERE bestellung.bestellung_id="+str(aktuelle_bestellung_id)+" AND pizza.pizza_id=wird_bestellt.pizza_id AND bestellung.bestellung_id=wird_bestellt.bestellung_id")
        print ("Content-Type: text/html")
        print()
        print('<!DOCTYPE html>')
        print("""<?xml version="1.0" ?>
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>


                <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/normalize.css"/>
                <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/grid.css">
                <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.css">
                <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/resources/css/style.css">
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
                                    <li><a href="#">Home </a></li>
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

                <section class="section-menü">
                    <div class="row">
                    <table>
                        <th>Pizzaname</th>
                        <th>Anzahl</th>
                        <th>Zwischensumme</th>
                        <th>Beschreibung</th>
                        <th>Einzelpreis</th>""")
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        db_cursor.execute(query_bestellung)
        zeile_bestellung=""
        i=0
        bestellung_summe=0.0
        for(name, pizza_id, einzelpreis, anzahl) in db_cursor:
            i += 1
            converted_pizza_id = str(pizza_id)
            converted_einzelpreis = "{0:.2f}".format(einzelpreis)
            zwischensumme_wert=einzelpreis*anzahl
            bestellung_summe += zwischensumme_wert
            zwischensumme_ergebnis= "{0:.2f}".format(zwischensumme_wert)
            zeile_bestellung='<tr><td>'+converted_pizza_id+'</td><td>'+name+'</td><td>'+str(anzahl)+'</td><td>'+converted_einzelpreis+'</td><td>'+zwischensumme_ergebnis+'</td></tr>'
            print(zeile_bestellung)
        converted_bestellung_summe = "{0:.2f}".format(bestellung_summe)
        print("""
                <tr>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td>&nbsp;</td>
                    <td class="gesamtsummebox">""")
        print('<div class="gesamtsumme">Gesamtsumme: '+converted_bestellung_summe+'</div></td>')
        print("""
                </tr>
            </table>
            </div>

            <form>
                    <div class="row">


                            <label>&nbsp;</label>
                        <div class="button-block-2">""")
        """print('<form action="http://localhost:8888/cgi-bin/listebestellung.py">\
                                                <input type="submit" value="Senden">\
                                                    <input type="hidden" id="kundeId" name="kundeId" value="'+str(self.kunde_id)+'">\
                                                        <input type="hidden" id="adresseId" name="adresseId" value="'+str(self.adresse_id)+'">\
                            </form>')"""
        print("""
                            <a class="btn btn-full" href="http://localhost/pizzacats/bestaetigt.html">Einverstanden!</a>
                            <a class="btn btn-ghost" href="index.html">Abbrechen</a>
                        </div>
                    </div>
            </form>

        </section>""")


bestellung = Bestellung_aufgeben()
bestellung.bestellung_auswerten()
