#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
# Name ; Chetan Rajesh KAbra
# Stduent ID : 1001152872
#lab - 3:00PM to 5:00PM

import sys
import re
# input comes from STDIN (standard input)
import os
#with open('F:/Downloads/isdlite-normals/30yr_03103.dat','rb') as f:
arg1 = sys.argv[1]
#    arg1 ="SEASON"
for line in sys.stdin:
                input_file = os.environ['map_input_file']
                station = input_file.split('_')[1]
                #station= "hello"
                val = line.strip()
                year, temp, windspeed, prcp = val[0: 4], val[14: 19], val[38:43],val[50:55]
                month = val[5:7]
                yearmonth = year+""+month
                if (month =="01" or month =="02"  or month =="03"):
                        seasoon = year+"-SPRING"
                elif(month =="04" or month =="05"  or month =="06"):
                        seasoon = year+"-SUMMER"
                elif(month =="07" or month =="08"  or month =="09"):
                        seasoon = year +"-FALL"
                else:
                        seasoon = year+"-WINTER"
                if temp != "-9999" and windspeed != "-9999" and prcp != "-9999":
                        if (arg1 == "YEAR"):
                            station = station+""+year
                            print '%s\t%s\t%s\t%s' % (station, temp, windspeed,prcp)
                        elif(arg1 =="MONTH"):
                            station = station+""+yearmonth
                            print '%s\t%s\t%s\t%s' %(station,temp,windspeed,prcp)
                        elif(arg1 =="SEASON"):
                            station = station+""+seasoon
                            print '%s\t%s\t%s\t%s' %(station,temp,windspeed,prcp)
