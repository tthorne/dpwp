'''
Student Name: Tara Thorne
Student Number: #0003809521
Assignment:
Date: Friday, September 5, 2014
GitHub URL: https://github.com/tthorne/dpwp/tree/master/Lab%201%20Madlib
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #tommy's grade
        t = Transcript()
        t.grade1 = 90
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99
        self.response.write ("Tommy's final grade is " + str(t.final_grade))

        #sally's grades
        s = Transcript()
        s.grade1 = 45
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        s.calc_grade()
        self.response.write ("<br/>Sally's final grade is " + str(s.final_grade))

class Transcript(object):
    def __init__(self):
        self.grade1 = 0 #no underscores - public
        self.grade2 = 0
        self.quiz1 = 0
        self.quiz2 = 0
        self.final_exam = 0
        self._final_grade = 0 #two underscores - private

    @property
    def final_grade(self):
        return self._final_grade

    @final_grade.setter
    def final_grade(self,new_final_grade):
        self._final_grade = new_final_grade

    def calc_grade(self):
        #calculate final grade
        self._final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam)/5


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
