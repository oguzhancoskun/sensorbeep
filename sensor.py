import sensors
import re
import os
import time

print 'System is running stable'



while(True):
	time.sleep(2)
	sensors.init()

	try:
    		for chip in sensors.iter_detected_chips():
        
        		for feature in chip:
            			a =  ' %d' % (feature.get_value())

				a=int(a)

	    			if a>65:
					os.system('sh -c \"echo -e \'\a\' > /dev/console\"')
					
					print 'problem!'
					print '  %s: %.2f' % (feature.label, feature.get_value())
								
	finally:
		sensors.cleanup()

