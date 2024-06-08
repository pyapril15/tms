import time

import mysql.connector
from mysql.connector import Error

from data.working.common import Common


class Database:
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.last_used_time = None
        self.connection_timeout = 3600  # 1 hour
        self.connected = False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                self.last_used_time = time.time()
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
                self.cursor.execute(f"USE {self.db_name}")
                self.connected = True
        except Error as e:
            self.connected = False

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection and self.connection.is_connected():
                self.connection.close()
        except Error as e:
            pass

    def transaction_execute_query_with_and_without(self, query1: str, value1: tuple, query2: str, j_id: list):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.connection.start_transaction()
                self.cursor.execute(query1, value1)
                receipt_no = self.cursor.lastrowid
                fee_journey = [(receipt_no, value1[0], i) for i in j_id]
                self.cursor.executemany(query2, fee_journey)
                self.connection.commit()
                return True
        except Error as e:
            self.connection.rollback()
            pass
        return False

    def transaction_execute_query(self, query1: str, query2: str):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query1)
                self.cursor.execute(query2)
                self.connection.commit()
                return True
        except Error as e:
            self.connection.rollback()
            pass
        return False

    def transaction_execute_query_with_value(self, query1: str, value1: tuple, query2: str, value2: tuple):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query1, value1)
                self.cursor.execute(query2, value2)
                self.connection.commit()
                return True
        except Error as e:
            self.connection.rollback()
            pass
        return False

    def transaction_execute_with_execute_many_query(self, query1: str, value1: tuple, query2: str, value2: list):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query1, value1)
                self.cursor.executemany(query2, value2)
                self.connection.commit()
                return True
        except Error as e:
            self.connection.rollback()
            pass
        return False

    def transaction_execute_many_query(self, query1: str, value1: list, query2: str, value2: list):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.executemany(query1, value1)
                self.cursor.executemany(query2, value2)
                self.connection.commit()
                return True
        except Error as e:
            self.connection.rollback()
            pass
        return False

    def execute_query(self, query):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query)
                self.connection.commit()
                self.last_used_time = time.time()
                return True
        except Error as e:
            pass
        return False

    def execute_query_with_value(self, query, value: tuple):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query, value)
                self.connection.commit()
                self.last_used_time = time.time()
                return True
        except Error as e:
            Common.show_message(f"Error executing query: {e}", "C")
        return False

    def execute_manyquery_with_value(self, query, value: list):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.executemany(query, value)
                self.connection.commit()
                self.last_used_time = time.time()
                return True
        except Error as e:
            pass
        return False

    def fetchone_query(self, query):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query)
                return self.cursor.fetchone()
        except Error as e:
            pass
        return None

    def fetchone_query_with_value(self, query, value: tuple):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query, value)
                return self.cursor.fetchone()
        except Error as e:
            pass
        return None

    def fetchmany_query(self, query):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query)
                return self.cursor.fetchmany()
        except Error as e:
            pass
        return

    def fetchall_query(self, query):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query)
                return self.cursor.fetchall()
        except Error as e:
            pass
        return

    def fetchall_query_with_value(self, query, value: tuple):
        self.refresh_connection()
        try:
            if self.connection.is_connected():
                self.cursor.execute(query, value)
                return self.cursor.fetchall()
        except Error as e:
            pass
        return None

    def refresh_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connect()
        elif self.last_used_time and time.time() - self.last_used_time > self.connection_timeout:
            self.close()
            self.connect()
        else:
            self.last_used_time = time.time()

    def is_connected(self):
        return self.connected
