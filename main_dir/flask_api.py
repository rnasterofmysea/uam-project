from flask import Flask, request, jsonify
import data_sorting

app = Flask(__name__)

@app.route('/<param>') #test api
#   def hello_world():
#    return 'Hello, World!'
def test(param):
    #recieved_data = request.args.get("data");
    received_list = str(param).split('$')
    
    output= data_sorting.sorting(received_list)
    return jsonify(output)
    #return jsonify(param)
@app.route('/echo_call/<param>') #get echo api
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/echo_call', methods=['POST']) #post echo api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "5000")

