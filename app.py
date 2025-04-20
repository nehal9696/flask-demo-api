from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/api/hello', methods=['POST'])
def hello_api():
    try:
        data = request.get_json(silent=True)
        print("Incoming JSON:", data)
        name = data.get('name')

        if not name:
            return jsonify({"error": "Name is required"}), 400

        return jsonify({"message": f"hello, {name}!"}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Invalid JSON or server error"}), 500

    

if __name__ == '__main__':
    app.run(debug=True)
