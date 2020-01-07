#!/usr/bin/python
#coding=utf-8
"""
/***************************************************************************
P-SARRET
        begin                : 2019-12
        copyright            : (C) 2019 by Stefano Crema, Giacomo Titti, 
                               Alessandro Sarretta and Matteo Mantovani, 
                               CNR-IRPI, Padova, Dec. 2019
        email                : giacomo.titti@irpi.cnr.it
 ***************************************************************************/

/***************************************************************************
    P-SARRET                                          
    Copyright (C) 2019 by Stefano Crema, Giacomo Titti,Alessandro Sarretta
                          and Matteo Mantovani,CNR-IRPI, Padova, Dec. 2019          

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 ***************************************************************************/
"""

from .psarret import psarretPlugin

def classFactory(iface):
    return psarretPlugin(iface)
