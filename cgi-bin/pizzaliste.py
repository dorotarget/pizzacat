#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class pizzaliste:
      def __init__(self):
          db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")  
      
      def pizzaliste_ausgeben(self):
        
        query_db = ("USE pizzastars")
        query_all_pizzas = ("SELECT name, groesze, beschreibung, preis FROM pizza")
        print('<html>\
              <head>\
                <title>Bitte Pizza ausw&auml;hlen</title>\
                    <\head>\
                        <body>\
                            <table>\
                                <th>Pizza</th><th>Gr&ouml;sse</th><th>Beschreibung></th><th>Preis</th><th>Anzahl</th>')
        db_cursor = self.db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        db_cursor.execute(query_all_pizzas)
        pizza_row=""
        for(name,groesze, beschreibung, preis) in db_cursor:
            converted_preis = "{:.2f}".format(2, preis)
            pizza_row='<tr> <td>'+name+'</td><td>'+groesze+'</td><td>'+beschreibung+'</td><td>'+converted_preis+'</td><td>0!</td></tr>'
            print(pizza_row)
        print('</table>\
            </body>')


"""          self.name=""
         self.groesze=""
         self.beschreibung=""
         self.preis=""

      def db(self):
         db_connection = mysql.connector.connect(host="localhost", user="root", passwd="")
         cursor_pizza = db_connection.cursor()
         try:
            cursor_pizza.execute("use pizzastars")

         while 1:
               try:
                  cursor_pizza.execute("select name from pizza") 
                  db_connection.commit() 
                  form = cgi.FieldStorage()
                  self.name = form["name"].value
               try:
                  cursor_pizza.execute("select groesze from pizza") 
                  db_connection.commit() 
                  form = cgi.FieldStorage()
                  self.groesze = form["groesze"].value
               try:
                  cursor_pizza.execute("select beschreibung from pizza") 
                  db_connection.commit() 
                  form = cgi.FieldStorage()
                  self.beschreibung = form["beschreibung"].value
               try:
                  cursor_pizza.execute("select preis from pizza") 
                  db_connection.commit() 
                  form = cgi.FieldStorage()
                  self.preis = form["preis"].value
               try:
                  cursor_pizza.execute("select pizza_id from pizza") 
                  db_connection.commit() 
                  form = cgi.FieldStorage()
                  self.pizza_id = form["pizza_id"].value                          
                  
                  continue
         db_connection.close()




      def pizzaliste_ausgabe(self):
            print ("Content-Type: text/html")
            print()
            print( '<!DOCTYPE html>')
            print ('<head>\
                  <title>Pizzaanlage erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                  </head>\
                  <body>\
                  <h1>'+self.name+' kostet '+self.preis+' !</h1>\
                  <p><div class = "text">Hier sind die Pizzadaten: '+self.name+' '+self.groesze+' cm, '+self.beschreibung+', '+self.preis+'€.</div></p>\
                  <p>\
                  <h1>einfache Tabelle</h1>\
                <table>\
                <tr>\
                    <input type="checkbox" id="pizza_select" name="pizza_select" value="'+self.pizza_id+'">\
                    <br>\
                </tr>\
                <tr>\
                    <th>'+self.name+'</th>\
                </tr>\
                <tr>\
                    <td>'+self.groesze+'</td>\
                </tr>\
                <tr>\
                    <td>'+self.beschreibung+'</td>\
                </tr>\
                <tr>\
                    <td>'+self.preis+'</td>\
                </tr>\
                </table>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  </p>\
                  </body>\
                  </html>'
                  )
            self.db() """

 
objekt=pizzaliste()
objekt.pizzaliste_auswertung()



