from flask import Flask, request, jsonify
import pandas as pd
import csv
import base64
from io import BytesIO
from matplotlib.figure import Figure
import histogram
import tools
import flask_histogram

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        data = "Hello World!"
        return jsonify({"data": data})
    # df = pd.read_csv(f"csv/research_2023-08-10.csv")
    # json_data = df.to_json(orient="values")
    # return json_data


@app.route("/math/<int:num>", methods=["GET"])
def addTwo(num):
    return jsonify({"data": num + 2})


@app.route("/hello")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


@app.route("/hello/world")
def world():
    data = flask_histogram.convertToImage()
    return f"<img src='data:image/png;base64,{data}'/>"
