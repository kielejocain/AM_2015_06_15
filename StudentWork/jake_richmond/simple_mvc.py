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
        view = self.routes[path]
        output =  view.render()
        return output

# CONTAINS THE SINGLE CONTROLLER AND ALL MODEL AND VIEW INSTANCES
class Application():
    def __init__(self):
        self.models = {}
        self.views = {}
        self.controller = Controller()


# CREATE AN APPLICATION INSTANCE
app = Application()

# define models (
app.models["user"] = Model("user", ["name", "score", "DNA"])
app.models["game"] = Model("game", ["game_name", "description"])
app.models["type"] = Model("type", ["type_name", "DNA"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9", "DNA": "Monster"},
    {"name": "Carol", "score": "11", "DNA": "Hobbit"},
    {"name": "Ted", "score": "15", "DNA": "Dinosaur"},
    {"name": "Alice", "score": "13", "DNA": "Troll"}]
app.models["type"].objects = [
    {"type_name": "Monster", "DNA": "Hobbit"},
    {"type_name": "Dinosaur", "DNA": "Troll"},
    ]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>, and you are a {{DNA}}!<br>\n"
scores_view = View(score_template, app.models["user"])


# Controller
app.controller.routes = {
    "/scores/": scores_view,
    "/score/": scores_view,


}
# TEST
request_path = "/scores/"
print(app.controller.route(request_path))

# TODO:
# 1. Add a new model, view/template and route)
# 2. call your new route and write output to a file
# 3. open file in your browser