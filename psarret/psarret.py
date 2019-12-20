import os
import sys
import inspect
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
import numpy as np
from qgis.utils import iface
from datetime import datetime as dt

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

class psarretPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        icon = os.path.join(os.path.join(cmd_folder, 'icon.png'))
        self.action = QAction(QIcon(icon), 'Generate time-series', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu('&PSARRET', self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu('&PSARRET', self.action)
        del self.action

    def run(self):
        # Layer structure
        layer = iface.activeLayer()
        fields = layer.fields()
        DATES=[]
        ys=[]
        IDs=[]
        features = layer.selectedFeatures()
        field_names = [field.name() for field in fields]
        if len(features)>0:
            #plot single figure
            for feat in features:
                attrs = feat.attributes()
                datetitle = field_names[6:-1]
                DATE = [dt.strptime(xk,'%Y%m%d') for xk in datetitle]
                DATES.append(DATE)
                #date_strings = [d.strftime('%Y-%m-%d') for d in datetitle]
                y = attrs[6:-1]#input desired range
                IDs.append(attrs[0])
                ys.append(y)
                x = range(len(y))
                coef = np.polyfit(x,y,1) #linear fit
                poly1d_fn = np.poly1d(coef)
                plt.figure()
                plt.plot(DATE,y,'-r',DATE,y,'bo',DATE,poly1d_fn(x), '--k')#if date is not desired, plot simply x
                plt.ylabel('Displacement [cm]')
                plt.xlabel('Date')
                plt.xticks(rotation=45)
                plt.title('ID '+attrs[0]+' Scan series - linear rate = '+str(coef[0]))
                plt.grid(b=True, which='major', color='#666666', linestyle='-')
                plt.minorticks_on()
                plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
                plt.show()
            #plot total figure
            plt.figure()
            ax = plt.gca()
            for t in range(len(ys)):
                color = next(ax._get_lines.prop_cycler)['color']
                plt.plot(DATES[t],ys[t],linestyle='-',markeredgecolor='none',marker='o', color=color)
            plt.legend(IDs)
            plt.ylabel('Displacement [cm]')
            plt.xlabel('Date')
            plt.xticks(rotation=45)
            #plt.title('Total')
            plt.grid(b=True, which='major', color='#666666', linestyle='-')
            plt.minorticks_on()
            plt.legend(IDs)
            plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
            plt.show()
            self.iface.messageBar().pushMessage('Time-series generated')
        else:
            self.iface.messageBar().pushMessage('select almost one feature')
