#!/usr/bin/env python
# coding: utf-8

# MVC: A GENERIC ARCHITECTURE FOR MAKING APPS THAT DISPLAY DATA

# MODEL: A LIST OF OBJECTS. TYPICALLY FROM A DATABASE
class Model(object):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.objects = []

    def create(self, item):
        self.objects.append(item)


# VIEW: A TEMPLATE FOR A PAGE OR PAGE FRAGMENT
class View(object):
    def __init__(self, template, model):
        self.template = template
        self.model = model

    def render(self):
        output = ""
        for item in self.model.objects:
            item_template = self.template
            for field in self.model.fields:
                if field in item.keys():
                    item_template = item_template.replace("{{" + field + "}}", item[field])
            output += item_template
        return output


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
app.models["user"] = Model("user", ["name", "score"])
app.models["song"] = Model("song", ["title", "origin", "artist"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

app.models["song"].objects = [
    {"title": "Insolita", "origin": "Italian", "artist": "Le Vibrazioni"},
    {"title": "Dimmi", "origin": "Italian", "artist": "Le Vibrazioni"},
    {"title": "Per Tutta La Vita", "origin": "Italian", "artist": "Noemi"},
    {"title": "Nú Gleymist Ég", "origin": "Iceland", "artist": "Árstíðir"}
]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
scores_view = View(score_template, app.models["user"])

songs_template = "The song <em>{{title}}</em> is by {{origin}} artist <strong>{{artist}}</strong>.<br>\n"
songs_view = View(songs_template, app.models["song"])

app.controller.routes = {
    "/scores/": scores_view,
    "/score/": scores_view,
    "/songs/": songs_view,
    "/song/": songs_view,
}

request_path = "/songs/"
print(app.controller.route(request_path))

f = open("output.html", "w")
f.write("<meta charset=utf-8>\n")
f.write(app.controller.route("/songs/"))
f.close()

# TODO:
# 1. Add a new model, view/template and route)
# 2. call your new route and write output to a file
# 3. open file in your browser
