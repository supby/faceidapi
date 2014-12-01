from flask import Flask

app = Flask(__name__)

@app.route('/api/v1.0/regnewperson/<string:name>', methods=['GET'])
def reg_new_person(name):
    return "Register New Person"

@app.route('/api/v1.0/regpersonsphoto/<string:name>', methods=['POST'])
def reg_persons_photo(name):
    return "Add person pthoto and retrain related model"

@app.route('/api/v1.0/recognizepersons', methods=['POST'])
def reg_persons_photo():
    return "Recornaze persons on input image, return persons' names"

if __name__ == '__main__':
    app.run(debug=True)