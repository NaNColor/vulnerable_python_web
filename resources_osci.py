from flask import render_template, make_response, Flask, request, flash
from webapp import app
import subprocess


@app.route("/osci")
def index_osci():
    command = 'cat ' + request.args.get("filename")
    payload = ""
    if command:
        payload = subprocess.check_output(command, shell=True).decode("utf-8")
    return make_response(render_template('osci.html',payload = payload))