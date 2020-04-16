import unittest
import mysql.connector


class DbTest(unittest.TestCase):
    def setUp(self): 
        self.db_connection_pizzastars = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        print(self.db_connection_pizzastars)
        return super().setUp()

    def test_db_connected(self):
        self.assertTrue(self.db_connection_pizzastars.is_connected)

    def test_table_pizza_exist(self):
        query_db = ("USE pizzastars")
        query_all_pizzas = ("SELECT * FROM pizza")

        db_cursor = self.db_connection_pizzastars.cursor()
        db_cursor.execute(query_db)
        db_cursor.execute(query_all_pizzas)
        db_cursor.fetchall()
        pizza_rowcount = db_cursor.rowcount
        self.assertTrue(pizza_rowcount > 0)

        db_cursor.close

    def test_table_pizza_insert(self):
        db_cursor = self.db_connection_pizzastars.cursor()
        query_db = ("USE pizzastars")
        query_insert_pizza = ("insert into pizza (name, groesze, beschreibung, preis) Values ('vegane Thunfischpizza', '24', 'mit Tomate','8.70')")

        try:
            db_cursor.execute(query_db)
        except (Exception):
            print("Fehler: kann mich nicht verbinden")
        while 1:
            try:
                db_cursor.execute(query_insert_pizza) 
                self.db_connection_pizzastars.commit() 
                break
            except (Exception):
                print("Fehler: kann keine Zeile in Tabelle Pizza hinzufügen")
                continue

    def test_table_kunde_insert(self):
        db_cursor = self.db_connection_pizzastars.cursor()
        query_db = ("USE pizzastars")
        query_insert_kunde = ("insert into kunde (vorname, nachname, adresse_id, email) Values ('Theodor', 'Fischer', '11', 'theodor@fischer.de')")

        try:
            db_cursor.execute(query_db)
        except (Exception):
            print("Fehler: kann mich nicht verbinden")
        while 1:
            try:
                db_cursor.execute(query_insert_kunde) 
                self.db_connection_pizzastars.commit() 
                break
            except (Exception):
                print("Fehler: kann keine Zeile in Tabelle Kunde hinzufügen")
                continue   

    def test_query_pizzaliste(self):
        query_db = ("USE pizzastars")
        query_all_pizzas = ("SELECT name, groesze, beschreibung, preis FROM pizza")

        db_cursor = self.db_connection_pizzastars.cursor()
        
        db_cursor.execute(query_db)
        db_cursor.execute(query_all_pizzas)
        pizza_row=""
        for(name,groesze, beschreibung, preis) in db_cursor:
            converted_preis = "{:.2f}".format(2, preis)
            pizza_row='<tr> <td>'+name+'</td><td>'+groesze+'</td><td>'+beschreibung+'</td><td>'+converted_preis+'</td></tr>'
            print(pizza_row)
        self.assertIsNotNone(pizza_row)


    def tearDown(self):
        self.db_connection_pizzastars.close
        return super().tearDown()