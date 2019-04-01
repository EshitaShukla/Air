'''
TestCase
'''

import time
import unittest


from FlightProfile.src.Guidance.FlightPathFile import FlightPath


Meter2Feet = 3.2808 # one meter equals 3.28 feet
Meter2NauticalMiles = 0.000539956803 # One Meter = 0.0005 nautical miles
NauticalMiles2Meter = 1852 

class Test_Route(unittest.TestCase):

    def test_route(self):
    
        print ("=========== Flight Plan start  =========== ")
        
        strRoute = 'ADEP/EGLL/27L-COMPTON-KENET-GAVGO-DIKAS-STRUMBLE-SLANY-'
        strRoute += 'ABAGU-TIPUR-SHANNON-MALOT-RIKAL-EBONY-SEAER-SCARS-KENNEBUNK-ADES/KJFK/04L'
        
        strRoute = 'ADEP/EGLL/27L-MID-DRAKE-SITET-ETRAT-DVL-LGL-SORAP-BENAR-VANAD-AMB-BALAN-LMG-VELIN-SAU-ENSAC-ADES/LFBM/27'
        
        strRoute = 'ADEP/EGLL/27L-MAY-SFD-BENBO-HAWKE-XAMAB-VEULE-INPAX-RESMI-KOTAP-KETEX-KUSEK-KOTIS-KUKOR-OBEPA-LERGA-LATAM-ARDEG-AVN-MTG-JULEE-ADES/LFMI/33'
        
        flightPath = FlightPath(route = strRoute, 
                                aircraftICAOcode = 'A320',
                                RequestedFlightLevel = 310, 
                                cruiseMach = 0.78, 
                                takeOffMassKilograms = 76000.0)
        '''
        RFL:    FL 310 => 31000 feet
        Cruise Speed    => Mach 0.78                                    
        Take Off Weight    72000 kgs    
        '''
        print ("=========== Flight Plan compute  =========== ")
        
        t0 = time.clock()
        print ('time zero= ' + str(t0))
        lengthNauticalMiles = flightPath.computeLengthNauticalMiles()
        print ('flight path length= {0} nautics '.format(lengthNauticalMiles))
        flightPath.computeFlight(deltaTimeSeconds = 1.0)
        print ('simulation duration= ' + str(time.clock()-t0) + ' seconds')
        
        print ("=========== Flight Plan create output files  =========== ")
        flightPath.createFlightOutputFiles()
        print ("=========== Flight Plan end  =========== " )
    
#============================================
if __name__ == '__main__':
    unittest.main()

