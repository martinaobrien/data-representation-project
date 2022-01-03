from flask import Flask, url_for, request, redirect, abort, jsonify
from FilmDao import filmDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "Welcome to the Movies"
# get all


@app.route('/films')
def getAll():
    return jsonify(filmDao.getAll())
# find By id


@app.route('/films/<int:Id>')
def findById(Id):
    return jsonify(filmDao.findById(Id))


# create
# curl - X, POST - d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}", http: // 127.0.0.1: 5000/films


@app.route('/films', methods=['POST'])
def create():

    if not request.json:
        abort(400)

    film = {
        "Id": request.json["Id"],
        "Film": request.json["Film"],
        "Director": request.json["Director"],
        "Year": request.json["Year"]
    }
    return jsonify(filmDao.create(film))

    return "served by Create "


# update
# curl - X PUT - d "{\"Title\":\"new Title\", \"Price\":999}" - H "content-type:application/json" http: // 127.0.0.1: 5000/films/1


@app.route('/films/<int:Id>', methods=['PUT'])
def update(Id):
    foundBook = filmDao.findById(Id)
    print(foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'Film' in request.json:
        currentBook['Film'] = request.json['Film']
    if 'Director' in request.json:
        currentBook['Director'] = request.json['Director']
    if 'Year' in request.json:
        currentBook['Year'] = request.json['Year']
    filmDao.update(currentBook)

    return jsonify(currentBook)

# delete
# curl -X DELETE http://127.0.0.1:5000/films/1


@app.route('/films/<int:Id>', methods=['DELETE'])
def delete(Id):
    filmDao.delete(Id)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)