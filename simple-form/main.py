'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Simple Form
Date: Thursday September 11, 2014
GitHub URL: https://github.com/tthorne/dpwp/tree/master/Lab%201%20Madlib
'''
import webapp2 # use the webapp2 library

class MainHandler(webapp2.RequestHandler): #Declaring a class
    def get(self): # function that starts everything. Catalyst
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>
    <link href='http://fonts.googleapis.com/css?family=Pacifico|Poiret+One' rel='stylesheet' type='text/css'>
    <style>
    body {
        background: #132042;
        font-family: 'Poiret One', cursive;
        background-image: url('coloredhorse.png');
        margin: 0px;
    }

    .bar {
        position: fixed;
        background: #000000;
        height: 50px;
        width: 100%;
        margin-top: -50px;
    }

    .wrap {
        width: 60%;
        margin: 50px auto;
        border: 4px solid #132042;
        padding: 20px;
        background: #ffffff;
        border-radius: 40px;
        box-shadow: 1px 1px 10px #BFD6F8;
    }

    .group {
        margin-bottom: 15px;
        vertical-align: middle;
    }

    h1 {
        font-family: 'Pacifico', cursive;
        color: #BFD6F8;
        margin-top: 0px;
        margin-bottom: 0px;
    }

    .form {
        display: block;
        width: 95%;
        height: 34px;
        padding: 6px 12px;
        font-size: 14px;
        line-height: 1.42857143;
        color: #666666;
        background-color: #fff;
        border: 1px solid #6D759C;
        border-radius: 4px;
        box-shadow: inset 0 1px 1px rgba(191,214,248, .75);
        transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
    }

    .form:focus {
        border-color: #6D759C;
        outline: 0;
        box-shadow: inset 0 1px 1px rgba(191,214,248,.75), 0 0 8px rgba(191,214,248, .75);
    }

    </style>
    </head>
    <body>
    <div class="bar"><h1>Register Horse</h1></div>
    <div class="wrap">'''

        page_body = '''<form method="GET">
            <div class="group"><label><strong>Name:</strong><label> <input type="text" name="name" class="form" /></div>
            <div class="group"><label><strong>Breed:</strong></label> <input type="text" name="breed" class="form" /></div>
            <div class="group"><label><strong>Year Of Birth:</strong></label> <input type="text" name="yob" class="form" /></div>
            <div class="group"><label><strong>Gender:</strong></label>
            <select name="gender" class="form">
            <option value="">Select</option>
            <option value="Gelding">Gelding</option>
            <option value="Mare">Mare</option>
            <option value="Stallion">Stallion</option>
            </select></div>
            <div class="group"><input type="submit" value="Submit" class="button" /></div>'''

        page_close = '''
        </form>
        </div>
    </body>
</html>'''
        if self.request.GET:
            #stores info we got from the form
            name = self.request.GET['name']
            breed = self.request.GET['breed']
            gender = self.request.GET['gender']
            self.response.write(page_head + '<strong>Name:</strong> ' + name + ' <br /><strong>Breed:</strong> ' + breed + ' <br /><strong>Gender:</strong> ' + gender + "</br>" + page_body + page_close)
        else: self.response.write(page_head + page_body + page_close) #print

# DO NOT TOUCH!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
