import telebot
import sqlite3 as sq
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient,sync,events
import requests
from adhoc_config import *


if __name__=="__main__":
    con = sq.connect('tithi.db')
    cursor = con.cursor()
    cursor.execute("select tithi_date,tithi_name from Tithi_dt where tithi_date>=current_date and tithi_name in ('Aatham','Chaudas') order by tithi_date asc limit 1;")
    out = cursor.fetchone()

    message = 'Jai Jinendra!!!\n Upcoming Aatham and Chaudas\n {0} - {1}  \n Please do not eat Kandool food and refrain to eat in night.\n -By Jinesh Jain'.format(out[0],out[1])


    client = TelegramClient('session',api_id,api_hash)
    client.connect()




    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone,input('Enter the code: '))

    try:
        for mob in user_details:
            client.send_message(mob, message)
    

    except Exception as e:
        print(e)

client.disconnect()