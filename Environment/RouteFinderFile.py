# -*- coding: UTF-8 -*-

'''
see route finder website

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
import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
from html.parser import HTMLParser

from Environment.WayPointsDatabaseFile import WayPointsDatabase

# create a subclass and override the handler methods
class HtmlParser(HTMLParser):
    
    def __init__(self, searchedTag):
        HTMLParser.__init__(self)

        self.searchedTag = searchedTag
        self.StartTagFound = False
        self.EndTagFound = False
        self.filteredData = ''
        
    
    def handle_starttag(self, tag, attrs):
        if tag == self.searchedTag:
            #print "Encountered a start tag:", tag
            self.StartTagFound = True
            
    def handle_endtag(self, tag):
        if tag == self.searchedTag:
            #print "Encountered an end tag :", tag
            self.EndTagFound = True
            
    def handle_data(self, data):
        if self.StartTagFound and not(self.EndTagFound):
            #print "Encountered some data  :", data
            self.filteredData += (data)
            
    def searchedTagFound(self):
        return self.StartTagFound and self.EndTagFound
            
    def getFilteredData(self):
        return self.filteredData


class RouteFinder(object):
    route = ''
    
    def __init__(self):
        self.className = self.__class__.__name__

        self.script_url = "http://rfinder.asalink.net/free/autoroute_rtx.php"
        self.base_url = "http://rfinder.asalink.net/free/"

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : user_agent , 
               "Content-type": "application/x-www-form-urlencoded", 
               "Accept": "text/plain"}

    def isConnected(self):
        response = urllib.request.urlopen(url = self.base_url)
        the_html_page = response.read()
        #print the_html_page
        htmlParser = HtmlParser(searchedTag = 'form')
        htmlParser.feed(the_html_page)
        return htmlParser.searchedTagFound()
    
    
    def findRoute(self, Adep, Ades, RFL):
        ''' query the route finder website and retrieve a route '''
        self.Adep = Adep
        self.Ades = Ades
        assert isinstance(RFL, str) and (len(RFL)>0) and str(RFL).startswith('FL')
        assert not(Adep is None) and isinstance(Adep,str) and (len(Adep)>0)
        assert not(Ades is None) and isinstance(Ades,str) and (len(Ades)>0)
        values = { 'id1': Adep,
                    'ic1':'',
                    'id2': Ades,
                    'ic2':'',
                    'minalt':'FL230',
                    'maxalt': RFL,
                    'lvl':'B',
                    'dbid': 1408,
                    'usesid':'Y',
                    'usestar':'Y',
                    'easet':'Y',
                    'rnav':'Y',
                    'nats':'',
                    'k':235644007           } 
        data = urllib.parse.urlencode(values)
        ''' use the script to retrieve a route '''
        response = urllib.request.urlopen(url = self.script_url, data= data)
        
        #print 'encoding = {0}'.format(response.headers.getparam('charset'))
        encoding = response.headers.getparam('charset')
        the_html_page = response.read().decode(encoding)

        the_html_page= the_html_page.replace('&deg;', u'\xb0')
        
        htmlParser = HtmlParser(searchedTag = 'pre')
        htmlParser.feed(the_html_page)
        if (htmlParser.searchedTagFound()):
            self.route = htmlParser.getFilteredData()
            #print '{0}'.format(self.route)
            return True
        return False
            
            
    def getRouteAsList(self):
        ''' get a route as a list '''
        routeList = []
        fixIndex = 0
        for line in self.route.split('\n'):
            if 'Remarks' in line: continue
            if self.Adep in line or self.Ades in line: continue
            index = 0
            fixDict = {}
            for item in line.split(' '):
                item = str(item).strip()
                if len(item)==0: continue
                if index == 0 :
                    #print 'fix= {0}'.format(item)
                    fixDict['Name'] = item
                    index += 1
                if len(item)> 0 and (u'\xb0' in str(item).strip()):
                    if 'N' in item or 'S' in item :
                        #print 'latitude= {0}'.format( unicode(unicode(item).strip()))
                        fixDict['latitude'] = item
                    if 'W' in item or 'E' in item:
                        #print 'longitude= {0}'.format( unicode(unicode(item).strip()))
                        fixDict['longitude'] = str(item).strip()
                    ''' increment only if item len > 0 ''' 
                    index += 1
            if len(fixDict) > 0:
                routeList.append( fixDict )
                fixIndex += 1
        return routeList
    
    def insertWayPointsInDatabase(self, wayPointsDb):
        
        for fix in self.getRouteAsList():    
            wayPointsDb.insertWayPoint(fix['Name'], 
                                       fix['latitude'], 
                                       fix['longitude'])


#============================================
if __name__ == '__main__':
    
    wayPointsDb = WayPointsDatabase()
    assert ( wayPointsDb.read() )
    
    print("=========== Route Finder start  =========== " + time.strftime("%c"))

    routeFinder = RouteFinder()
    if routeFinder.isConnected():
        print('route finder is connected')
        
        print("=========== Route Finder start  =========== " + time.strftime("%c"))
        Adep = 'LPPT'
        Ades = 'LFPG'
        RFL = 'FL360'
        
        if routeFinder.findRoute(Adep, Ades, RFL):
            routeList = routeFinder.getRouteAsList()
            print(routeList)
            routeFinder.insertWayPointsInDatabase(wayPointsDb)
    
    print("=========== Route Finder start  =========== " + time.strftime("%c"))
