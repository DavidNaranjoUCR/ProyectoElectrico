import telebot
from telebot import types
from telebot import formatting
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Definición de variables
# Extrae el token del bot
bot = telebot.TeleBot("6070473082:AAEr0curi1pZ8FJBjjznATaZeFtVJW6Jnps")

# Diccionario para las palabras en inglés
set1 = ["Bachelors", "Licentiate", "Masters", "PhD", "Postdoc"]
set2 = ["Bachillerato", "Licenciatura", "Maestría", "Doctorado", "Posdoctorado"]

word_mapping = {}

for word1, word2 in zip(set1, set2):
    word_mapping[word1] = word2
    word_mapping[word1.lower()] = word2.lower()




# Botones de interacción
# Botones de /equipos
botonACE = types.InlineKeyboardButton(text='Más sobre ACE', callback_data="ACE")
botonBEND = types.InlineKeyboardButton(text='Más sobre BEND', callback_data="BEND")
botonMOVE = types.InlineKeyboardButton(text='Más sobre MOVE', callback_data="MOVE")
botonCORE = types.InlineKeyboardButton(text='Más sobre CORE', callback_data="CORE")
botonRISE = types.InlineKeyboardButton(text='Más sobre RISE', callback_data="RISE")
botonDAWN = types.InlineKeyboardButton(text='Más sobre DAWN', callback_data="DAWN")
botonJAM = types.InlineKeyboardButton(text='Más sobre JAM', callback_data="JAM")

# Botones de /teams
buttonACE = types.InlineKeyboardButton(text='More about ACE', callback_data="ACE_ENG")
buttonBEND = types.InlineKeyboardButton(text='More about BEND', callback_data="BEND_ENG")
buttonMOVE = types.InlineKeyboardButton(text='More about MOVE', callback_data="MOVE_ENG")
buttonCORE = types.InlineKeyboardButton(text='More about CORE', callback_data="CORE_ENG")
buttonRISE = types.InlineKeyboardButton(text='More about RISE', callback_data="RISE_ENG")
buttonDAWN = types.InlineKeyboardButton(text='More about DAWN', callback_data="DAWN_ENG")
buttonJAM = types.InlineKeyboardButton(text='More about JAM', callback_data="JAM_ENG")

# Se extrae informacion general de la página principal en inglés y español
URL_landing_page = "https://pris.eie.ucr.ac.cr/"
browser = webdriver.Firefox()
browser.get(URL_landing_page)
time.sleep(5)
#
#AboutUs1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[4]").text
#AboutUs2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[5]").text
#AboutUsVector = [AboutUs1, AboutUs2]
#
#
Spanish = browser.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[2]/nav/ul/li[6]/a/span").click()
time.sleep(5)
SobreNosotros1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[3]").text
SobreNosotros2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[4]").text
SobreNosotrosVector = [SobreNosotros1, SobreNosotros2]
#SobreNosotros1 = ""

#
#
## Se extrae informacion general de la página de Sobre nososotros
URL_SobreNosotros = "https://pris.eie.ucr.ac.cr/about/"
browser.get(URL_SobreNosotros)
time.sleep(2)

MisionEsp = browser.find_element(By.XPATH, '//*[@id="panel-314-1-0-0"]/div/div/p[2]/span[2]').text
ObjetivosEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-314-1-0-0"]/div/div/p[5]/span[2]').text
ObjetivosEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-314-1-0-0"]/div/div/p[6]/span').text
ObjetivosEspVector = [ObjetivosEsp1, ObjetivosEsp2]
VisionEsp = browser.find_element(By.XPATH, '//*[@id="panel-314-1-1-0"]/div/div/p[2]/span[2]').text
IntereseEsp = browser.find_element(By.XPATH, '//*[@id="panel-314-1-1-0"]/div/div/p[5]/span[2]').text
ColaboracionesEsp = browser.find_element(By.XPATH, '//*[@id="panel-314-1-1-0"]/div/div/p[8]/span[2]').text
OrganizacionEsp = browser.find_element(By.XPATH, '//*[@id="panel-314-2-1-0"]/div/div/p[3]').text
#
#
## Se extrae informacion de la página de Investigacion
URLInvestigacion = "https://pris.eie.ucr.ac.cr/investigacion/"
browser.get(URLInvestigacion)
time.sleep(2)
Biocomputacion1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/p[1]").text
Biocomputacion2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/p[2]").text
Biocomputacion = [Biocomputacion1, Biocomputacion2]
AnalisisDeportivo = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[5]").text
MovimientoHumano = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/p[5]").text
RoboticaCognitiva = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/div/p[5]").text
ComputacionCientifica = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[5]/div/div[2]/div/div/div/p[5]").text
#
#
#
## Se extrae información de la páginas de equipos de trabajo
# Información BEND Español
URL_BEND = "https://pris.eie.ucr.ac.cr/bend/"
browser.get(URL_BEND)
time.sleep(2)
BENDDescripcionEsp = browser.find_element(By.XPATH, '//*[@id="panel-496-0-2-0"]/div/div/p[2]/span').text
BENDEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-496-1-0-0"]/div/div/p[4]').text   # prediccion quimisensibilidad
BENDEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-496-1-1-0"]/div/div/p[4]').text   # rastreo de celulas
BENDEsp3 = browser.find_element(By.XPATH, '//*[@id="panel-496-1-2-0"]/div/div/p[4]').text   # deteccion de virus
#
# Información ACE Español
URL_ACE = "https://pris.eie.ucr.ac.cr/ace/"
browser.get(URL_ACE)
time.sleep(2)
ACEDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-471-0-2-0"]/div/div/p[3]/span').text
ACEDescripcionEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-471-0-2-0"]/div/div/p[4]/span').text
ACE_DescripVector = [ACEDescripcionEsp1, ACEDescripcionEsp2]
ACEEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-471-1-0-0"]/div/div/p[4]').text  # segmentacion temporal y espacial
ACEEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-471-1-1-0"]/div/div/p[4]').text  # calibracion modelo de camara
ACEEsp3 = browser.find_element(By.XPATH, '//*[@id="panel-471-1-2-0"]/div/div/div').text   # clasificacion acciones y estrategias
# Información MOVE Español
URL_MOVE = "https://pris.eie.ucr.ac.cr/move/"
browser.get(URL_MOVE)
time.sleep(2)
MOVEDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-506-0-2-0"]/div/div/p[2]/span').text
MOVEDescripcionEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-506-0-2-0"]/div/div/p[3]/span').text
MOVE_DescripVector = [MOVEDescripcionEsp1, MOVEDescripcionEsp2]
MOVEEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-506-1-1-0"]/div/div/p[4]').text  # analisis de la marcha
MOVEEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-506-1-2-0"]/div/div/p[4]').text  # base de datos de movimientos humanos
#Información CORE Español
URL_CORE = "https://pris.eie.ucr.ac.cr/core/"
browser.get(URL_CORE)
time.sleep(2)
COREDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-514-0-2-0"]/div/div/p[2]/span').text
COREDescripcionEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-514-0-2-0"]/div/div/p[3]/span').text
CORE_DescripVector = [COREDescripcionEsp1, COREDescripcionEsp2]
COREEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-514-1-1-0"]/div/div/p[4]').text  # Implementacion de algoritmos
COREEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-514-1-2-0"]/div/div/p[4]').text  # Modelo de comunicaión
# Información RISE Español
URL_RISE = "https://pris.eie.ucr.ac.cr/rise/"
browser.get(URL_RISE)
time.sleep(2)
RISEDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-525-0-2-0"]/div/div/p[1]/span').text
RISEDescripcionEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-525-0-2-0"]/div/div/p[2]/span').text
RISE_DescripVector = [RISEDescripcionEsp1, RISEDescripcionEsp2]
RISEEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-525-1-0-0"]/div/div/p[4]').text  # simulacion de modelos no lineales
RISEEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-525-1-1-0"]/div/div/p[4]').text  # modelos de aprendizaje automático
RISEEsp3 = browser.find_element(By.XPATH, '//*[@id="panel-525-1-2-0"]/div/div/p[4]').text  # Análisis de video
#
#
URL_DAWN = "https://pris.eie.ucr.ac.cr/dawn/"
browser.get(URL_DAWN)
time.sleep(2)
DAWNDescripcionEsp = browser.find_element(By.XPATH, '//*[@id="panel-544-0-2-0"]/div/div/p[4]/span').text
DAWNEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-544-1-1-0"]/div/div/p[4]').text  # Diseño Conceptual
DAWNEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-544-1-2-0"]/div/div/p[4]').text  # animacion digital
#
URL_JAM = "https://pris.eie.ucr.ac.cr/jam/"
browser.get(URL_JAM)
time.sleep(2)
JAMDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-537-0-2-0"]/div/div/p[2]/span').text
JAMDescripcionEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-537-0-2-0"]/div/div/p[3]/span').text
JAM_DescripVector = [JAMDescripcionEsp1, JAMDescripcionEsp2]
JAMEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-537-1-1-0"]/div/div/p[4]').text  # Soporte técnico
JAMEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-537-1-2-0"]/div/div/p[4]').text  # Servicios de la nube
#
#
#
#
browser.close()



# Comando de bienvenidda /start
@bot.message_handler(commands=['start'])
def Mensaje_Bienvenida(message):
    markup = types.InlineKeyboardMarkup()
    BotonEnglish = types.InlineKeyboardButton(text='English', callback_data="English")
    BotonSpanish = types.InlineKeyboardButton(text='Español', callback_data="Spanish")          
    markup.row(BotonSpanish, BotonEnglish)
    bot.send_message(message.chat.id, "Hola bienvenido al PRIS-Lab\nWelcome to PRIS-Lab\n\nSelecciones su idioma / Select your language", reply_markup=markup)

# Funcion de inscripción
def llenar_form(message, VectorEntradas = [], grado_proceso=[], titulo_proceso=[], grado_concluido=[], titulo_concluido=[], area_interes=[]):

    # https://docs.google.com/forms/d/e/1FAIpQLSdfPOdSPH4zTidTR-PSJFTu19M5fEbDsPmBtqHwZ8h7KDW7Pw/viewform #FORM REAL
    # https://docs.google.com/forms/d/e/1FAIpQLSeDbzQbcA6CexGqZLEDnwL3BoaF1j6yTra_vFzPdmLI68nrkA/viewform #Form de prueba
    URL_Form = "https://docs.google.com/forms/d/e/1FAIpQLSdfPOdSPH4zTidTR-PSJFTu19M5fEbDsPmBtqHwZ8h7KDW7Pw/viewform"
    browser = webdriver.Firefox()
    browser.get(URL_Form)
    time.sleep(1)
    respuestas_cortas = browser.find_elements(By.CLASS_NAME, "whsOnd")
    seleccion_multiple = browser.find_elements(By.CLASS_NAME, "bzfPab")
    respuestas_largas = browser.find_elements(By.CLASS_NAME, "KHxj8b")
    time.sleep(1)
    grado_proceso1 = seleccion_multiple[:5]
    grado_concluido1 = seleccion_multiple[5:10]
    area_interes1 = seleccion_multiple[10:19]
    VectorTitulos = [titulo_proceso, titulo_concluido]
    

    for i in range(len(respuestas_cortas)):
        respuestas_cortas[i].clear()
        if VectorEntradas[i] in ("pass", "Pass"):
            respuestas_cortas[i].send_keys("")

        else:
            respuestas_cortas[i].send_keys(VectorEntradas[i])
# Respuestas Largas
    VectorTitulos2 = [0, 0]
    for i in range(len(VectorTitulos)):
        VectorTitulos2[i] = [entry + "\n" for entry in VectorTitulos[i]]

    for i in range(len(respuestas_largas)):
        respuestas_largas[i].clear()
        if VectorTitulos2[i] in (["pass\n"], ["Pass\n"]):
            respuestas_largas[i].send_keys("")
        else:
            respuestas_largas[i].send_keys(VectorTitulos2[i])
        
# Respuestas de opción múltiple

# Se revisa el diccionario        
    matched_words = []
    for word in grado_proceso:
            matched_word = word_mapping.get(word.lower())
            if matched_word:
                matched_words.append(matched_word.lower())
            else:
                matched_words.append("pass")
# Para la sección de grado en proceso
    grado_proceso_min = [grado.lower() for grado in grado_proceso]
    for item in grado_proceso1:
        if item.text in ("pass", "Pass"):
            pass
        elif item.text.lower() in (grado_proceso_min):
            item.click()
        elif item.text.lower() in (matched_words):
            item.click()
            


# Se revisa el diccionario
    matched_words2 = []
    for word in grado_concluido:
        matched_word2 = word_mapping.get(word.lower())
        if matched_word2:
            matched_words2.append(matched_word2.lower())
        else:
            matched_words2.append("pass")
# Para la sección de grado concluido
    grado_concluido_min = [grado.lower() for grado in grado_concluido]
    for item in grado_concluido1:
        if item.text  in ("pass", "Pass"):
            pass
        elif item.text.lower() in (grado_concluido_min):
            item.click()
        elif  item.text.lower() in (matched_words2):
            item.click()

# Para la sección de Área de Interés
    area_interes_min = [area.lower() for area in area_interes]
    for item in area_interes_min:
        for area in area_interes1:
            if item in area.text.lower():
                area.click()
    
    bot.send_chat_action(message.chat.id,'typing')
    enviar = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    time.sleep(1)
    enviar.click()
    browser.close()
    bot.send_chat_action(message.chat.id,'typing')

# manejo de idiomas

@bot.callback_query_handler(func=lambda call: True)
def handle_language_selection(call):
    if call.data == 'English':
        bot.answer_callback_query(call.id)
        bot.send_message(call.from_user.id, "You've selected English")
        bot.send_message(call.from_user.id, "Type /help for command list")

        # Comando /help
        @bot.message_handler(commands=['help'])
        def research_message(message):
            bot.reply_to(message,"The commands for this bot are\n/start: Resets the bot and returns to language select\n/about_us: Displays general information about PRIS-LAB CURRENTLY NOT WORKING\n/research: Displays PRIS-Lab research areas CURRENTLY NOT WORKING\n"
            "/teams: Displays the work teams that make up PRIS-Lab CURRENTLY NOT WORKING\n/enroll: Allows you to fill in the registration form for the PRIS-Lab\n/contact: Displays contact info and socials of PRIS-Lab")
        
        # Comando /research
        @bot.message_handler(commands=['research'])
        def Research_message(message):
            # Botones de /research
            botACE = types.InlineKeyboardButton(text='About ACE', callback_data="ACE_Research")
            botBEND = types.InlineKeyboardButton(text='About BEND', callback_data="BEND_Research")
            botMOVE = types.InlineKeyboardButton(text='About MOVE', callback_data="MOVE_Research")
            botCORE = types.InlineKeyboardButton(text='About CORE', callback_data="CORE_Research")
            botRISE = types.InlineKeyboardButton(text='About RISE', callback_data="RISE_Research")
            markup = types.InlineKeyboardMarkup()
            markup.row(botBEND)
            markup.row(botACE)
            markup.row(botMOVE)
            markup.row(botCORE)
            markup.row(botRISE)
        
            time.sleep(1)
            bot.reply_to(message,"PRIS-Lab's research areas are:\n\n"+formatting.hbold("BIOCOMPUTING/BEND\nANÁLISIS DEPORTIVO/ACE\nMOVIMIENTO HUMANO/MOVE\n"
            "ROBÓTICA COGNITIVA/CORE\nCOMPUTACIÓN CIENTÍFICA/RISE"),reply_markup=markup, parse_mode='HTML')

        # Comando /contact
        @bot.message_handler(commands=['contact'])
        def Message_contact(message):
            # Botones de /contact
            botonUbicacion = types.InlineKeyboardButton(text='Location', callback_data="Location")
            botonTelefono = types.InlineKeyboardButton(text='Phone numbers', callback_data="Phone")
            botonEmail = types.InlineKeyboardButton(text='Email', callback_data="Email")
            botonApartadoPostal = types.InlineKeyboardButton(text='PO Box', callback_data="PO")
            botonRedes = types.InlineKeyboardButton(text='Links to social networks', callback_data="Socials")
            markup = types.InlineKeyboardMarkup()
            bot.send_chat_action(message.chat.id,'typing')
            time.sleep(1)
            markup.row(botonUbicacion)
            markup.row(botonTelefono)
            markup.row(botonEmail)
            markup.row(botonApartadoPostal)
            markup.row(botonRedes)
            bot.reply_to(message, formatting.hbold("Contact Info\n\n"), reply_markup=markup, parse_mode='HTML')

        # Comando /teams
        @bot.message_handler(commands=["teams"])
        def TeamsMessage(message):
            markup = types.InlineKeyboardMarkup()
        
            bot.send_chat_action(message.chat.id, 'typing')
        
            markup.row(buttonBEND)
            markup.row(buttonACE)
            markup.row(buttonMOVE)
            markup.row(buttonCORE)
            markup.row(buttonRISE)
            markup.row(buttonDAWN)
            markup.row(buttonJAM)
        
            time.sleep(1)
            bot.reply_to(message,"The PRIS-Lab work teams are:\n\n"+formatting.hbold("BEND\nACE\nMOVE\nCORE\nRISE\nDAWN\nJAM"),reply_markup=markup, parse_mode='HTML')



        @bot.message_handler(commands=['enroll'])
        def Mensaje_enroll(message):
            bot.send_message(message.chat.id, "Your enrollment process is going to start")
            bot.send_message(message.chat.id, "Type your first name")
            bot.register_next_step_handler(message, get_name)
    
        def get_name(message):
            nombre = message.text # Se obtiene el primer nombre del mensaje de Telegram
            bot.send_message(message.chat.id, "Type your middle name\nIn case you don't have one type 'pass' or 'Pass'")
            bot.register_next_step_handler(message, get_2_name, nombre) # Se llama a la siguiente funcion y se pasa el nombre
        
        def get_2_name(message, nombre):
            nombre2 = message.text # Se obtiene el segundo nombre del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your first lastname')
            bot.register_next_step_handler(message, get_1_lastname, nombre, nombre2) # Se llama a la siguiente funcion y se pasa el segundo nombre
        
        def get_1_lastname(message, nombre, nombre2):
            apellido1 = message.text # Se obtiene el primer apellido del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your second lastname')
            bot.register_next_step_handler(message, get_2_lastname, nombre, nombre2, apellido1) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_2_lastname(message, nombre, nombre2, apellido1):
            apellido2 = message.text # Se obtiene el segundo apellido del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your ID number')
            bot.register_next_step_handler(message, get_ID_number, nombre, nombre2, apellido1, apellido2) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_ID_number(message, nombre, nombre2, apellido1, apellido2):
            identificacion = message.text # Se obtiene la identificación del mensaje de Telegram
            bot.send_message(message.chat.id, "Type your university ID number.\nIn case you don't have one type 'pass' or 'Pass'")
            bot.register_next_step_handler(message, get_Uni_ID, nombre, nombre2, apellido1, apellido2, identificacion) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_Uni_ID(message, nombre, nombre2, apellido1, apellido2, identificacion):
            carne = message.text # Se obtiene la  del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your email')
            bot.register_next_step_handler(message, get_mail, nombre, nombre2, apellido1, apellido2, identificacion, carne) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_mail(message, nombre, nombre2, apellido1, apellido2, identificacion, carne):
            correo = message.text # Se obtiene la  del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your phone number')
            bot.register_next_step_handler(message, get_phone, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_phone(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo):
            telefono = message.text # Se obtiene la  del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your province of residence')
            bot.register_next_step_handler(message, get_province, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_province(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono):
            provincia = message.text # Se obtiene la del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your canton of residence.')
            bot.register_next_step_handler(message, get_cantonENG, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_cantonENG(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia):
            canton = message.text # Se obtiene la del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your district of residence')
            bot.register_next_step_handler(message, get_district, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_district(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton):
            distrito = message.text # Se obtiene la del mensaje de Telegram
            bot.send_message(message.chat.id, 'Type your date of birth  with the format "DD-MM-YYYY" or "DD/MM/YYYY"')
            bot.register_next_step_handler(message, get_date, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton, distrito) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_date(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton, distrito):
            fecha=message.text
            fecha=re.split("-|/",fecha)
            dia = fecha[0]
            mes = fecha[1]
            año = fecha[2]
            bot.send_message(message.chat.id, 'Type your the academic degree(s) you are currently studying\nSeparate them with a comma or a line change\nBachelors\nLicentiate\nMasters\nPhD\nPostdoc'+"\nIn case you don't have one type 'pass' or 'Pass'")
            VectorEntradas = [nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton, distrito, dia, mes, año]
            bot.register_next_step_handler(message, get_degree_process, VectorEntradas) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_degree_process(message, VectorEntradas):
            #print(VectorEntradas)
            grado_proceso = message.text # Se obtiene el correo del mensaje de Telegram
            grado_proceso = re.split(", |\n|,",grado_proceso) # Se crea una lista en caso de múltiples grados que separa por comas y cambios de línea
            bot.send_message(message.chat.id, "Type your the academic degree(s) you are currently studying (one per line, in ascending order, for example: Bachelors of Electrical Engineering, Universidad de Costa Rica\nIn case you don't have one type 'pass' or 'Pass'")
            bot.register_next_step_handler(message, get_title_process, VectorEntradas ,grado_proceso)
        
        def get_title_process(message, VectorEntradas ,grado_proceso):
            titulo_proceso = message.text # Se obtiene el  del mensaje de Telegram
            titulo_proceso = re.split("\n",titulo_proceso) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            bot.send_message(message.chat.id, 'Type your completed academic degree(s)\nSeparate them with a comma or a line change\nBachelors\nLicenciate\nMasters\nPhD\nPostdoc'+"\nIn case you don't have one type 'pass' or 'Pass'")
            bot.register_next_step_handler(message, get_degree_finish, VectorEntradas ,grado_proceso, titulo_proceso)
        
        def get_degree_finish(message, VectorEntradas ,grado_proceso, titulo_proceso):
            grado_concluido = message.text # Se obtiene el  del mensaje de Telegram
            grado_concluido = re.split(", |\n|,",grado_concluido) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            bot.send_message(message.chat.id, "Type your completed academic degree(s) (one per line, in ascending order, for example: Bachelors of Electrical Engineering, Universidad de Costa Rica\nIn case you don't have one type 'pass' or 'Pass'")
            bot.register_next_step_handler(message, get_title_finish, VectorEntradas ,grado_proceso, titulo_proceso, grado_concluido)
        
        def get_title_finish(message, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido):
            titulo_concluido = message.text # Se obtiene el  del mensaje de Telegram
            titulo_concluido = re.split("\n",titulo_concluido) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            bot.send_message(message.chat.id, "Type the lab areas that you are interested in\nYou can write only the acronym separated by a line change for example:\nMOVE\nBEND\n\nAnálisis deportivo: ACE\nBiocomputing: BEND\nBiomechanics: MOVE\nRobótica cognitiva: CORE\nComputación científica: RISE\nArt an Science/3D Animation: DAWN\nIT Services: JAM\nCommunication: VOX\nAudio amd Voice: WAVE")
            bot.register_next_step_handler(message, get_areas_interest, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido, titulo_concluido)
        
        def get_areas_interest(message, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido, titulo_concluido):
            area_interes = message.text # Se obtiene el  del mensaje de Telegram
            area_interes = re.split("\n", area_interes) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            llenar_form(message, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido, titulo_concluido, area_interes)
            bot.send_chat_action(message.chat.id,'typing')
            time.sleep(0.5)
            bot.send_message(message.chat.id,"Enrollment form completed")

    
    
    elif call.data == 'Spanish':
        bot.answer_callback_query(call.id)
        bot.send_message(call.from_user.id, "Ha seleccionado Español")
        bot.send_message(call.from_user.id, "Escriba /ayuda para la lista de comandos")


        
        @bot.message_handler(commands=['ayuda'])
        def Mensaje_ayuda(message):
            bot.reply_to(message,"Los comandos para este bot son\n/start: Reinicia el bot y vuelve a la selección de idioma\n/sobre_nosotros: Muestra la información general del PRIS-Lab\n/investigacion: Muestra las áreas de investigación del PRIS-Lab\n"
            "/equipos: Muestra los equipos de trabajo que componen el PRIS-Lab\n/inscribir: Permite rellenar el formulario de inscripción para el PRIS-Lab\n/contacto: Brinda la información de contacto y redes sociales del PRIS-Lab")

        @bot.message_handler(commands=['inscribir'])
        def Mensaje_Bienvenida(message):
            bot.send_message(message.chat.id, "Va a comenzar con su proceso de inscripción")
            bot.send_message(message.chat.id, "Escriba su primer nombre")
        
            bot.register_next_step_handler(message, get_nombre)
        
        def get_nombre(message):
            nombre = message.text # Se obtiene el primer nombre del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su segundo nombre\nEn caso de no tener escribir "pass" o "Pass"')
            bot.register_next_step_handler(message, get_2_nombre, nombre) # Se llama a la siguiente funcion y se pasa el nombre
        
        def get_2_nombre(message, nombre):
            nombre2 = message.text # Se obtiene el segundo nombre del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su primer apellido')
            bot.register_next_step_handler(message, get_1_apellido, nombre, nombre2) # Se llama a la siguiente funcion y se pasa el segundo nombre
        
        def get_1_apellido(message, nombre, nombre2):
            apellido1 = message.text # Se obtiene el primer apellido del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su segundo apellido')
            bot.register_next_step_handler(message, get_2_apellido, nombre, nombre2, apellido1) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_2_apellido(message, nombre, nombre2, apellido1):
            apellido2 = message.text # Se obtiene el segundo apellido del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su número de identificación')
            bot.register_next_step_handler(message, get_identificacion, nombre, nombre2, apellido1, apellido2) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_identificacion(message, nombre, nombre2, apellido1, apellido2):
            identificacion = message.text # Se obtiene la identificación del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su número de carné.\nEn caso de no tener escribir "pass" o "Pass"')
            bot.register_next_step_handler(message, get_carne, nombre, nombre2, apellido1, apellido2, identificacion) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_carne(message, nombre, nombre2, apellido1, apellido2, identificacion):
            carne = message.text # Se obtiene la  del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su correo eléctrónico')
            bot.register_next_step_handler(message, get_correo, nombre, nombre2, apellido1, apellido2, identificacion, carne) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_correo(message, nombre, nombre2, apellido1, apellido2, identificacion, carne):
            correo = message.text # Se obtiene la  del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su número de teléfono')
            bot.register_next_step_handler(message, get_telefono, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_telefono(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo):
            telefono = message.text # Se obtiene la  del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su provincia de residencia')
            bot.register_next_step_handler(message, get_provincia, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_provincia(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono):
            provincia = message.text # Se obtiene la del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su cantón de residencia')
            bot.register_next_step_handler(message, get_canton, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_canton(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia):
            canton = message.text # Se obtiene la del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su distrito de residencia')
            bot.register_next_step_handler(message, get_distrito, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_distrito(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton):
            distrito = message.text # Se obtiene la del mensaje de Telegram
            bot.send_message(message.chat.id, 'Escriba su fecha de nacimiento en formato "DD-MM-YYYY" o "DD/MM/YYYY"')
            bot.register_next_step_handler(message, get_fecha, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton, distrito) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_fecha(message, nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton, distrito):
            fecha=message.text
            #dia = message.text # Se obtiene la del mensaje de Telegram
            fecha=re.split("-|/",fecha)
            dia = fecha[0]
            mes = fecha[1]
            año = fecha[2]
            bot.send_message(message.chat.id, 'Escriba su(s) grado(s) en proceso\nSeparelos por coma o cambio de línea\nBachillerato\nLicenciatura\nMaestría\nDoctorado\nPosdoctorado'+'\nEn caso de no tener escribir "pass" o "Pass"')
            VectorEntradas = [nombre, nombre2, apellido1, apellido2, identificacion, carne, correo, telefono, provincia, canton, distrito, dia, mes, año]
            bot.register_next_step_handler(message, get_grado_proceso, VectorEntradas) # Se llama a la siguiente funcion y se pasan las variables anteriores
        
        def get_grado_proceso(message, VectorEntradas):
            grado_proceso = message.text # Se obtiene el correo del mensaje de Telegram
            grado_proceso = re.split(", |\n|,",grado_proceso) # Se crea una lista en caso de múltiples grados que separa por comas y cambios de línea
            bot.send_message(message.chat.id, "Escriba sus títulos universitarios en proceso (uno por línea, de forma ascendente académicamente, por ejemplo: Bachillerato en Ingeniería Eléctrica, Universidad de Costa Rica)"+'\nEn caso de no tener escribir "pass" o "Pass"')
            bot.register_next_step_handler(message, get_titulo_proceso, VectorEntradas ,grado_proceso)
        
        def get_titulo_proceso(message, VectorEntradas ,grado_proceso):
            titulo_proceso = message.text # Se obtiene el  del mensaje de Telegram
            titulo_proceso = re.split("\n",titulo_proceso) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            bot.send_message(message.chat.id, "Escriba su(s) grado(s) universitarios concluidos\nSeparelos por coma o cambio de línea\nBachillerato\nLicenciatura\nMaestría\nDoctorado\nPosdoctorado"+'\nEn caso de no tener escribir "pass" o "Pass"')
            bot.register_next_step_handler(message, get_grado_concluido, VectorEntradas ,grado_proceso, titulo_proceso)
        
        def get_grado_concluido(message, VectorEntradas ,grado_proceso, titulo_proceso):
            grado_concluido = message.text # Se obtiene el  del mensaje de Telegram
            grado_concluido = re.split(", |\n|,",grado_concluido) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            bot.send_message(message.chat.id, "Escriba sus títulos universitarios en concluidos (uno por línea, de forma ascendente académicamente, por ejemplo: Bachillerato en Ingeniería Eléctrica, Universidad de Costa Rica)"+'\nEn caso de no tener escribir "pass" o "Pass"')
            bot.register_next_step_handler(message, get_titulo_concluido, VectorEntradas ,grado_proceso, titulo_proceso, grado_concluido)
        
        def get_titulo_concluido(message, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido):
            titulo_concluido = message.text # Se obtiene el  del mensaje de Telegram
            titulo_concluido = re.split("\n",titulo_concluido) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            bot.send_message(message.chat.id, "Escriba las áreas del laboratorio que le interesan\nPuede solo escribir únicamente el acrónimo separado por cambio de línea por ejemplo:\nMOVE\nBEND\nAnálisis deportivo: ACE\nBiocomputación: BEND\nBiomecánica: MOVE\nRobótica cognitiva: CORE\nComputación científica: RISE\nArte y Ciencia/Animación 3D: DAWN\nServicios IT: JAM\nComunicación: VOX\nAudio y Voz: WAVE")
            bot.register_next_step_handler(message, get_areas_interes, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido, titulo_concluido)
        
        def get_areas_interes(message, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido, titulo_concluido):
            area_interes = message.text # Se obtiene el  del mensaje de Telegram
            area_interes = re.split("\n", area_interes) # Se crea una lista en caso de múltiples grados que separa por cambios de línea
            llenar_form(message, VectorEntradas, grado_proceso, titulo_proceso, grado_concluido, titulo_concluido, area_interes)
            bot.send_chat_action(message.chat.id,'typing')
            time.sleep(0.5)
            bot.send_message(message.chat.id,"Formulario Completo")
        



        #Información de la página de investigación

        @bot.message_handler(commands=['investigacion', 'investigación'])
        def Mensaje_invest(message):
            # Botones de /investigación
            botACE = types.InlineKeyboardButton(text='Acerca de ACE', callback_data="ACE_Invest")
            botBEND = types.InlineKeyboardButton(text='Acerca de BEND', callback_data="BEND_Invest")
            botMOVE = types.InlineKeyboardButton(text='Acerca de MOVE', callback_data="MOVE_Invest")
            botCORE = types.InlineKeyboardButton(text='Acerca de CORE', callback_data="CORE_Invest")
            botRISE = types.InlineKeyboardButton(text='Acerca de RISE', callback_data="RISE_Invest")
            markup = types.InlineKeyboardMarkup()
            markup.row(botBEND)
            markup.row(botACE)
            markup.row(botMOVE)
            markup.row(botCORE)
            markup.row(botRISE)
        
            time.sleep(1)
            bot.reply_to(message,"Las áreas de investigación de PRIS-Lab son:\n\n"+formatting.hbold("BIOCOMPUTACIÓN/BEND\nANÁLISIS DEPORTIVO/ACE\nMOVIMIENTO HUMANO/MOVE\n"
            "ROBÓTICA COGNITIVA/CORE\nCOMPUTACIÓN CIENTÍFICA/RISE"),reply_markup=markup, parse_mode='HTML')

        @bot.message_handler(commands=["equipos"])
        def mensajeEquipos(message):
            markup = types.InlineKeyboardMarkup()
        
            bot.send_chat_action(message.chat.id, 'typing')
        
            markup.row(botonBEND)
            markup.row(botonACE)
            markup.row(botonMOVE)
            markup.row(botonCORE)
            markup.row(botonRISE)
            markup.row(botonDAWN)
            markup.row(botonJAM)
        
            time.sleep(1)
            bot.reply_to(message,"Los equipos de trabjado de PRIS-Lab son:\n\n"+formatting.hbold("BEND\nACE\nMOVE\nCORE\nRISE\nDAWN\nJAM"),reply_markup=markup, parse_mode='HTML')
        
        @bot.message_handler(commands=['sobre_nosotros'])
        def Mensaje_info(message):
            # Botones de /sobre_nosotros
            botonMision = types.InlineKeyboardButton(text='Misión', callback_data="Mision")
            botonObjetivos = types.InlineKeyboardButton(text='Objetivos', callback_data="Objetivos")
            botonVision = types.InlineKeyboardButton(text='Visión', callback_data="Vision")
            botonIntereses = types.InlineKeyboardButton(text='Intereses', callback_data="Intereses")
            botonColaboraciones = types.InlineKeyboardButton(text='Colaboraciones', callback_data="Colaboraciones")
            botonOrganizacion = types.InlineKeyboardButton(text='Organización', callback_data="Organizacion")
            markup = types.InlineKeyboardMarkup()
            bot.send_chat_action(message.chat.id,'typing')
            time.sleep(1)
            markup.row(botonMision)
            markup.row(botonObjetivos)
            markup.row(botonVision)
            markup.row(botonIntereses)
            markup.row(botonColaboraciones)
            markup.row(botonOrganizacion)
            SobreNosotros = '\n'.join(SobreNosotrosVector)
            bot.reply_to(message, formatting.hbold("SOBRE NOSOTROS\n\n")+SobreNosotros, reply_markup=markup, parse_mode='HTML')
        
        @bot.message_handler(commands=['contacto'])
        def Mensaje_contacto(message):
            # Botones de /contacto
            botonUbicacion = types.InlineKeyboardButton(text='Ubicación', callback_data="Ubicacion")
            botonTelefono = types.InlineKeyboardButton(text='Teléfonos', callback_data="Telefono")
            botonEmail = types.InlineKeyboardButton(text='Email', callback_data="Email")
            botonApartadoPostal = types.InlineKeyboardButton(text='Apartado Postal', callback_data="Apartado")
            botonRedes = types.InlineKeyboardButton(text='Links a redes sociales', callback_data="Redes")
            markup = types.InlineKeyboardMarkup()
            bot.send_chat_action(message.chat.id,'typing')
            time.sleep(1)
            markup.row(botonUbicacion)
            markup.row(botonTelefono)
            markup.row(botonEmail)
            markup.row(botonApartadoPostal)
            markup.row(botonRedes)
            bot.reply_to(message, formatting.hbold("Información de Contacto\n\n"), reply_markup=markup, parse_mode='HTML')
        
# Botones sobre nosotros
    elif call.data == "Mision":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Misión\n\n")+MisionEsp, parse_mode='HTML')
    
    elif call.data == "Objetivos":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        Objetivos = '\n'.join(ObjetivosEspVector)
        bot.reply_to(call.message, formatting.hbold("Objetivos\n\n")+Objetivos, parse_mode='HTML')
    
    elif call.data == "Vision":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Visión\n\n")+VisionEsp, parse_mode='HTML')
    
    elif call.data == "Intereses":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Intereses\n\n")+IntereseEsp, parse_mode='HTML')

    elif call.data == "Colaboraciones":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Colaboraciones\n\n")+ColaboracionesEsp, parse_mode='HTML')
    elif call.data == "Organizacion":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Organización\n\n")+OrganizacionEsp, parse_mode='HTML')
# Botones Ubicaión
    elif call.data == "Ubicacion":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Ubicación\n\n")+
        "Tercer piso de la Escuela de Ingeniería Eléctrica, Ciudad de la Investigación, "
        "Universidad de Costa Rica, San Pedro de Montes de Oca, San José, Costa Rica.", parse_mode='HTML')

    elif call.data == "Location":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Location\n\n")+
        "Third floor of Electrical Engineering building, Ciudad de la Investigación, "
        "Universidad de Costa Rica, San Pedro de Montes de Oca, San José, Costa Rica.", parse_mode='HTML')
# Botones Teléfono
    elif call.data == "Telefono":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Teléfonos\n\n")+"(+506)2511-2603\n(+506)2511-2642", parse_mode='HTML')

    elif call.data == "Phone":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Phone numbers:\n\n")+"(+506)2511-2603\n(+506)2511-2642", parse_mode='HTML')
# Botón correo
    elif call.data == "Email":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Email\n\n")+"pris-lab@googlegroups.com", parse_mode='HTML')

# Botones Apartado
    elif call.data == "PO":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("PO Box:\n\n")+"11501-2060", parse_mode='HTML')

    elif call.data == "Apartado":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Apartado Postal\n\n")+"11501-2060", parse_mode='HTML')

# Botones Redes sociales
    elif call.data == "Redes":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Redes Sociales\n\n")+"Sitio Web: https://pris.eie.ucr.ac.cr/\nFacebook: https://www.facebook.com/PRISLaboratory\n"
        "Instagram: https://www.instagram.com/pris.lab/\nYoutube: https://www.youtube.com/user/PRISLaboratory", parse_mode='HTML')

    elif call.data == "Socials":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("Social Networks\n\n")+"Website: https://pris.eie.ucr.ac.cr/\nFacebook: https://www.facebook.com/PRISLaboratory\n"
        "Instagram: https://www.instagram.com/pris.lab/\nYoutube: https://www.youtube.com/user/PRISLaboratory", parse_mode='HTML')

# Botones de investigación
    elif call.data == "ACE_Invest":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("ANÁLISIS DEPORTIVO/ACE\n\n")+AnalisisDeportivo, reply_markup=types.InlineKeyboardMarkup().row(botonACE), parse_mode='HTML')
    
    elif call.data == "BEND_Invest":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        BC = '\n'.join(Biocomputacion)
        bot.reply_to(call.message, formatting.hbold("BIOCOMPUTACIÓN/BEND\n\n")+BC, reply_markup=types.InlineKeyboardMarkup().row(botonBEND), parse_mode='HTML')

    elif call.data == "MOVE_Invest":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("MOVIMIENTO HUMANO/MOVE\n\n")+MovimientoHumano, reply_markup=types.InlineKeyboardMarkup().row(botonMOVE), parse_mode='HTML')

    elif call.data == "CORE_Invest":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("ROBÓTICA COGNITIVA/CORE\n\n")+RoboticaCognitiva, reply_markup=types.InlineKeyboardMarkup().row(botonCORE), parse_mode='HTML')
    
    elif call.data == "RISE_Invest":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("COMPUTACIÓN CIENTÍFICA/RISE\n\n")+ComputacionCientifica, reply_markup=types.InlineKeyboardMarkup().row(botonRISE), parse_mode='HTML')


#Botones de research
    elif call.data == "ACE_Research":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("ANÁLISIS DEPORTIVO/ACE\n\n")+AnalisisDeportivo, reply_markup=types.InlineKeyboardMarkup().row(botonACE), parse_mode='HTML')
    
    elif call.data == "BEND_Research":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        BC = '\n'.join(Biocomputacion)
        bot.reply_to(call.message, formatting.hbold("BIOCOMPUTACIÓN/BEND\n\n")+BC, reply_markup=types.InlineKeyboardMarkup().row(botonBEND), parse_mode='HTML')

    elif call.data == "MOVE_Research":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("MOVIMIENTO HUMANO/MOVE\n\n")+MovimientoHumano, reply_markup=types.InlineKeyboardMarkup().row(botonMOVE), parse_mode='HTML')

    elif call.data == "CORE_Research":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("ROBÓTICA COGNITIVA/CORE\n\n")+RoboticaCognitiva, reply_markup=types.InlineKeyboardMarkup().row(botonCORE), parse_mode='HTML')
    
    elif call.data == "RISE_Research":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("COMPUTACIÓN CIENTÍFICA/RISE\n\n")+ComputacionCientifica, reply_markup=types.InlineKeyboardMarkup().row(botonRISE), parse_mode='HTML')



# Botones de equipos español
    elif call.data == "BEND":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("BIOCOMPUTACIÓN/BEND\n\n")+BENDDescripcionEsp+formatting.hbold("\n\nPredicción de quimiosensibilidad\n\n")+BENDEsp1+
        formatting.hbold("\n\nRastreo de células\n\n")+BENDEsp2+formatting.hbold("\n\nDetección de virus\n\n")+BENDEsp3, parse_mode='HTML')

    #Caso de ACE
    elif call.data == "ACE":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        ACE_DESCRIP = '\n'.join(ACE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("ANÁLISIS DEPORTIVO/ACE\n\n")+ACE_DESCRIP+formatting.hbold("\n\nSegmentacion temporal y espacial\n\n")+ACEEsp1+
        formatting.hbold("\n\nCalibración modelo de cámara\n\n")+ACEEsp2+formatting.hbold("\n\nClasificacion acciones y estrategias\n\n")+ACEEsp3, parse_mode='HTML')
    #Caso de MOVE
    elif call.data == "MOVE":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        MOVE_DESCRIP = '\n'.join(MOVE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("MOVIMIENTO HUMANO/MOVE\n\n")+MOVE_DESCRIP+formatting.hbold("\n\nAnálisis de la marcha\n\n")+MOVEEsp1+
        formatting.hbold("\n\nBases de datos de movimiento humano\n\n")+MOVEEsp2, parse_mode='HTML')

    #Caso de CORE
    elif call.data == "CORE":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        CORE_DESCRIP = '\n'.join(CORE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("ROBÓTICA COGNITIVA/CORE\n\n")+CORE_DESCRIP+formatting.hbold("\n\nImplementación de algoritmos\n\n")+COREEsp1+
        formatting.hbold("\n\nModelos de comunicación\n\n")+COREEsp2, parse_mode='HTML')


    #Caso de RISE
    elif call.data == "RISE":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        RISE_DESCRIP = '\n'.join(RISE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("COMPUTACIÓN CIENTÍFICA/RISE\n\n")+RISE_DESCRIP+formatting.hbold("\n\nSimulación de modelos no lineales\n\n")+RISEEsp1+
        formatting.hbold("\n\nMétodos de aprendizaje automático\n\n")+RISEEsp2+formatting.hbold("\n\nAnálisis de video\n\n")+RISEEsp3, parse_mode='HTML')


    #Caso de DAWN
    elif call.data == "DAWN":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("DAWN\n\n")+DAWNDescripcionEsp+formatting.hbold("\n\nDiseño conceptual\n\n")+DAWNEsp1+
        formatting.hbold("\n\nAnimación digital\n\n")+DAWNEsp2, parse_mode='HTML')


    #Caso de JAM
    elif call.data == "JAM":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        JAM_DESCRIP = '\n'.join(JAM_DescripVector)
        bot.reply_to(call.message, formatting.hbold("JAM\n\n")+JAM_DESCRIP+formatting.hbold("\n\nSoporte técnico\n\n")+JAMEsp1+
        formatting.hbold("\n\nServicios de la nube\n\n")+JAMEsp2, parse_mode='HTML')

# Botones /teams

    elif call.data == "BEND_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("BIOCOMPUTACIÓN/BEND\n\n")+BENDDescripcionEsp+formatting.hbold("\n\nPredicción de quimiosensibilidad\n\n")+BENDEsp1+
        formatting.hbold("\n\nRastreo de células\n\n")+BENDEsp2+formatting.hbold("\n\nDetección de virus\n\n")+BENDEsp3, parse_mode='HTML')

    #Caso de ACE
    elif call.data == "ACE_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        ACE_DESCRIP = '\n'.join(ACE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("ANÁLISIS DEPORTIVO/ACE\n\n")+ACE_DESCRIP+formatting.hbold("\n\nSegmentacion temporal y espacial\n\n")+ACEEsp1+
        formatting.hbold("\n\nCalibración modelo de cámara\n\n")+ACEEsp2+formatting.hbold("\n\nClasificacion acciones y estrategias\n\n")+ACEEsp3, parse_mode='HTML')
    #Caso de MOVE
    elif call.data == "MOVE_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        MOVE_DESCRIP = '\n'.join(MOVE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("MOVIMIENTO HUMANO/MOVE\n\n")+MOVE_DESCRIP+formatting.hbold("\n\nAnálisis de la marcha\n\n")+MOVEEsp1+
        formatting.hbold("\n\nBases de datos de movimiento humano\n\n")+MOVEEsp2, parse_mode='HTML')

    #Caso de CORE
    elif call.data == "CORE_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        CORE_DESCRIP = '\n'.join(CORE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("ROBÓTICA COGNITIVA/CORE\n\n")+CORE_DESCRIP+formatting.hbold("\n\nImplementación de algoritmos\n\n")+COREEsp1+
        formatting.hbold("\n\nModelos de comunicación\n\n")+COREEsp2, parse_mode='HTML')


    #Caso de RISE
    elif call.data == "RISE_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        RISE_DESCRIP = '\n'.join(RISE_DescripVector)
        bot.reply_to(call.message, formatting.hbold("COMPUTACIÓN CIENTÍFICA/RISE\n\n")+RISE_DESCRIP+formatting.hbold("\n\nSimulación de modelos no lineales\n\n")+RISEEsp1+
        formatting.hbold("\n\nMétodos de aprendizaje automático\n\n")+RISEEsp2+formatting.hbold("\n\nAnálisis de video\n\n")+RISEEsp3, parse_mode='HTML')


    #Caso de DAWN
    elif call.data == "DAWN_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        bot.reply_to(call.message, formatting.hbold("DAWN\n\n")+DAWNDescripcionEsp+formatting.hbold("\n\nDiseño conceptual\n\n")+DAWNEsp1+
        formatting.hbold("\n\nAnimación digital\n\n")+DAWNEsp2, parse_mode='HTML')


    #Caso de JAM
    elif call.data == "JAM_ENG":
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_chat_action(call.message.chat.id, 'typing')
        time.sleep(1)
        JAM_DESCRIP = '\n'.join(JAM_DescripVector)
        bot.reply_to(call.message, formatting.hbold("JAM\n\n")+JAM_DESCRIP+formatting.hbold("\n\nSoporte técnico\n\n")+JAMEsp1+
        formatting.hbold("\n\nServicios de la nube\n\n")+JAMEsp2, parse_mode='HTML')
        



bot.infinity_polling()