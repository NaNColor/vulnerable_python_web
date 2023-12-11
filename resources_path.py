from flask import render_template, make_response, Flask, request, flash
from webapp import app



@app.route("/path_traversal")
def index_path_traversal():
    filename = request.args.get("filename")
    return make_response(render_template('path_traversal.html',payload = open(filename, "r").read()))