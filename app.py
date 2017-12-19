
from flask import Flask, render_template, request, url_for,redirect, jsonify
from engine.SearchEngine import SearchEngine
from engine.IndexerEngine import IndexerEngine

import os, json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search/<string:id_image>",methods=['GET'])
def search_content(id_image):
    filetraining = os.path.join(app.static_folder,"result/training.json")
    fileimage = os.path.join(app.static_folder,"example/query/"+ id_image +".png")
    se = SearchEngine(filetraining)
    results = se.searchQuery(fileimage)
    print results
    return render_template("content.html",results=results,id_image=id_image)

@app.route("/search/",methods=["GET"])
def search():
    filetraining = os.path.join(app.static_folder,"result/training.json")
    fileimage = os.path.join(app.static_folder,"example/query/103100.png")
    se = SearchEngine(filetraining)
    results = se.searchQuery(fileimage)
    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)