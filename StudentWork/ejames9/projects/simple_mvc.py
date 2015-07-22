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
app.models["game"] = Model("game", ["game_name", "description"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

app.models["game"].objects = [
    {"game_name": "War", "description": "Match cards, highest card wins."},
    {"game_name": "Go-Fish", "description": "First one to find matches for all cards wins."},
    {"game_name": "Gin", "description": "I don't know how to play this game."},
    {"game_name": "Euker", "description": "Too long to write here, look it up."},
]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
game_template = "\nThe game is <strong>{{game_name}}</strong>. <em>{{description}}</em>.<br>\n"
game_view = View(game_template, app.models["game"])
scores_view = View(score_template, app.models["user"])

app.controller.routes = {
    "/scores/": scores_view,
    "/score/": scores_view,
    "/game/": game_view
}

request_path = "/score/"
print(app.controller.route(request_path))

file = open("output.html", "w")
file.write(app.controller.route("/game/"))
file.close

# TODO:
# 1. Add a new model, view/template and route)
# 2. call your new route and write output to a file
# 3. open file in your browser
