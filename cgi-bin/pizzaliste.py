#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class Pizzaliste:
      def __init__(self):
        self.kunde_id=-1

      def pizzaliste_ausgeben(self):
        form = cgi.FieldStorage()
        if "kundeId" in form:
              self.kunde_id = form["kundeId"].value
        db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
        query_db = ("USE pizzastars")
        query_all_pizzas = ("SELECT pizza_id, name, groesze, beschreibung, einzelpreis FROM pizza")
        print ("Content-Type: text/html")
        print()
        print('<!DOCTYPE html>')
        print('<head><title>Bitte Pizza ausw&auml;hlen</title></head>\
                <body><form action="http://localhost:8888/cgi-bin/bestellung_keineanmeldung.py">\<section class="section-menü">\
            <div class="row">\
                    <table>\
                    <th>Nr.</th><th>Pizza</th><th>Gr&ouml;sse</th><th>Beschreibung</th><th>Preis</th><th>Anzahl</th>')
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        db_cursor.execute(query_all_pizzas)
        pizza_row=""
        i = 0
        converted_iterator = ""
        for(pizza_id, name, groesze, beschreibung, einzelpreis) in db_cursor:
            i += 1
            converted_iterator = str(i)
            converted_pizza_id = str(pizza_id)
            converted_einzelpreis = "{0:.2f}".format(einzelpreis)
           # converted_einzelpreis = str(round(einzelpreis, 2))
           # <tr> <td>Pizza Quatro Formaggi vegan</td><td>24</td><td>mit veganem Cheddar, Parmesan, Gorgonzola und Mozzarella</td><td>2.00</td><td><input id="anzahl4" type="number" name="anzahl4" min="0" max="225" step="1" value="0"></td></tr>


            pizza_row='<tr><td><input type="hidden" id="pizzaId'+converted_iterator+'" name="pizzaId'+converted_iterator+'" value="'+converted_pizza_id+'"><input type="hidden" id="preis'+converted_iterator+'" name="preis'+converted_iterator+'" value="'+converted_einzelpreis+'">'+converted_pizza_id+'</td>\
              <td>'+name+'</td>\
                <td>'+groesze+'</td>\
                  <td>'+beschreibung+'</td>\
                    <td>'+converted_einzelpreis+'</td>\
                      <td><input id="anzahl'+converted_iterator+'" type="number" name="anzahl'+converted_iterator+'" min="0" max="225" step="1" value="0"></td></tr>'
           # pizza_row='<tr><td>'+converted_pizza_id+'</td><td>'+name+'</td><td>'+groesze+'</td><td>'+beschreibung+'</td><td>'+converted_einzelpreis+'</td><td>0!</td></tr>'
            print(pizza_row)
        print('</table><p><input type="hidden" id="kundeId" name="kundeId" value="'+str(self.kunde_id)+'">\
          <input type="hidden" name="number_of_rows" value="'+converted_iterator+'">\
            <input type="submit" value="Absenden"><input type="reset" value="Zur&uuml;cksetzen"></p>\
              </form>\
                </div></section></body>')

objekt=Pizzaliste()
objekt.pizzaliste_ausgeben()



