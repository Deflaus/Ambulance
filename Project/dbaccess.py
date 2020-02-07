# -*- coding: utf-8 -*-
import sqlite3


class DataBaseAccess:
    @staticmethod
    def insert_call(date, cause, address, priority):
        try:
            con = sqlite3.connect('Ambulance.db')
            cur = con.cursor()

            cur.execute('INSERT INTO calls VALUES("' + date + '","' + cause + '","' + address + '",' + priority + ') ')
            con.commit()

            cur.close()
            con.close()
        except:
            print("Данные введены неверно!")

    @staticmethod
    def parse_alldata_brigade():
        try:
            con = sqlite3.connect('Ambulance.db')
            cur = con.cursor()

            cur.execute('SELECT * FROM brigade')

            data = cur.fetchall()

            cur.close()
            con.close()

            return data
        except:
            print("Error!!!")

