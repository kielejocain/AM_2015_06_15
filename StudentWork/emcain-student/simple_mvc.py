import webbrowser

# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields): # C
        self.name = name
        self.fields = fields
        self.objects = [] # A

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model): # D
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects: # B
            item_template = self.template
            for field in self.model.fields:
                if field in item.keys():
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output


# CONTROLLER: Routes messages
# its job is to contain a dictionary of routes.
class Controller(object):  # if you don't use this in python 2 you don't get to use the new functions from 3.
    def __init__(self):
        self.routes = {}  # creates an empty dictionary

    def route(self, path):  # where does path come from?
        return self.routes[path].render()  # returns the value associated with the "path" key in routes, rendered.
    # render is a method of View so we know that the values in routes are Views.


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()

# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score"])
app.models["game"] = Model("game", ["game_name", "description"])


# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

app.models['game'].objects = [
    {"game_name" : "CalvinBall", "description" : "never played the same way twice"},
    {"game_name" : "Quidditch", "description" : "fun in theory but the broom hurts your legs by the end"},
    {"game_name" : "Hashing", "description" : "the drinking team with a running problem"}]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
# ^ this is the relevant line of code we want to save and output
scores_view = View(score_template, app.models["user"])


# my own type:
game_template = "The game {{game_name}} is {{description}}. <br>"  # why is the \n not showing up??

game_view = View(game_template, app.models["game"])


# app.controller.routes = {
#     "/scores/": scores_view,
#     "/score/": scores_view,
# }

app.controller.routes = {
    "/games/": game_view,
    "/game/": game_view,
}

request_path = "/games/" # this is the key for the dictionary in controller. changed from /scores/
# print(app.controller.route(request_path)) # calls route with request path as parameter. what does this do?
# returns the value associated with the "path" key in routes, rendered.


# TODO:
# 1. Add a new model, view/template and route) -- will do this last.
# 2. call your new route and write output to a file
# 3. open file in your browser

# create template for html file

# the inner variable needs further processing to render correctly
bgcolor = raw_input("What color do you want your page to be? Please enter a valid HTML color. >> ")
file_string = """
<html>
    <head></head>
        <body bgcolor='""" + bgcolor + """'>
""" + game_view.render() + """
    </body>
</html>
"""

# write it to a file with extn .html

print "What would you like your new page to be called? "
url_name = raw_input("Enter a word or words separated by - or _, then press enter. >> ") + ".html"

page = open(url_name, 'w+')
page.write(buffer(file_string))
page.close()

# open file in browser

webbrowser.open(url_name)

