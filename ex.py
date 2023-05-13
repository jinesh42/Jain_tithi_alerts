import telebot
import sqlite3 as sq
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient,sync,events
import requests


api_id = '19006611'
api_hash = '9b951b36189af760a33396410e03cd9c'
token = '6035045789:AAGX3pjJa5BpmPytRXAmnIlNRGT_-NOqgX4'

con = sq.connect('tithi.db')
cursor = con.cursor()
cursor.execute("select tithi_date,tithi_name from Tithi_dt where tithi_date>=current_date and tithi_name in ('Aatham','Chaudas') order by tithi_date asc limit 1;")
out = cursor.fetchone()

message = 'Jai Jinendra!!!\n Upcoming Aatham and Chaudas\n {0} - {1}  \n Please do not eat Kandool food and refrain to eat in night.\n -By Jinesh Jain'.format(out[0],out[1])

phone = '+918879453842'

client = TelegramClient('session',api_id,api_hash)
client.connect()
user_details=['+919167263350','+918104537501']



if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone,input('Enter the code: '))

try:
    for mob in user_details:
        client.send_message(mob, message)
    

except Exception as e:
    print(e)

client.disconnect()

#TOKEN = "6035045789:AAGX3pjJa5BpmPytRXAmnIlNRGT_-NOqgX4"
#url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#print(requests.get(url).json())

#chat_id=['721863342','6277500917']
#for i in chat_id:
    #url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={i}&text={message}"
    #print(requests.get(url).json())
