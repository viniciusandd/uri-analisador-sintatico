from flask import abort, render_template, url_for, jsonify

def index():
    return render_template("index.html")