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
                            <li><a href="#">Über uns </a></li>
                            <li><a href="#"> Registrieren</a></li>
                            <li><a href="#"> Menü</a></li>
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
        </div><section class="section-menü">\
            <div class="row">\
                    <table><th>Pizza</th><th>Gr&ouml;sse</th><th>Beschreibung</th><th>Preis</th>""")
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        db_cursor.execute(query_all_pizzas)
        pizza_row=""
        for(pizza_id, name, groesze, beschreibung, einzelpreis) in db_cursor:
            converted_pizza_id = str(pizza_id)
            converted_einzelpreis = "{:.2f}".format(einzelpreis)
            pizza_row='<tr><td>'+converted_pizza_id+'</td><td>'+name+'</td><td>'+groesze+'</td><td>'+beschreibung+'</td><td>'+converted_einzelpreis+'</td></tr>'
            print(pizza_row)
        print("""</table>\
            </div></section></body><div class="footer">flkdsrgn</div></div>""")

objekt=Pizzaliste()
objekt.pizzaliste_ausgeben()
