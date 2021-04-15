# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

# # if __name__ == '__main__':
# #     # app.run(host='127.0.0.1', port=8080, debug=True)
# #     app.run(port=8080, debug=True)




from flask import Flask, jsonify, request
from userdb import users
import uuid

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello Azure'


# Get a list of users
@app.route('/users', methods=['GET'])
def find_all_users():
    return jsonify(list(users.values()))


# Get a single user
@app.route('/users/<user_id>', methods=['GET'])
def find_single_user(user_id):
    if user_id not in users:
        return '', 404
    return jsonify(users[user_id])


@app.route('/users', methods=['POST'])
def create_user():
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]

    user_exists = False
    for d in users.values():
        if d["full_name"] == first_name + last_name:
            user_exists = True

    if not user_exists:
        user_id = str(uuid.uuid1())
        users[user_id] = request.json
        users[user_id]['id'] = user_id
        users[user_id]['full_name'] = first_name + last_name
        return jsonify({"status": "success", "result": {"id": str(user_id)}})
    else:
        return jsonify({"status": "failure", "result": {"reason": "User is existing."}})


@app.route('/users/<user_id>', methods=['GET'])
def get_user_greeting(user_id):
    if user_id in users:
        return jsonify({"status": "success", "result": {"user": users[user_id]}, "greeting": "Hello, " + users[user_id]["first_name"] + "!"})
    else:
        return jsonify({"status": "failure", "result": {"reason": "User id " + user_id + " is not existing."}})


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        for key in request.json:
            users[user_id][key] = request.json[key]
        return jsonify(users[user_id])
    else:
        return 'not found', 404


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return 'delete user successful', 200
    else:
        return 'user not found', 404


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(port=8080, debug=True)







# import os
# from flask import Flask, render_template, session, redirect, url_for, flash

# from flask_bootstrap import Bootstrap

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'flask-hello-world-secret-key'
# bootstrap = Bootstrap(app)

# from src.form import nameform
# from src.db import db
# from src.model import userdb

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,"data.sqlite")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# with app.app_context():
#     db.init_app(app)
#     db.create_all()


# @app.route("/", methods=["GET","POST"])
# def index():
#     form = nameform()
    
#     if form.validate_on_submit():
#         name = form.firstname.data + ' ' + form.lastname.data
#         user = userdb.query.filter_by(username=name).first()

#         if user is None:
#             user = userdb(username=name)
#             db.session.add(user)
#             db.session.commit()
#             session["known"] = False
#         else:
#             session["known"] = True
#         return redirect(url_for("index"))
#     return render_template("index.html", form=form, name=session.get("name"), known=session.get("known",False))


# # @app.route("/", methods=["GET","POST"])
# # def index():
# #     # name = None
# #     form = nameform()
# #     if form.validate_on_submit():
# #         # firstname = form.firstname.data
# #         # form.firstname.data = ""
# #         # lastname = form.lastname.data
# #         # form.lastname.data = ""
# #         # name = firstname + ' ' + lastname

# #         old_name = session.get("name")
# #         name = form.firstname.data + ' ' + form.lastname.data
# #         if old_name is not None and old_name != name:
# #             flash("name changed")
# #         session["name"] = name
# #         return redirect(url_for("index"))
# #     return render_template("index.html", form=form, name=session.get("name"))


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"),404


# if __name__ == '__main__':
#     # app.run(host='127.0.0.1', port=8080, debug=True)
#     app.run(port=8080, debug=True)