class Page(object):
    def __init__(self):
        self.title= "Welcome!"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css">
        <link href='http://fonts.googleapis.com/css?family=Pacifico|Poiret+One' rel='stylesheet' type='text/css'>
    </head>
    <body><div class="bar"><div class="barwrap"><h1>Stock Horse Assocaiton</h1></div></div>
    <div class="wrap">
        """
        self.body = ""
        self.view = ""
        self.close = """
    </div>
    </body>
</html>
        """
    def print_out(self):
        all = self.head + self.body + self.view + self.close
        all = all.format(**locals())
        return all