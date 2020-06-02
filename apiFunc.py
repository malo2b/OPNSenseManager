import json
from systemeLogs import *

def listePostes():
    datas = {
        "poste1" : {
            "utilisateur" : "Girard Malo",
            "ip" : "192.168.1.1",
            "uuid" : "123e4567-e89b-12d3-a456-426614174000"
        },
        "poste2" : {
            "utilisateur" : "Dupont Jacques",
            "ip" : "192.168.1.2",
            "uuid" : "123e4567-e89b-12d3-a456-426614174002"
        },
        "poste3" : {
            "utilisateur" : "Martin Antoine",
            "ip" : "192.168.1.3",
            "uuid" : "123e4567-e89b-12d3-a456-426614174018"
        }
    }

    listePostes_dump=json.dumps(datas)
    return(listePostes_dump)

def listeSourceInternet():
    datas = {
        "source1" : "4g",
        "source2" : "fibre",
        "source3" : "Adsl"
    }

    listeSourceInternet_dump=json.dumps(datas)
    return(listeSourceInternet_dump)
    
    