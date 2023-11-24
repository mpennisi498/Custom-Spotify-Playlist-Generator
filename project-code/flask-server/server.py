from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# /api/home
@app.route('/api/home',methods=['POST'])
def return_home():
    data = request.get_json()
    print(data)
    return jsonify({'message' : 'https://open.spotify.com/playlist/37i9dQZF1EQpoj8u9Hn81e?si=89sPtY3fTz-P7Clk_TPnNA'})


if __name__ == "__main__":
    app.run(debug=True,port=8080)