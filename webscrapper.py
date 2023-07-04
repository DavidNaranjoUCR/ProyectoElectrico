import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Definición de variables


# Se extrae informacion general de la página principal
#URL_landing_page = "https://pris.eie.ucr.ac.cr/"
browser = webdriver.Firefox()
#browser.implicitly_wait(300)
#browser.get(URL_landing_page)
#time.sleep(5)
#AboutUs1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[4]").text
#AboutUs2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[5]").text
#AboutUsVector = [AboutUs1, AboutUs2]
#
#browser.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div[2]/nav/ul/li[6]/a/span/img").click()  # Cambiar a español
#time.sleep(7)

#SobreNosotros1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[3]").text
#SobreNosotros2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/p[4]").text
#SobreNosotrosVector = [SobreNosotros1, SobreNosotros2]

#browser.close()
#print("about us1\n",AboutUs1,"\nabout us2\n",AboutUs2)
#print("sobre nosotros1\n",SobreNosotros1, "\nsobre nosotros2\n",SobreNosotros2)

# Se extrae informacion general de la página de Sobre nososotros
#URL_SobreNosotros = "https://pris.eie.ucr.ac.cr/about/"
#browser = webdriver.Firefox()
#browser.get(URL_SobreNosotros)
#time.sleep(2)

#MisionEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[2]/span[2]").text
#ObjetivosEsp1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[5]/span[2]").text
#ObjetivosEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[6]").text
#ObjetivosEspVector = [ObjetivosEsp1, ObjetivosEsp2]
#VisionEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[2]/span[2]").text
#IntereseEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[5]/span[2]").text
#ColaboracionesEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[8]/span[2]").text
#OrganizacionEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/p[3]").text
#
#
##Información de la página About us en inglés 
#URL_SobreNosotros = "https://pris.eie.ucr.ac.cr/en/aboutus/"
#browser.get(URL_SobreNosotros)
#time.sleep(2)
#MisionEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[2]/span[2]").text
#ObjetivosEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[6]/span").text
#ObjetivosEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[7]/span").text
#ObjetivosEngVector = [ObjetivosEng1, ObjetivosEng2]
#VisionEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[2]/span[2]").text
#IntereseEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[5]/span[2]").text
#ColaboracionesEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[8]/span[2]").text
#OrganizacionEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/p[3]").text
#browser.close()
#
#print(ObjetivosEsp1,ObjetivosEng1)
#
## Se extrae informacion de la página de Investigacion
#URLInvestigacion = "https://pris.eie.ucr.ac.cr/investigacion/"
##browser = webdriver.Firefox()
#browser.get(URLInvestigacion)
#time.sleep(2)
#Biocomputacion1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/p[1]").text
#Biocomputacion2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/p[2]").text
#Biocomputacion = [Biocomputacion1, Biocomputacion2]
#AnalisisDeportivo = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[5]").text
#MovimientoHumano = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/p[5]").text
#RoboticaCognitiva = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/div/p[5]").text
#ComputacionCientifica = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[5]/div/div[2]/div/div/div/p[5]").text
#
## Se extrae información de la página de investigación en inglés
#URLInvestigacionEng = "https://pris.eie.ucr.ac.cr/en/research/"
#browser.get(URLInvestigacionEng)
#time.sleep(2)
#BiocomputacionEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/p[1]").text
#BiocomputacionEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/p[2]").text
#BiocomputacionEngVector = [BiocomputacionEng1, BiocomputacionEng2]
#AnalisisDeportivoEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[5]").text
#MovimientoHumanoEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/p[5]").text
#RoboticaCognitivaEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[4]/div/div[1]/div/div/div/p[5]").text
#ComputacionCientificaEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[5]/div/div[2]/div/div/div/p[5]").text
#browser.close()
#
#print(BiocomputacionEng1,Biocomputacion1)
#
## Se extrae información de la páginas de equipos de trabajo
## Información de BEND en español
#URL_BEND = "https://pris.eie.ucr.ac.cr/bend/"
##browser = webdriver.Firefox()
#browser.get(URL_BEND)
#time.sleep(2)
#BENDDescripcionEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#BENDEsp1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[4]").text   # prediccion quimisensibilidad
#BENDEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text   # rastreo de celulas
#BENDEsp3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text   # deteccion de virus
#
#
## Información de BEND en Inglés
#URL_BEND_Eng = "https://pris.eie.ucr.ac.cr/en/bend-2/"
#browser.get(URL_BEND_Eng)
#time.sleep(2)
#BENDDescripcionEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]/span").text
#BENDEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[4]").text   # Prediction of chemosensitivity
#BENDEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text   # Cells tracking
#BENDEng3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text   # Virus detection
#
#browser.close()
#
#
#print(BENDEsp1, BENDEng1)
#
#
## Información ACE en Español
URL_ACE = "https://pris.eie.ucr.ac.cr/ace/"
browser.get(URL_ACE)
time.sleep(2)
ACEDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-471-0-2-0"]/div/div/p[3]/span').text
ACEDescripcionEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-471-0-2-0"]/div/div/p[4]/span').text
ACE_DescripVector = [ACEDescripcionEsp1, ACEDescripcionEsp2]
ACEEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-471-1-0-0"]/div/div/p[4]').text  # segmentacion temporal y espacial
ACEEsp2 = browser.find_element(By.XPATH, '//*[@id="panel-471-1-1-0"]/div/div/p[4]').text  # calibracion modelo de camara
ACEEsp3 = browser.find_element(By.XPATH, '//*[@id="panel-471-1-2-0"]/div/div/div').text   # clasificacion acciones y estrategias
browser.close()
print(ACE_DescripVector)
#
## Información ACE en Inglés
#URL_ACE_Eng = "https://pris.eie.ucr.ac.cr/en/ace-2/"
#browser.get(URL_ACE)
#time.sleep(2)
#ACEDescripcionEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#ACEDescripcionEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#ACE_DescripVectorEng = [ACEDescripcionEng1, ACEDescripcionEng2]
#ACEEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[4]").text  # segmentacion temporal y espacial
#ACEEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # calibracion modelo de camara
#ACEEng3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/div").text   # clasificacion acciones y estrategias
#
#browser.close()
#print(ACEEsp1,ACEEng1)
#
#
## Información de MOVE en Español
#URL_MOVE = "https://pris.eie.ucr.ac.cr/move/"
##browser = webdriver.Firefox()
#browser.get(URL_MOVE)
#time.sleep(2)
#MOVEDescripcionEsp1 = browser.find_element(By.XPATH, '//*[@id="panel-514-0-2-0"]/div/div').text
#browser.close()
#print(MOVEDescripcionEsp1)
#MOVEDescripcionEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#MOVE_DescripVector = [MOVEDescripcionEsp1, MOVEDescripcionEsp2]
#MOVEEsp1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # analisis de la marcha
#MOVEEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # base de datos de movimientos humanos
#
#
##Información de MOVE en inglés
#URL_MOVE_Eng = "https://pris.eie.ucr.ac.cr/en/move-2/"
#browser.get(URL_MOVE_Eng)
#time.sleep(2)
#MOVEDescripcionEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#MOVEDescripcionEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#MOVE_DescripVector_Eng = [MOVEDescripcionEng1, MOVEDescripcionEng2]
#MOVEEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # analisis de la marcha
#MOVEEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # base de datos de movimientos humanos
##browser.close()
#print(MOVEEsp1,MOVEEng1)

# Información de CORE en español
#URL_CORE = "https://pris.eie.ucr.ac.cr/core/"
#browser = webdriver.Firefox()
#browser.get(URL_CORE)
#time.sleep(2)
#COREDescripcionEsp1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#COREDescripcionEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#CORE_DescripVector = [COREDescripcionEsp1, COREDescripcionEsp2]
#COREEsp1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # Implementacion de algoritmos
#COREEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # Modelo de comunicaión

# Información de CORE en inglés
#URL_CORE_Eng = "https://pris.eie.ucr.ac.cr/en/core-2/"
#browser.get(URL_CORE)
#time.sleep(2)
#COREDescripcionEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#COREDescripcionEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#CORE_DescripVector_Eng = [COREDescripcionEng1, COREDescripcionEng2]
#COREEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # Implementacion de algoritmos
#COREEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # Modelo de comunicaión
#browser.close()



# Información de RISE en español
#URL_RISE = "https://pris.eie.ucr.ac.cr/rise/"
#browser8 = webdriver.Firefox()
#browser8.get(URL_RISE)
#time.sleep(2)
#RISEDescripcionEsp1 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[1]").text
#RISEDescripcionEsp2 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#RISE_DescripVector = [RISEDescripcionEsp1, RISEDescripcionEsp2]
#RISEEsp1 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[4]").text  # simulacion de modelos no lineales
#RISEEsp2 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # modelos de aprendizaje automático
#RISEEsp3 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # Análisis de video
#
# Información de RISE en inglés

#URL_RISE_Eng = "https://pris.eie.ucr.ac.cr/en/rise-2/"
#browser8.get(URL_RISE_Egn)
#time.sleep(2)
#RISEDescripcionEng1 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[1]").text
#RISEDescripcionEng2 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#RISE_DescripVectorEng = [RISEDescripcionEsp1, RISEDescripcionEsp2]
#RISEEng1 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/p[4]").text  # simulacion de modelos no lineales
#RISEEng2 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # modelos de aprendizaje automático
#RISEEng3 = browser8.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # Análisis de video
#browser8.close()




# Información de DAWN en Español
#URL_DAWN = "https://pris.eie.ucr.ac.cr/dawn/"
#browser9 = webdriver.Firefox()
#browser.get(URL_DAWN)
#time.sleep(2)
#DAWNDescripcionEsp = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[4]").text
#DAWNEsp1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # Diseño Conceptual
#DAWNEsp2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # animacion digital


# Información de DAWN en inglés
#URL_DAWN_Eng = ""
#browser.get(URL_DAWN)
#time.sleep(2)
#DAWNDescripcionEng = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[4]").text
#DAWNEng1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # Diseño Conceptual
#DAWNEng2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # animacion digital

#browser9.close()


# Información de JAM en español
#URL_JAM = "https://pris.eie.ucr.ac.cr/jam/"
#browser10 = webdriver.Firefox()
#browser10.get(URL_JAM)
#time.sleep(2)
#JAMDescripcionEsp1 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#JAMDescripcionEsp2 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#JAM_DescripVector = [JAMDescripcionEsp1, JAMDescripcionEsp2]
#JAMEsp1 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # Soporte técnico
#JAMEsp2 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # Servicios de la nube



# Información de JAM en inglés
#URL_JAM_Eng = ""
#browser10.get(URL_JAM)
#time.sleep(2)
#JAMDescripcionEng1 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[2]").text
#JAMDescripcionEng2 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/p[3]").text
#JAM_DescripVectorEng = [JAMDescripcionEng1, JAMDescripcionEng2]
#JAMEng1 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div/p[4]").text  # Soporte técnico
#JAMEng2 = browser10.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/div/div/p[4]").text  # Servicios de la nube
#browser.close()
