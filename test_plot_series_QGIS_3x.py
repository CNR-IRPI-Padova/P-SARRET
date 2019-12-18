## created by Stefano Crema and Giacomo Titti 20191211
## License type: GPL v.3
#
# Imports
import matplotlib.pyplot as plt
import numpy as np
from qgis.utils import iface
from datetime import datetime as dt
#
# Layer structure
layer = iface.activeLayer()
fields = layer.fields()

features = layer.selectedFeatures()

field_names = [field.name() for field in fields]
#
for feat in features:
    attrs = feat.attributes()
    datetitle = field_names[6:-1]
    DATE = [dt.strptime(xk,'%Y%m%d') for xk in datetitle]
    #date_strings = [d.strftime('%Y-%m-%d') for d in datetitle]
    y = attrs[6:-1]#input desired range
    x = range(len(y))
    coef = np.polyfit(x,y,1) #linear fit
    poly1d_fn = np.poly1d(coef)
    # print(attrs)
    plt.figure()
    plt.plot(DATE,y,'-r',DATE,y,'bo',DATE,poly1d_fn(x), '--k')#if date is not desired, plot simply x
    plt.ylabel('H var [m]')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.title('ID '+attrs[0]+' Scan series - rate = '+str(coef[0]))
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.show()
#
#print(y)
#print(field_names[6:-1])
