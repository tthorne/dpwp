'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Final
Date: Thursday September 25, 2014
GitHub URL: https://github.com/tthorne/dpwp/tree/master/Lab%201%20Madlib
'''
import webapp2
import urllib2 #python classes and code needed to requesting info, receiving and opening
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['item_id', 'text', 'Item Id ex.9579'],['Submit', 'submit']]

        if self.request.GET: #only if there is a zip variable in the url
            im = ItemModel() #creates our model
            im.item_id = self.request.GET['item_id'] #sends our Zip from the URL to our Model
            im.callApi() #tells it to connect to the API

            iv = ItemView() #creates our View
            iv.idos = im.dos #takes data objects from model and gives them to view
            p._body = iv.content

        self.response.write(p.print_out())

class ItemView(object):
    '''This class handles how the data is shown to the user'''
    def __init__(self):
        self.__idos = []
        self.__content = '<br />'

    def update(self):
        for do in self.__idos:
            self.__content += do.name + " HIGH: "+ do.high + " Low: " + do.low
            self.__content += "Condition: " + do.condition

    @property
    def content(self):
        return self.__content

    @property
    def idos(self):
        pass

    @idos.setter
    def idos(self,arr):
        self.__idos = arr
        self.update()

class ItemModel(object):
    ''' This model handles fetching, parsing and sorting data from Yahoo's weather api '''
    def __init__(self):
        self.__url = "https://api.guildwars2.com/v1/item_details.json?item_id="
        self.__item_id = ''
        self.__jsondoc = ''

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
        self.__jsondoc = json.load(result)

        #sorting data
        list = self.__xmldoc.getElementsByTagName("yweather:forecast")
        self._dos = []
        for tag in list :
            do = ItemData()
            do.name = tag.jsondoc['name']
            do.description = tag.jsondoc['description']
            do.type = tag.jsondoc['type']
            do.level = tag.jsondoc['level']
            do.rarity = tag.jsondoc['rarity']
            do.vendor_value = tag.jsondoc['vendor_value']
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def item_id(self):
        pass

    @item_id.setter
    def item_id(self, z):
        self._item_id = z

class ItemData(object):
    ''' This data object holds the data fetched by the model and shown by the view '''
    def __init__(self):
        self.name = ''
        self.description = ''
        self.type = ''
        self.level = ''
        self.rarity = ''
        self.vendor_value = ''

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
