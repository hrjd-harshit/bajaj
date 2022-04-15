from flask import Flask, request, jsonify
from collections import OrderedDict
import json

app = Flask(__name__)


@app.get("/")
def get_countries():
    return {"message" : "Hello World"}


@app.post("/bhfl")
def post_request():
    if request.is_json:
        data = request.get_json()
        temp = json.loads(json.dumps(_list))
        _list = data['data']
        _num_list = []
        _alpha_list = []
        success = True
        for i in temp:
            if str(i).isalnum():
                if str(i).isdigit():
                    _num_list.append(int(i))
                elif str(i).isalpha():
                    _alpha_list.append(i)
        od  = OrderedDict(
            {
            "is_success": "true",
            "user_id": "harshit_jain_12072001",
            "email": "harshitofficial12@gmail.com@",
            "roll_number": "0827CI191020"
            "numbers": json.dumps(_num_list),
            "alphabets": _alpha_list
        }, 201)
        return  od
        
    return {"is_success": False}


if __name__ == '__main__':
    app.run(debug=True)
