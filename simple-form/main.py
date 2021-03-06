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
        '''Includes the style sheet for the layout '''
        head = '''<!DOCTYPE HTML>
<html>
    <head>
    <title>Simple Form</title>
    <link href='http://fonts.googleapis.com/css?family=Pacifico|Poiret+One' rel='stylesheet' type='text/css'>
    <style>
    body {
        font-family: 'Poiret One', cursive;
        background: url('coloredhorse.png'), url('coloredhorse2.png');
        background-repeat: no-repeat, no-repeat;
        background-size: 25%, 25%;
        background-position: bottom left, bottom right;
        margin: 0px;
    }

    .bar {
        position: fixed;
        background: #000000;
        height: 60px;
        width: 100%;
        margin-top: -100px;
        border-bottom: 1px solid #7BF6FE;
    }

    .barwrap {
        width: 60%;
        margin: 0px auto;
    }

    .wrap {
        width: 60%;
        margin: 100px auto;
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

    .response {
        border: 1px solid #6D759C;
        padding: 20px;
        width: 50%;
        margin: 20px auto;
        background-color: #BFD6F8;
        border-radius: 20px;
    }

    b, strong {
        font-weight: bolder;
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

    .button {
        color: #BFD6F8;
        background-color: #484EBC;
        border: 1px solid #132042;
        border-radius: 10px;
        height: 30px;
        width: 60px
    }

    .button:hover,
    .button:focus,
    .button:active {
        color: #BFD6F8;
        background-color: #132042;
    }

    </style>
    </head>
    <body>
    <div class="bar"><div class="barwrap"><h1>Register Horse</h1></div></div>
    <div class="wrap">'''
        '''Contains the form asking the user to input the name, breed, year of birth, gender, and if own the horse.'''
        body = '''<form method="GET">
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
            <div class="group">
            <label><strong>Do you own this horse?</strong></label>
            <input type="checkbox" name="own" value="Yes">Yes <input type="checkbox" name="own" value="No">No</div>
            <div class="group"><input type="submit" value="Submit" class="button" /></div>'''

        close = '''
        </form>
        </div>
    </body>
</html>'''
        if self.request.GET:
            #stores info we got from the form
            name = self.request.GET['name']
            breed = self.request.GET['breed']
            yob = self.request.GET['yob']
            gender = self.request.GET['gender']
            own = self.request.GET['own']
            self.response.write(head + '<div class="response"><strong>Your input follows as the following</strong>:<br /><strong>Name:</strong> ' + name + ' <br /><strong>Breed:</strong> ' + breed + '<br /><strong>Year Of Birth:</strong> ' + yob +  '<br /><strong>Gender:</strong> ' + gender + '</br>' + '<strong>Do you own this horse?</strong> ' + own + '</div>' + body + close) # If the user has input the proper information this is what is displayed. If shows the input results along with the form
        else: self.response.write(head + body + close) # If the user hasn't input any information then they see the form.

# DO NOT TOUCH!!
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
