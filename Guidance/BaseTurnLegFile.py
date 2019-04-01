# -*- coding: UTF-8 -*-

'''

@note: returns a list of angles in degrees from an initial to a final heading for a given increment in degrees
is used in case of SIMULATED arrival turn.

'''
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import object
import time
import unittest

class BaseTurnLeg(object):
    
    className = ''
    initialHeadingDegrees = 0.0
    finalHeadingDegrees = 0.0
    incrementDegrees = 0.0
    turnLegList = []
    
    def __init__(self, initialHeadingDegrees, 
                 finalHeadingDegrees, 
                 incrementDegrees ):
        
        self.className = self.__class__.__name__

        assert (isinstance(initialHeadingDegrees, float))
        assert (initialHeadingDegrees >= 0.0) and (initialHeadingDegrees <= 360.0)
        self.initialHeadingDegrees = initialHeadingDegrees
            
        assert (isinstance(finalHeadingDegrees, float))
        assert (finalHeadingDegrees >= 0.0) and (finalHeadingDegrees <= 360.0)
        self.finalHeadingDegrees = finalHeadingDegrees
    
        assert isinstance(incrementDegrees, float)
        ''' increment cannot be null but might be positive or negative '''
        assert (incrementDegrees > 0.0) or (incrementDegrees < 0.0)
        self.incrementDegrees = incrementDegrees
            
        strMsg = self.className + ': Base Turn Leg: initial Heading= ' + str(self.initialHeadingDegrees) + ' degrees'
        strMsg += ' final Heading= ' + str(self.finalHeadingDegrees)+ ' degrees '
        strMsg += ' increment= ' + str(self.incrementDegrees) + ' degrees'
        print(strMsg)
        
        self.turnLegList = []
                    
        
    def build(self):
        
        self.turnLegList = []
        #print self.initialHeadingDegrees
        self.turnLegList.append(self.initialHeadingDegrees)
        
        if self.incrementDegrees > 0.0:
            print(self.className + ': increment is > 0.0 => turn clock-wise ')
            if self.initialHeadingDegrees < self.finalHeadingDegrees:
                while self.initialHeadingDegrees < self.finalHeadingDegrees:
                    self.initialHeadingDegrees += self.incrementDegrees
                    self.turnLegList.append(self.initialHeadingDegrees)
                    #print self.initialHeadingDegrees
            else:
                ''' initial heading greater to final ... value will increase then go through 360.0 '''
                while (self.initialHeadingDegrees < 360.0):
                    self.initialHeadingDegrees += self.incrementDegrees
                    if self.initialHeadingDegrees < 360.0:
                        self.turnLegList.append(self.initialHeadingDegrees)

                self.initialHeadingDegrees = 0.0
                self.turnLegList.append(self.initialHeadingDegrees)
                
                while self.initialHeadingDegrees < self.finalHeadingDegrees:
                    ''' need to cope with the situation where initial heading will be greater to 360 '''
                    self.initialHeadingDegrees += self.incrementDegrees
                    self.turnLegList.append(self.initialHeadingDegrees)
                    #print self.initialHeadingDegrees
            
        else:
            print(self.className + ': increment is < 0.0 => turn anti-clock wise ')
            if self.initialHeadingDegrees < self.finalHeadingDegrees:
                #print ''' initial heading lower to final heading '''
                while self.initialHeadingDegrees > 0.0:
                    self.initialHeadingDegrees += self.incrementDegrees
                    if self.initialHeadingDegrees > 0.0:
                        self.turnLegList.append(self.initialHeadingDegrees)
                    
                self.initialHeadingDegrees = 360.0
                self.turnLegList.append(self.initialHeadingDegrees)
                
                while self.finalHeadingDegrees <  self.initialHeadingDegrees:
                    self.initialHeadingDegrees += self.incrementDegrees
                    self.turnLegList.append(self.initialHeadingDegrees)

            else:
                #print self.className + ': initial heading greater to final'
                while self.finalHeadingDegrees < self.initialHeadingDegrees:
                    self.initialHeadingDegrees += self.incrementDegrees
                    self.turnLegList.append(self.initialHeadingDegrees)
        
        return self.turnLegList
    
    def __str__(self):
        return str( self.turnLegList)
    
    
#============================================
class Test_Class(unittest.TestCase):

    def test_Class(self):

    
        print("=========== Base Turn Leg testing   =========== " + time.strftime("%c"))
        
        baseTurnLeg = BaseTurnLeg(150.0, 190.0, 1.0)
        baseTurnLeg.build()
        print(baseTurnLeg)
        
        print("=========== Base Turn Leg testing   =========== " + time.strftime("%c"))
    
        baseTurnLeg = BaseTurnLeg(350.0, 10.0, 1.0)
        baseTurnLeg.build()
        print(baseTurnLeg)
        
        print("=========== Base Turn Leg testing   =========== " + time.strftime("%c"))
        baseTurnLeg = BaseTurnLeg(10.0, 350.0, -1.0)
        baseTurnLeg.build()
        print(baseTurnLeg)
        
        print("=========== Base Turn Leg testing   =========== " + time.strftime("%c"))
        baseTurnLeg = BaseTurnLeg(270.0, 80.0, -1.0)
        baseTurnLeg.build()
        print(baseTurnLeg)
        
        print("=========== Base Turn Leg testing   =========== " + time.strftime("%c"))
        try:
            BaseTurnLeg(361.0, 0.0, 0.0)
            self.assertFalse(True)
        except:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()