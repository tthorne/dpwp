
import webapp2
import urllib2 #python classes and code needed to requesting info, receiving and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'],['Submit', 'submit']]

        if self.request.GET: #only if there is a zip variable in the url
            wm = WeatherModel() #creates our model
            wm.zip = self.request.GET['zip'] #sends our Zip from the URL to our Model
            wm.callApi() #tells it to connect to the API

            wv = WeatherView() #creates our View
            wv.wdos = wm.dos #takes data objects from model and gives them to view
            p._body = wv.content

        self.response.write(p.print_out())

class WeatherView(object):
    '''This class handles how the data is shown to the user'''
    def __init__(self):
        self.__wdos = []
        self.__content = '<br />'

    def update(self):
        for do in self.__wdos:
            self.__content += do.day + " HIGH: "+ do.high + " Low: " + do.low
            self.__content += "Condition: " + do.condition
            self.__content += '<img src="images/"' + do.code + '.png" width="20" /><br/>'

    @property
    def content(self):
        return self.__content

    @property
    def wdos(self):
        pass

    @wdos.setter
    def wdos(self,arr):
        self.__wdos = arr
        self.update()

class WeatherModel(object):
    ''' This model handles fetching, parsing and sorting data from Yahoo's weather api '''
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.__zip = ''
        self.__xmldoc = ''

        #parse
    #contact API
    def callApi(self):
        #loads requests and loads info from API
        #assemble the request
        request = urllib2.Request(self.__url+self.__zip)
        #use the urllib2 to create and object from the api
        opener = urllib2.build_opener()
        #use the url to get a result - request info from API
        result = opener.open(request)

        #parse data
        self.__xmldoc = minidom.parse(result)

        #sorting data
        list = self.__xmldoc.getElementsByTagName("yweather:forecast")
        self._dos = []
        for tag in list :
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.date = tag.attributes['date'].value
            do.code = tag.attributes['code'].value
            do.condition = tag.attributes['text'].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self._zip = z

class WeatherData(object):
    ''' This data object holds the data fetched by the model and shown by the view '''
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''

class Page(object): #borrowing stuff from the object class
    def __init__(self): #constructor
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = 'Weather App'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constructor function for the super class
        super(FormPage, self).__init__() #Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        #sort through the mega array and create HTML inputs based on the info there.
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item... add it in...
            try:
                self._form_inputs += '" placeholder="' + item[2] + '" />'
            #otherwise.. end tag
            except:
                self._form_inputs += '" />'

    #polymorphism alert!!! -------- method overriding
    def print_out(self):
        return self._head + self._form_open + self._form_inputs + self._form_close + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
