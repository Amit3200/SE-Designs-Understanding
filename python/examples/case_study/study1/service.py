from flask import Flask, request, jsonify
import json


UPLOAD_FOLDER       = 'testcase/1/dumps/path/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000



@app.route('/')
def service():
    return "Hello World!"

@app.route('/case/study/1/api/doc/uploads/', methods = ['POST'])
def doc_upload():
    if request.method == 'POST':
        from processor import process_request
        user_data  = json.loads(request.files['json'].read())
        data = request.files
        process_request(data, user_data, app)
        return jsonify({"status":200,"message":"request processed","upload":"success"})
    return """INVALID"""


if __name__ == "__main__":
    app.run(debug = True)