from bottle import route, run

@route('/')
@route('/<name>')
def index(name="Python"):
    return 'Hello %s' % name

run(host='0.0.0.0', port=3000, threaded=True)