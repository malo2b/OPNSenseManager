# -*- coding: utf-8 -*-
 
import logging
from logging.handlers import RotatingFileHandler
 
# Objet pour écrire dans les logs
logger = logging.getLogger()
# Niveau du logger
logger.setLevel(logging.DEBUG)
 
# Format d'écriture
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# Fichier de sauvegarde
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
 
# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)