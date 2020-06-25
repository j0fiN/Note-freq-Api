from flask import *
from frequency import Note_Freq
from wsgiref.simple_server import make_server
api = Flask(__name__)

@api.route('/api', methods=["GET"])
def getter():
    s = request.args.get("note")
    if s is None:
        return abort(400)
    note = Note_Freq(s)
    if note.frequency() is False:
        return abort(400)
    else:
        return jsonify(dict(
            note=note.N,
            octave=note.octave,
            frequency=note.frequency()
        )), 200

if __name__ =="__main__":
    api.run()