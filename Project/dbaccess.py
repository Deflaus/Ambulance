# -*- coding: utf-8 -*-
import sqlite3


class DataBaseAccess:
    db = "Ambulance.db"

    @staticmethod
    def insert_call(date, cause, address, priority):
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('INSERT INTO calls VALUES("' + date + '","' + cause + '","' + address + '",' + priority + ') ')
            con.commit()
        except:
            pass
        finally:
            cur.close()
            con.close()

    @staticmethod
    def count_of_calls():
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('SELECT COUNT(*) FROM calls')
            data = cur.fetchall()
        except:
            pass
        finally:
            cur.close()
            con.close()
            return data[0][0]

    @staticmethod
    def parse_alldata_calls():
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('SELECT * FROM calls')

            data = cur.fetchall()
        except:
            pass
        finally:
            cur.close()
            con.close()

            return data

    @staticmethod
    def parse_alldata_addresses():
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('SELECT * FROM addresses')

            data = cur.fetchall()
        except:
            pass
        finally:
            cur.close()
            con.close()

            return data

    @staticmethod
    def parse_alldata_distance():
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('SELECT * FROM distance')

            data = cur.fetchall()
        except:
            pass
        finally:
            cur.close()
            con.close()

            return data

    @staticmethod
    def parse_alldata_brigade():
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('SELECT * FROM brigade')

            data = cur.fetchall()
        except:
            pass
        finally:
            cur.close()
            con.close()

            return data

    @staticmethod
    def swap_address_brigade(number, oldAdd, newAdd):
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('DELETE FROM brigade WHERE AddressOfBrig = "' + str(oldAdd) + '"')
            con.commit()
        except:
            pass
        finally:
            cur.close()
            con.close()

            DataBaseAccess.insert_brigade(number, newAdd)


    @staticmethod
    def insert_brigade(number, add):
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()
            print(number)
            print(add)
            cur.execute('INSERT INTO brigade VALUES( ' + str(number) + ', "' + str(add) + '")')
        except:
            pass
        finally:
            con.commit()

            cur.close()
            con.close()
