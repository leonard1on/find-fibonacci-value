import flask
from flask import request, jsonify
app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/fibonacci', methods=['GET'])
def fibo():
    if 'n' in request.args:
        n = int(request.args['n'])
        if n < 0:
            return "Error: Number must be positive!"
    else:
        return "Error: Number required to use function!"

    if n == 0:
        return jsonify(0)
    fib1 = 0
    fib2 = 1
    for x in range(1, n):
        temp = fib1 + fib2
        fib1 = fib2
        fib2 = temp
    return jsonify(fib2)


@app.errorhandler(404)
def pageNotFount(e):
    return "<h1>Error: Page not found! </h1> <p>Are you lost? API works using \"/fibonacci\".</p>"


app.run()
