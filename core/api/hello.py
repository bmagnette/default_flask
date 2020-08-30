from flask import Blueprint, render_template


hello_world_router = Blueprint('hello2', __name__)


@hello_world_router.route("/")
def hello_world():
    """
    Tu peux ajouter ce que tu veux ici, mettre un model
    """

    return render_template("hello.html") # tu peux passer des arguments à ta vue.

