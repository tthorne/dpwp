'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment: Encapsulated Calculator
Date: Thursday, September 18, 2014
GitHub URL: https://github.com/tthorne/dpwp/tree/master/encapsulated
'''
import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Membership Data Information
        #Charles Registration
        c = Registration()
        c.name = "Charles"
        c.address = "124 Main Street, Chambersburg, PA 17201"
        c.phone = "717-555-9545"
        c.level = "Professional"
        c.horses = 5
        c.fee = 125.95
        c.calc_price()
        #self.response.write ("<strong>Name:</strong> " + c.name + "<br /><strong>Address:</strong> " + c.address + "<br /><strong>Phone:</strong> " + c.phone + "<br /><strong>Membership Level:</strong> " + c.level + "<br /><strong>Number of Horses Registered:</strong> " + str(c.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(c.final_price))

        #Megan Registration
        m = Registration()
        m.name = "Megan"
        m.address = "567 Second Street, Chambersburg, PA 17201"
        m.phone = "717-555-9545"
        m.level = "Youth"
        m.horses = 15
        m.fee = 25.95
        m.calc_price()
        #self.response.write ("<br><br><strong>Name:</strong> " + m.name + "<br /><strong>Address:</strong> " + m.address + "<br /><strong>Phone:</strong> " + m.phone + "<br /><strong>Membership Level:</strong> " + m.level + "<br /><strong>Number of Horses Registered:</strong> " + str(m.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(m.final_price))

        #Duke Registration
        d = Registration()
        d.name = "Duke"
        d.address = "2905 Roland Avenue, Chambersburg, PA 17201"
        d.phone = "555-234-6789"
        d.level = "Amatuer"
        d.horses = 1
        d.fee = 75.95
        d.calc_price()
        #self.response.write ("<br><br><strong>Name:</strong> " + d.name + "<br /><strong>Address:</strong> " + d.address + "<br /><strong>Phone:</strong> " + d.phone + "<br /><strong>Membership Level:</strong> " + d.level + "<br /><strong>Number of Horses Registered:</strong> " + str(d.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(d.final_price))

        #Jenn Registration
        j = Registration()
        j.name = "Jennifer"
        j.address = "9012 Norland Avenue, Chambersburg, PA 17201"
        j.phone = "555-573-9753"
        j.level = "Youth"
        j.horses = 5
        j.fee = 25.95
        j.calc_price()
        #self.response.write ("<br><br><strong>Name:</strong> " + j.name + "<br /><strong>Address:</strong> " + j.address + "<br /><strong>Phone:</strong> " + j.phone + "<br /><strong>Membership Level:</strong> " + j.level + "<br /><strong>Number of Horses Registered:</strong> " + str(j.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(j.final_price))

        #Tara's Registration
        t = Registration()
        t.name = "Tara"
        t.address = "1242 Livermoore Road, Chambersburg, PA 17201"
        t.phone = "555-234-9874"
        t.level = "Professional"
        t.horses = 15
        t.fee = 125.95
        t.calc_price()
        #self.response.write ("<br><br><strong>Name:</strong> " + t.name + "<br /><strong>Address:</strong> " + t.address + "<br /><strong>Phone:</strong> " + t.phone + "<br /><strong>Membership Level:</strong> " + t.level + "<br /><strong>Number of Horses Registered:</strong> " + str(t.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(t.final_price))

        p = Page()
        #p.body = "<strong>Name:</strong> " + c.name + "<br /><strong>Address:</strong> " + c.address + "<br /><strong>Phone:</strong> " + c.phone + "<br /><strong>Membership Level:</strong> " + c.level + "<br /><strong>Number of Horses Registered:</strong> " + str(c.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(c.final_price) + "<br/><hr><strong>Name:</strong> " + m.name + "<br /><strong>Address:</strong> " + m.address + "<br /><strong>Phone:</strong> " + m.phone + "<br /><strong>Membership Level:</strong> " + m.level + "<br /><strong>Number of Horses Registered:</strong> " + str(m.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(m.final_price) + "<br/><hr><strong>Name:</strong> " + d.name + "<br /><strong>Address:</strong> " + d.address + "<br /><strong>Phone:</strong> " + d.phone + "<br /><strong>Membership Level:</strong> " + m.level + "<br /><strong>Number of Horses Registered:</strong> " + str(d.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(d.final_price) + "<br/><hr><strong>Name:</strong> " + j.name + "<br /><strong>Address:</strong> " + j.address + "<br /><strong>Phone:</strong> " + j.phone + "<br /><strong>Membership Level:</strong> " + j.level + "<br /><strong>Number of Horses Registered:</strong> " + str(j.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(j.final_price) + "<br/><hr><strong>Name:</strong> " + t.name + "<br /><strong>Address:</strong> " + t.address + "<br /><strong>Phone:</strong> " + t.phone + "<br /><strong>Membership Level:</strong> " + t.level + "<br /><strong>Number of Horses Registered:</strong> " + str(t.horses) + "<br /><strong>Total Registration Fee:</strong> $" + str(t.final_price)
        p.body = "<h1>Registered Members</h1><a href='?name="+ c.name +"'>" + c.name + "</a><br>" + "<a href='?name="+ m.name +"'>" + m.name + "</a><br>" + "<a href='?name="+ d.name +"'>" + d.name + "</a><br>" + "<a href='?name="+ j.name +"'>" + j.name + "</a><br>" + "<a href='?name="+ t.name +"'>" + t.name + "</a><br>"

        # When link is click and there is variables this following is viewed
        if self.request.GET:
            name = self.request.GET['name']

            # if variable = Charles
            if name == "Charles":
                address = c.address
                phone = c.phone
                level = c.level
                horses = c.horses
                fee = c.fee
                _final_price = m.calc_price()
                p.view = "<hr><h1>View Member Information:</h1><strong>Name:</strong> " + name + "<br/><strong>Address:</strong> " + address + "<br><strong>Phone:</strong> " + phone + "</br><strong>Address:</strong> " + level + "<br/><strong>Horses:</strong> " + str(horses) + "<br/><strong>Registration Fee:</strong> $" + str(fee) + "<br/><strong>Final Registration Price:</strong> $" + str(_final_price)

            # if variable = Megan
            if name == "Megan":
                address = m.address
                phone = m.phone
                level = m.level
                horses = m.horses
                fee = m.fee
                _final_price = m.calc_price()
                p.view = "<hr><h1>View Member Information:</h1><strong>Name:</strong> " + name + "<br/><strong>Address:</strong> " + address + "<br><strong>Phone:</strong> " + phone + "</br><strong>Address:</strong> " + level + "<br/><strong>Horses:</strong> " + str(horses) + "<br/><strong>Registration Fee:</strong> $" + str(fee) + "<br/><strong>Final Registration Price:</strong> $" + str(_final_price)

            # if variable = Duke
            if name == "Duke":
                address = d.address
                phone = d.phone
                level = d.level
                horses = d.horses
                fee = d.fee
                _final_price = d.calc_price()
                p.view = "<hr><h1>View Member Information:</h1><strong>Name:</strong> " + name + "<br/><strong>Address:</strong> " + address + "<br><strong>Phone:</strong> " + phone + "</br><strong>Address:</strong> " + level + "<br/><strong>Horses:</strong> " + str(horses) + "<br/><strong>Registration:</strong> $" + str(fee) + "<br/><strong>Final Registration Price:</strong> $" + str(_final_price)

            # if variable = Jennifer
            if name == "Jennifer":
                address = j.address
                phone = j.phone
                level = j.level
                horses = j.horses
                fee = j.fee
                _final_price = j.calc_price()
                p.view = "<hr><h1>View Member Information:</h1><strong>Name:</strong> " + name + "<br/><strong>Address:</strong> " + address + "<br><strong>Phone:</strong> " + phone + "</br><strong>Address:</strong> " + level + "<br/><strong>Horses:</strong> " + str(horses) + "<br/><strong>Registration:</strong> $" + str(fee) + "<br/><strong>Final Registration Price:</strong> $" + str(_final_price)

            # if variable = Tara
            if name == "Tara":
                address = t.address
                phone = t.phone
                level = t.level
                horses = t.horses
                fee = t.fee
                _final_price = t.calc_price()
                p.view = "<hr><h1>View Member Information:</h1><strong>Name:</strong> " + name + "<br/><strong>Address:</strong> " + address + "<br><strong>Phone:</strong> " + phone + "</br><strong>Address:</strong> " + level + "<br/><strong>Horses:</strong> " + str(horses) + "<br/><strong>Registration:</strong> $" + str(fee) + "<br/><strong>Final Registration Price:</strong> $" + str(_final_price)
        else: # if no variables then nothing is viewed
            p.view = ''

        self.response.write(p.print_out())

#Registration
class Registration(object):
    def __init__(self):
        self.name = 0 #no underscores - public
        self.address = 0
        self.phone = 0
        self.level = 0
        self.horses = 0
        self.fee = 0
        self._final_price = 0 #two underscores - private
    #Calculation
    @property
    def final_price(self):
        return self._final_price

    @final_price.setter
    def final_price(self,new_final_price):
        self._final_price = new_final_price

    def calc_price(self):
        #calculate final grade
        self._final_price = (self.horses * self.fee)
        return self._final_price

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
