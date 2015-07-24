# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name  # a string??
        self.fields = fields  # a list or dict of fields
        self.objects = []  # list of objects obviously but not sure what kind. Where is it used?

    def create(self, item): #what does this do?? doesn't seem to be used.
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template # a string that is a generic form for html showing the data
        self.model = model

    def render(self):
        output = ""  # creates an empty string called output. specific to this function, not global/object wide
        for item in self.model.objects:  # iterating through the list of items
            # [this view].[the model that is a parameter of this view].[the list of objects contained in that model]
            item_template = self.template  # what data type is this?
            for field in self.model.fields:
                if field in item.keys():
                    item_template = item_template.replace("{{" + field + "}}", item[field])
                    # this is where replacement happens. finds the key name of the field surrounded by
                    # double curly brackets and replaces with the value of the field.
            output += item_template
        return output

S
# CONTROLLER: Routes messages
class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path):
        return self.routes[path].render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()


# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score"])  # tuple containing string user and a list of name and score
app.models["game"] = Model("game", ["game_name", "description"])

# load model objects form database tables (no real database tables but we could do something similar with queries)
app.models["user"].objects = [  # add to the dictionary app.models a list of dictionaries under key "user"
    {"name": "Bob", "score": "9"},  # first dictionary in list. Has two entries with key of field and value of entry
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
# one line of the generated html. At what point are the {{}} items replaced with actual values?
scores_view = View(score_template, app.models["user"])  # creates a new View() called scores_view
# this view has the above string, score_template, as the template argument
# what is the second argument? it is a view from the views list in Application app

app.controller.routes = {  #not sure what this does
    "/scores/": scores_view,
    "/score/": scores_view,
}

request_path = "/scores/"
print(app.controller.route(request_path))

# TODO:
# 1. Add a new model, view/template and route)
# 2. call your new route and write output to a file
# 3. open file in your browser
