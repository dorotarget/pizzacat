#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *


class Bestellung_aufgeben:
    def __init__(self):
         self.bestellung_id = -1 # besser: "Magic Number", zu faul :-O -> zugunsten Parameter-Aufruf keine globale Variable...
    
    def bestellung_auswerten(self):
        form = cgi.FieldStorage()
        zeilen_formular_anzahl = int(form["number_of_rows"].value)

        db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")  
        query_db = ("USE pizzastars")
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        # -1 Konvention für noch nicht ermittelten Wert
        query_bestellung_anlegen = ("insert into bestellung (kunde_id, adresse_id, bestellsumme) Values (-1, -1, -1)")
        db_cursor.execute(query_bestellung_anlegen)
        db_connection_pizzastars.commit()
        aktuelle_bestellung_id = db_cursor.lastrowid
        # query_bestellzeile_einfuegen = ("")

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
        print('<head><title>Ihre Bestellung</title></head>\
                <body>\
                    <table>\
                    <th>Nr.</th><th>Pizzanummer</th><th>Pizzaname</th><th>Anzahl</th><th>Einzelpreis</th><th>Zwischensumme</th>')
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
            zeile_bestellung='<tr><td>'+str(i)+'</td><td>'+converted_pizza_id+'</td><td>'+name+'</td><td>'+str(anzahl)+'</td><td>'+converted_einzelpreis+'</td><td>'+zwischensumme_ergebnis+'</td></tr>'
            print(zeile_bestellung)
        converted_bestellung_summe = "{0:.2f}".format(bestellung_summe)    
        print('<td colspan="6">Gesamtsumme: '+converted_bestellung_summe+'</td>')
        print('</table>\
            </body>')


bestellung = Bestellung_aufgeben()
bestellung.bestellung_auswerten()
