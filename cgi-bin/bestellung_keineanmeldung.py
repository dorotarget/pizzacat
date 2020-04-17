#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *


class Bestellung_aufgeben:
    def __init__(self):
         self.bestellungsid = -1 # besser: "Magic Number", zu faul :-O
    
    def bestellung_auswerten(self):
        form = cgi.FieldStorage()

        number_of_rows = int(form["number_of_rows"].value)     # passed from form
        for r in range(1,number_of_rows+1):    # for each row...
           pizza_id = form["pizzaId"+ str(r)].value  
           preis = form["preis"+ str(r)].value
           anzahl = form["anzahl"+ str(r)].value

        # TODO hier insert in die Datenbank
        # check https://stackoverflow.com/questions/2548493/how-do-i-get-the-id-after-insert-into-mysql-database-with-python
        # connection.insert_id()
        # close db!

        self.ausgabe()

    def ausgabe(self):
        # TODO SELECT bestellung und ausgeben (wie pizzaliste) mit self.bestellungsid
        print ("Content-Type: text/html")
        print()
        print( '<!DOCTYPE html>')
        print ('<head>\
                <link rel="stylesheet" type="text/css" href="../cssclass.css"/>\
                </head>\
                <body>\
                <h2>Bestellung erfolgreich!</h2>\
                </body>\
                </html>')

bestellung = Bestellung_aufgeben()
bestellung.bestellung_auswerten()