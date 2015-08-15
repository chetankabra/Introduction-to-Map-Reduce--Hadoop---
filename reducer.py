#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""
# Name ; Chetan Rajesh KAbra
# Stduent ID : 1001152872
#lab - 1:00PM to 3:00PM

import sys
import operator
lastKey, Avgtemp, Avgwindspeed, Avgprcp, count = None, 0, 0, 0, 0
#with open('C:/Users/SONY/Desktop/output.txt','rb') as f:
all_data = {}
for line in sys.stdin:
                key, tempval,tempwind, tempprcp  = line.split('\t')
                if lastKey and lastKey != key:
                    temp = Avgtemp / float(count)
                    all_data.update({lastKey:temp})
                    print '%s \t %s \t %s \t %s' % (lastKey, Avgtemp / float(count),Avgwindspeed / float(count),Avgprcp /float(count) )
                lastKey = key
                Avgtemp += int(tempval)
                Avgwindspeed +=int(tempwind)
                Avgprcp += int(tempprcp)
                count += 1
if lastKey:
        temp = Avgtemp / float(count)
        all_data.update({lastKey:temp})
        print '%s \t %s \t %s \t %s' % (lastKey, Avgtemp / float(count),Avgwindspeed / float(count),Avgprcp /float(count) )

station,temperature = max(all_data.iteritems(), key=operator.itemgetter(1))
station2,min_temp = min(all_data.iteritems(), key=operator.itemgetter(1))
print 'Compare Temperature '
print 'HIGH Temperature : %s ,%s' %(station,temperature)
print 'Low Temperature: %s, %s'%(station2,min_temp)