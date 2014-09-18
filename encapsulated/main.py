'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Encapsulated Calculator
Date: Thursday, September 18, 2014
GitHub URL: https://github.com/tthorne/dpwp/tree/master/Lab%201%20Madlib
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #tommy's grade
        t = Transcript()
        t.name = "Charles"
        t.address = "124 Beechwood Lane, Chambersburg, PA 17201"
        t.phone = 7173609531
        t.level = "Professional"
        t.horses = 5
        t.fee = 125.95
        t.calc_price()
        self.response.write ("<strong>Name:</strong> " + t.name + "<br /><strong>Address:</strong> " + t.address + "<br /><strong>Phone:</strong> " + str(t.phone) + "<br /><strong>Membership Level:</strong> " + t.level + "<br /><strong>Number of Horses Registered:</strong> $" + str(t.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(t.final_price))



class Transcript(object):
    def __init__(self):
        self.name = 0 #no underscores - public
        self.address = 0
        self.phone = 0
        self.level = 0
        self.horses = 0
        self.fee = 0
        self._final_price = 0 #two underscores - private

    @property
    def final_price(self):
        return self._final_price

    @final_price.setter
    def final_price(self,new_final_price):
        self._final_price = new_final_price

    def calc_price(self):
        #calculate final grade
        self._final_price = (self.horses * self.fee)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
