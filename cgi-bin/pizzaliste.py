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
        print("""   <head>


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
                            <li><a href="index.html">Home </a></li>
                            <li><a href="ueberuns.html">Über uns </a></li>
                            <li><a href="kundenanlage.html"> Registrieren</a></li>
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
                   <!-- <div class="col span-1-of-2">
                        <div class="hero-button">
                            <a class="btn btn-full" href="#">Anmelden und bestellen</a>
                            <a class="btn btn-ghost" href="#">Registrieren und bestellen</a>
                        </div>
                    </div>-->
                </div>
        </header>
        </div><section class="section-menü"><form action="http://localhost:8888/cgi-bin/bestellung_keineanmeldung.py">
            <div class="row">
                    <table><th>Nr.</th><th>Pizza</th><th>Gr&ouml;sse</th><th>Beschreibung</th><th>Preis</th><th>Anzahl</th>""")
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



