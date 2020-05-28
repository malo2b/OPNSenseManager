import os
import sys
from PySide2 import QtWidgets, QtGui
from Gui import *
from traitementFichierIni import *
from plyer import notification


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    # Menu trayicon
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'OPNSense Manager')
        menu = QtWidgets.QMenu(parent)
               
        quitter = menu.addAction("Quitter")
        quitter.triggered.connect(lambda: sys.exit())
        quitter.setIcon(QtGui.QIcon("./img/icon.png"))

        menu.addSeparator()
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)

    def onTrayIconActivated(self, reason):
        # Double clique sur l'icone
        if reason == self.DoubleClick:
            if lireIni(): 
                afficherGui("accueil")
            else:
                afficherGui("config")


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("./img/icon.png"), w)
    tray_icon.show()
    
    if lireIni():
        afficherGui("accueil")
    else:
        notification.notify(
        title='Attention',
        message='Informations manquantes dans le fichier de configuration',
        app_name='OPNSense Manager',
        app_icon="./img/icon.ico"
        )
        afficherGui("config")
        
        
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()