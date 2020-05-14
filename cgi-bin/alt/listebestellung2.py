#!C:/Users/juerg/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
import cgi
from pymysql import *

class finalausgabe:

    def __init__(self):
        self.kunde_id=""
        self.adresse_id=""
        print("Hallo")
    def drucken(self):

        form = cgi.FieldStorage()

        if "kundeId" in form:
            self.kunde_id = form["kundeId"].value
        print ("Content-Type: text/html")
        print()
        print('<!DOCTYPE html>')
        print("""<?xml version="1.0" ?>
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>


                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/normalize.css"/>
                <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/vendors/css/grid.css">
                <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.css">
                <link rel="stylesheet" type="text/css" href="http://localhost/pizzacats/resources/css/style.css">
                <link href='https://fonts.googleapis.com/css?family=Lato:100,300,400,300italic' rel='stylesheet' type="text/css">
                <title> Pizzacats</title>
            </head>


            <body>
            """)
        print('<h1>'+str(self.kunde_id)+'</h1>')

    def kunde_in_db_suchen(self):
        db_connection_pizzastars = mysql.connector.connect(host="localhost", user="root", passwd="")
        query_db = ("USE pizzastars")
        db_cursor = db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        kunde=[]
        query_kunde_suchen = ("select adresse_id, nachname from kunde where kunde_id='"+self.kunde_id+"' ")
        db_cursor.execute(query_kunde_suchen)
        kunde=db_cursor.fetchall()
        #print(kunde)
        #print("Hallo")
        db_connection_pizzastars.commit()
        if not kunde:
                print("nicht gefunden")
        else:
                datensatz=kunde[0]
                self.adresse_id=datensatz[0]
                self.nachname=datensatz[1]
                query_adresse_suchen = ("Select strasse, hausnummer, postleitzahl, ort from adresse where adresse_id='"+str(self.adresse_id)+"' ")
                db_cursor.execute(query_adresse_suchen)
                adressliste=db_cursor.fetchall()
                adressdaten=adressliste[0]
                self.strasse=adressdaten[0]
                self.hausnummer=adressdaten[1]
                self.postleitzahl=adressdaten[2]
                self.ort=adressdaten[3]
                db_connection_pizzastars.commit()
                db_connection_pizzastars.close()



final = finalausgabe()
final.drucken()