# -*- coding: utf-8 -*-
import sqlite3


class DataBaseAccess:
    db = "Ambulance.db"

    @staticmethod
    def insert_call(date, cause, address, priority, id, addid):
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('INSERT INTO calls VALUES("' + date + '","' + cause + '","' + address + '",' + priority + ','
                        + id + ', "' + addid + '") ')
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
    def swap_address_brigade(number, newAdd):
        try:
            con = sqlite3.connect(DataBaseAccess.db)
            cur = con.cursor()

            cur.execute('UPDATE brigade SET AddressOfBrig = "' + str(newAdd) + '" WHERE NumOfBrig = ' + str(number) + '')
            con.commit()
        except:
            pass
        finally:
            cur.close()
            con.close()