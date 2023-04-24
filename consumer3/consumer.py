#!/usr/bin/env python
import pika
import sys
import json
import ast
import mysql.connector

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.21.0.2'))
channel = connection.channel()

# channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

channel.queue_declare(queue='requestqueue2')
# queue_name = result.method.queue

# channel.queue_bind(
        # exchange='direct_logs', queue=queue_name, routing_key="requestqueue")

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    mydb = mysql.connector.connect(
  host="172.21.0.3",
  user="root",
  password="ary123",
  database="Ccproject"
)
    c = mydb.cursor()
    # c.execute("insert into students values('man','r','t')")
    c.execute("select * from students")
    f=c.fetchall()
    # print(c.fetchall())
    # print(properties.correlation_id)
    # print(properties.reply_to)
    ch.basic_publish('',routing_key=properties.reply_to,body=json.dumps(f))
    print("ack sent")
    mydb.commit()
    #insert into dbms


channel.basic_consume('requestqueue2',on_message_callback=callback)

channel.start_consuming()
