import sqlite3

conn = sqlite3.connect('date.db')


def create_table():
    conn.execute("""
              CREATE TABLE IF NOT EXISTS users (
                  id INTEGER ,
                  заказ CHAR(50),
                  оформлен INTEGER,
                  менеджер STRING,
                  клиент CHAR(50),
                  номер тел CHAR(50),
                  доп тел номера CHAR(50),
                  дата доставки CHAR(50),
                  адрес CHAR(50),
                  состав заказа CHAR(50),
                  доставка INTEGER,
                  итого INTEGER,
                  тип оплаты STRING,
                  комментарий клиента CHAR(50),
                  комментарий оператора CHAR(50)
              )
               """)


conn.commit()
conn.close()
