import webapp2
import urllib2 #python classes and code needed to requesting info, receiving and opening
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p = ResultsPage()
        p.inputs = [['item_id', 'text', 'Item Id ex.2060'],['Submit', 'submit']]
        self.response.write(p.print_out())

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
    <body>'''

        self._body = '<img src="images/GW2_Logo.png" width="300px" /><h1>Guild Wars 2 Items</h1>'
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

class ResultsPage():
    def __init__(self):
        #constructor function for the super class
        super(ResultsPage, self).__init__() #Page.__init__()
        self._results = ''

    @property
    def results(self):
        pass

    @results.setter
    def results(self):

        if self.request.GET: #only if there is a zip variable in the url
            #get inro from api
            item_id = self.request.GET['item_id']
            url= "https://api.guildwars2.com/v1/item_details.json?item_id=" + item_id
            #assemble the request
            request = urllib2.Request(url)
            #use the urllib2 to create and object from the api
            opener = urllib2.build_opener()
            #use the url to get a result - request info from API
            result = opener.open(request)

            #parse json
            jsondoc = json.load(result)

            name = jsondoc['name']
            description = jsondoc['description']
            type = jsondoc['type']
            level = jsondoc['level']
            rarity = jsondoc['rarity']
            vendor_value = jsondoc['vendor_value']
            print self.results("<br/><strong>Item Name:</strong> " + name + "<br/><strong>Description:</strong>" + description + "<br/><strong>Type:</strong>" + type + "<br/><strong>Level:</strong>" + level + "<br/><strong>Rarity:</strong>" + rarity + "<br/><strong>Rarity:</strong>" + vendor_value)

    #polymorphism alert!!! -------- method overriding
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._results + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
