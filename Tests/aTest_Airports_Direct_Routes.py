'''
TestCase
'''
import time
import unittest


from Environment.AirportDatabaseFile import AirportsDatabase
from Environment.RunWaysDatabaseFile import RunWayDataBase
from Environment.WayPointsDatabaseFile import WayPointsDatabase

from Environment.RouteFinderFile import RouteFinder

from Guidance.FlightPathFile import FlightPath
            
class Test_Route(unittest.TestCase):


    def test_route(self):
    
#     import sys
#     temp = sys.stdout #store original stdout object for later
#     sys.stdout = open('log.txt','w') #redirect all prints to this log file

        wayPointsDb = WayPointsDatabase()
        assert wayPointsDb.read()
            
        t0 = time.clock()
        print ' ========== Airports Direct Route testing ======= '
        
        airportsDb = AirportsDatabase()
        assert  airportsDb.read()
        t1 = time.clock()
        print ' time to read airports database= {0:.2f} seconds'.format(t1-t0)
        
        t2 = time.clock()
        runwaysDb = RunWayDataBase()
        assert runwaysDb.read()
        print ' time to read run-way database= {0:.2f} seconds'.format(t2-t1)
        
        print ' ========== Airports Direct Route testing ======= '
        departureCountry = 'Japan'
        departureCountry = 'United Kingdom'
        departureCountry = 'France'
        departureCountry = 'United States'
        arrivalCountry = 'Canada'
        arrivalCountry = 'France' 
        arrivalCountry = 'United States' 
        for departureAirport in  airportsDb.getAirportsFromCountry(Country = departureCountry):
            departureAirportICAOcode = departureAirport.getICAOcode()
            
            departureRunwayName = ''
            departureRunwayFound = False
            
            for runwayName in runwaysDb.findAirportRunWays(airportICAOcode = departureAirportICAOcode, 
                                                           runwayLengthFeet = 11000.0):
                if not(runwaysDb.getFilteredRunWays(
                                                    airportICAOcode = departureAirportICAOcode, 
                                                    runwayName = runwayName) is None):
                    departureRunwayName  = runwayName
                    departureRunwayFound = True
                    break
                
            if departureRunwayFound:
                
                for arrivalAirport in airportsDb.getAirportsFromCountry(Country = arrivalCountry):
                    
                    arrivalRunwayName = ''
                    arrivalRunwayFound = False
                    arrivalAirportICAOcode =  arrivalAirport.getICAOcode()
                    for runwayName in runwaysDb.findAirportRunWays(airportICAOcode = arrivalAirportICAOcode, 
                                                               runwayLengthFeet = 11000.0):
                        if not(runwaysDb.getFilteredRunWays(
                                                        airportICAOcode = arrivalAirportICAOcode, 
                                                        runwayName = runwayName) is None):
                            arrivalRunwayName = runwayName
                            arrivalRunwayFound = True
                            break
                    ''' we have a pair of airports '''
                    
                    if departureRunwayFound and arrivalRunwayFound:
                        distanceMeters = departureAirport.getDistanceMetersTo(arrivalAirport)
                        if  distanceMeters > 300000.0:
                            print ' ========== Airports Direct Route testing ======= '
                            print '{0} - {1} - distance  = {2} meters'.format(departureAirport.getName(), arrivalAirport.getName(), distanceMeters)
                
                            print departureAirport
                            print arrivalAirport
                            routeFinder = RouteFinder()
                            if routeFinder.isConnected():    
                                RFL = 'FL390'
                        
                                if routeFinder.findRoute(departureAirport.getICAOcode(), arrivalAirport.getICAOcode(), RFL):
                                    routeList = routeFinder.getRouteAsList()
                                    print routeList
                                    routeFinder.insertWayPointsInDatabase(wayPointsDb)
                
                                    strRoute = 'ADEP/' + departureAirport.getICAOcode() + '/' + departureRunwayName + '-'
                                    for fix in routeList:    
                                        strRoute += fix['Name'] + '-'
                                    strRoute += 'ADES/' + arrivalAirport.getICAOcode() + '/' + arrivalRunwayName
                                    
                                    print strRoute
                                    
                                    flightPath = FlightPath(route = strRoute, 
                                                                aircraftICAOcode = 'B744',
                                                                RequestedFlightLevel = 390, 
                                                                cruiseMach = 0.92, 
                                                                takeOffMassKilograms = 280000.0)
        
                                
                                    print "=========== Flight Plan compute  =========== " 
                      
                                    t0 = time.clock()
                                    print 'time zero= ' + str(t0)
                                    lengthNauticalMiles = flightPath.computeLengthNauticalMiles()
                                    print 'flight path length= {0:.2f} nautics '.format(lengthNauticalMiles)
                                    flightPath.computeFlight(deltaTimeSeconds = 1.0)
                                    print 'simulation duration= ' + str(time.clock()-t0) + ' seconds'
                                    print "=========== Flight Plan create output files  =========== "
                                    flightPath.createFlightOutputFiles()
                                    
                                    
        #sys.stdout.close() #ordinary file object
        
        
if __name__ == '__main__':
    unittest.main()