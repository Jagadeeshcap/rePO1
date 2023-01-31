from flask import Flask,jsonify,render_template
import socket

app = Flask(__name__)

# Function to fetch hostname and ip
def fetch_Details():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname),str(host_ip)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname_from_function,hostip_from_function = fetch_Details()
    return render_template('index.html',hostname_passed = hostname_from_function,host_ip_passed=hostip_from_function)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5001)
