#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class Pizzaliste:
      def __init__(self):
        self.the_one="1"

      def pizzaliste_ausgeben(self):
        db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
        query_db = ("USE pizzastars")
        query_all_pizzas = ("SELECT pizza_id, name, groesze, beschreibung, einzelpreis FROM pizza")
        print ("Content-Type: text/html")
        print()
        print('<!DOCTYPE html>')
        print('<head><title>Unsere Pizzen</title><link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/cssclass2.css"/></head><div id="container">\
          <div class="header">Hallo</div>\<div class="sidebar"><form action="http://localhost:8888/cgi-bin/pizzaliste_ohnebestellung.py"><input type="submit" value="Pizzakarte" /></form><a href="">Pizzaquiz</a><a href="kontakt.html">Kontakt</a><a href="wissenswertes.html">Wissenswertes über Pizza</a></div>\
            <div id="content"><nav>\
      <button class="button button1" onclick="window.location.href='"bestellung_keineanmeldung.html"'">Bestellung ohne Anmeldung</button><button class="button button2" onclick="window.location.href='"kunde_anlegen.html"'">Registrieren</button><button class="button button1" onclick="window.location.href='"einloggen.html"'">Anmelden und bestellen</button>\
      </nav><body>\
                    <table><th>Pizza</th><th>Gr&ouml;sse</th><th>Beschreibung</th><th>Preis</th>')
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        db_cursor.execute(query_all_pizzas)
        pizza_row=""
        for(pizza_id, name, groesze, beschreibung, einzelpreis) in db_cursor:
            converted_pizza_id = str(pizza_id)
            converted_einzelpreis = "{:.2f}".format(2, einzelpreis)
            pizza_row='<tr><td>'+converted_pizza_id+'</td><td>'+name+'</td><td>'+groesze+'</td><td>'+beschreibung+'</td><td>'+converted_einzelpreis+'</td></tr>'
            print(pizza_row)
        print('</table>\
            </body><div class="footer">flkdsrgn</div></div>')

objekt=Pizzaliste()
objekt.pizzaliste_ausgeben()
