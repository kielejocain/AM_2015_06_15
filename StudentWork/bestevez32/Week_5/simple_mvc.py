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
            output += item_template # This merges Bob / score to the output, then loops through again for Carol / score
        return output


# CONTROLLER: Routes messages
class Controller(object):
    def __init__(self):
        self.routes = {}

    def route(self, path): # path is the URL
        return self.routes[path].render()


# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()


# CREATE AN APPLICATION INSTANCE
app = Application() # Everything above this line is a Framework

# define models (
app.models["user"] = Model("user", ["name", "score"])
app.models["game"] = Model("game", ["game_name", "description"])
app.models["character"] = Model("character", ["name", "rank"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
scores_view = View(score_template, app.models["user"])

app.models["character"].objects = [
    {"name": "Drattlebrat", "rank": "Seasoned"},
    {"name": "Kyou", "rank": "Veteran"},
    {"name": "Glenlivette", "rank": "Novice"},
    {"name": "Jacksyn", "rank": "Heroic"}]

rank_template = "\nWelcome <em>{{name}}</em>, your rank is currently <strong>{{rank}}</strong>.<br>\n"
ranks_view = View(rank_template, app.models["character"])

# Controller
app.controller.routes = {
    "/scores/": scores_view,
    "/score/": scores_view,
    "/ranks/": ranks_view,
    "/rank/": ranks_view,
}

# TEST
request_path = "/scores/"
new_path = "/ranks/"
print(app.controller.route(request_path))
print(app.controller.route(new_path))


# TODO:
# 1. Add a new model, view/template and route)
# 2. call your new route and write output to a file
# 3. open file in your browser
f = open("output.html", "w")
f.write(app.controller.route("/ranks/"))
f.close()
