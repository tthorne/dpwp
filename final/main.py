import webapp2
import urllib2 #python classes and code needed to requesting info, receiving and opening
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['item_id', 'text', 'Item Id ex.9579'],['Submit', 'submit']]

        if self.request.GET: #only if there is a zip variable in the url
            #get info from api
            im = ItemModel()
            im.item_id = self.request.GET['item_id']
            im.callApi()

            iv = ItemView()
            iv.idos = im.dos #takes data objects from the model and gives them to view
            p._body = iv.content

        self.response.write(p.print_out())


class ItemView(object):
    '''This class handles how the data is shown to the user '''
    def __init__(self):
        self.__idos = []
        self.__content = '<br/>'

    def update(self):
        for do in self.__idos:
            self.__content += '<h2 class="subhead">Search Results</h2><strong>Name:</strong> ' + do.name + '<br/><strong>Description:</strong> <br/>' + do.description + '<br/><strong>Type:</strong> ' + do.type + '<br/><strong>Level:</strong> ' + do.level + '<br/><strong>Rarity:</strong> ' + do.rarity + '<br/><strong>Vendor Value:</strong> ' + do.vendor_value

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
    ''' This model handles fetching, parsing and sorting data from API'''
    def __init__(self):
        self.__url = "https://api.guildwars2.com/v1/item_details.json?item_id="
        self._item_id = ''

    def callApi(self):
        #Requests and Loads info from API
        request = urllib2.Request(self.__url + self._item_id)
        #use the urllib2 to create and object from the api
        opener = urllib2.build_opener()
        #use the url to get a result - request info from API
        result = opener.open(request)

        #parse json
        jsondoc = json.load(result)
        #Sorts Data
        self._dos = []
        do = ItemData()
        do.name = jsondoc['name']
        do.description = jsondoc['description']
        do.type = jsondoc['type']
        do.level = jsondoc['level']
        do.rarity = jsondoc['rarity']
        do.vendor_value = jsondoc['vendor_value']
        self._dos.append(do)

    @property
    def dos(self):
        return self._dos

    @property
    def item_id(self):
        pass

    @item_id.setter
    def item_id(self,z):
        self._item_id = z



class ItemData(object):
    '''This data object holds the data fetched by the model and shown in the view'''
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
        <title>Guild Wars 2 Item Database Search</title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
        <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700italic,700,400italic' rel='stylesheet' type='text/css'>
    </head>
    <body><div class="wrapper">'''

        self._body = ''
        self._close = '''

    <div class="footer"><hr>&copy 2012 ArenaNet, Inc. All rights reserved. NCsoft, the interlocking NC logo, ArenaNet, Arena.net, Guild Wars, Guild Wars Factions, Factions, Guild Wars Nightfall, Nightfall, Guild Wars: Eye of the North, Eye of the North, Guild Wars 2, and all associated logos and designs are trademarks or registered trademarks of NCsoft Corporation. All other trademarks are the property of their respective owners.</div>
    </div>
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
                self._form_inputs += '" class="button" />'

        print self._form_inputs

    #polymorphism alert!!! -------- method overriding
    def print_out(self):
        return self._head + '<div class="header"><img src="images/GW2_Logo.png" width="500px" /></div><h1>Guild Wars 2 Items Database Search</h1><div class="search">' + self._form_open + self._form_inputs + self._form_close + '</div>' + self._body + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
