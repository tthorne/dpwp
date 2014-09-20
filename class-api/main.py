import webapp2
import urllib2 #python classes and code needed to requesting info, receiving and opening
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'],['Submit', 'submit']]
        self.response.write(p.print_out())

        if self.request.GET: #only if there is a zip variable in the url
            #get inro from api
            zip = self.request.GET['zip']
            url= "http://xml.weather.yahoo.com/forecastrss?p=" + zip
            #assemble the request
            request = urllib2.Request(url)
            #use the urllib2 to create and object from the api
            opener = urllib2.build_opener()
            #use the url to get a result - request info from API
            result = opener.open(request)

            #parse the XML
            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)
            self.content = '<br/>'
            list = xmldoc.getElementsByTagName("yweather:forecast")
            for item in list:
                self.content += item.attributes['day'].value
                self.content += " HIGH: " + item.attributes['high'].value
                self.content += " LOW: " + item.attributes['low'].value
                self.content += " CONDITION: " + item.attributes['text'].value
                self.content += '<img src="images/' + item.attributes['code'].value+'.png" width="40" />'
                self.content += '<br/>'

            self.response.write(self.content)

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

        print self._form_inputs

    #polymorphism alert!!! -------- method overriding
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
