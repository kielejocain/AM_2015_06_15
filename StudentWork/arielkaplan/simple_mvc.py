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
                    clean_field = item[field]
                    if type(clean_field) == list:
                        clean_field = ", ".join(clean_field)
                    item_template = item_template.replace("{{" + field + "}}", str(clean_field))
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
app.models["team"] = Model("team", ["coach", "win_loss", "team_members"])

# load model objects form database tables
app.models["user"].objects = [
    {"name": "Bob", "score": "9"},
    {"name": "Carol", "score": "11"},
    {"name": "Ted", "score": "15"},
    {"name": "Alice", "score": "13"}]

app.models["team"].objects = [
    {"coach": "Mr. Green", "win_loss": "4/1", "team_members": ["Alice", "Bob", "Carol"]},
    {"coach": "Ms. Scarlet", "win_loss": "3/2", "team_members": ["David", "Eve", "Frank"]},
    {"coach": "Col. Mustard", "win_loss": "2/3", "team_members": ["George", "Hannah", "Isabelle"]},
]

score_template = "\nHello <em>{{name}}</em>, your score is <strong>{{score}}</strong>.<br>\n"
scores_view = View(score_template, app.models["user"])

team_template = "Coach: <em>{{coach}}</em><br>" \
                "Win/Loss Record: <strong>{{win_loss}}</strong><br>" \
                "Team Members: <strong>{{team_members}}</strong><br><br>\n"
team_view = View(team_template, app.models["team"])

app.controller.routes = {
    "/scores/": scores_view,
    "/score/": scores_view,
    "/team/": team_view,
    "/teams/": team_view,
}

request_path = "/scores/"
print(app.controller.route(request_path))

request_path = "/teams/"
f = open("mvc_output.html", "w")
f.write(app.controller.route(request_path))

# TODO:
# 1. Add a new model, view/template and route)
# 2. call your new route and write output to a file
# 3. open file in your browser
