from configparser import ConfigParser
from systemeLogs import *
import tkinter

def ecrireConfigIni(ip,apiKey,apiSecret):
    logger.info('informations sauvegardees')
    config = ConfigParser()

    config['settings'] = {
        'debug' : 'true',
        'ip' : ip, # IP pare-feu
        'api_key' : apiKey, # Clé api
        'api_secret' : apiSecret # Secret Api
    }

    with open("config.ini", "w") as f:
        config.write(f)

        

def lireIni():
    logger.info('Lecture config.ini')

    parser = ConfigParser()
    parser.read('config.ini')

    # Si vide ou partiellement vide
    if  parser.sections() == [] or parser.get('settings','ip') == "" or parser.get('settings','api_key') == "" or parser.get('settings','api_secret') =="":
        logger.warning('config.ini vide ou partiellement vide') 
        return(False)
        
    
    # Sinon infos a tester
    else:
        logger.debug('fichier complet')
        ip=parser.get('settings','ip')
        api_key=parser.get('settings','api_key')
        api_secret=parser.get('settings','api_secret')

        donnees=[]
        donnees.append(ip)
        donnees.append(api_key)
        donnees.append(api_secret)
        # IP / api_key / api_secret

        logger.info(donnees)

        return(True)