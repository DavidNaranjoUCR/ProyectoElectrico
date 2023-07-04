import telebot
import re
from email.message import EmailMessage
import ssl
import smtplib
bot = telebot.TeleBot("6023911866:AAGnKJjoFE-bbZ1ncE8hgAlz_wDJiT-oq5k")


email_sender = "pris@ucr.ac.cr"
email_password = "123#Queso"

@bot.message_handler(commands=['start'])
def Mensaje_Bienvenida(message):
    bot.send_message(message.chat.id, "Escriba \n/ayuda para ver comandos del bot")

@bot.message_handler(commands=['ayuda'])
def Mensaje_Bienvenida(message):
    bot.send_message(message.chat.id, "Este es un bot para el envió de correos electrónicos")
    bot.send_message(message.chat.id, "Los comandos del bot son:\n/start: reinicia el bot\n/ayuda: muestra la lista de comandos\n/correo: Permite iniciar el envío del correo\n/buscar: Permite buscar las direcciones de correos electrónicos\n/buscar_todo: Muestra todas las direcciones de correo electrónicos")


@bot.message_handler(commands=['correo'])
def Mensaje_Bienvenida(message):
    bot.send_message(message.chat.id, "Se va enviar un correo")
    bot.send_message(message.chat.id, "Escriba el asunto del correo")

    bot.register_next_step_handler(message, get_asunto)

def get_asunto(message):
    asunto = message.text # Se obtiene el asunto del mensaje de Telegram
    bot.send_message(message.chat.id, "Por favor, ingrese el correo de destino.\nSepare por una coma o cambio de línea en caso de ser multiples destinatarios")
    bot.register_next_step_handler(message, get_correo, asunto) # Se llama a la siguiente funcion y se pasa el asunto

def get_correo(message, asunto):
    correo = message.text # Se obtiene el correo del mensaje de Telegram
    correo = re.split(",|\n",correo) # Se crea una lista en caso de múltiples destinatarios que separa por comas y cambios de línea
    bot.send_message(message.chat.id, "Envíe el contenido del correo")
    bot.register_next_step_handler(message, get_mensaje, asunto, correo)

def get_mensaje(message, asunto, correo):
    contenido = message.text
    bot.send_message(message.chat.id, "se va a enviar el correo")
    email_reciever = correo
    subject = asunto
    body = contenido
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.ucr.ac.cr', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())



@bot.message_handler(commands=['buscar'])
def mensaje_buscar(message):
    bot.send_message(message.chat.id, "Escriba el nombre que quiera buscar")
    bot.register_next_step_handler(message, buscar_en_archivo)
def buscar_en_archivo(message):
    mensaje = message.text
    busqueda = mensaje.lower()
    file = open("correos.txt", "r") #conectar con base de datos, en este caso es un archivo de muestra
    lines = file.readlines()
    for line in lines:
        if busqueda in line:
            bot.send_message(message.chat.id, line) # enviar varios mensajes con los correos buscados
    file.close()


@bot.message_handler(commands=['buscar_todo'])
def mensaje_buscar_todo(message):
    bot.send_message(message.chat.id, "Se van a mostrar todas las direcciones de correo electrónico")
    file = open("correos.txt", "r") #conectar con base de datos, en este caso es un archivo de muestra
    lines = file.readlines()
    for line in lines:
        bot.send_message(message.chat.id, line) # enviar varios mensajes con los correos buscados
    file.close()


# Esta función permite enviar los  
#def buscar_en_archivo(message):
#    lista = []
#    busqueda = message.text
#    file = open("correos.txt", "r")
#    lines = file.readlines()
#    for line in lines:
#        if busqueda in line:
#            lista.append(line)
#    nuevalista = ''.join(lista)
#    bot.send_message(message.chat.id, nuevalista) # Enviar un solo mensaje con los mensajes buscados
#    file.close()

        

    






bot.infinity_polling()