from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    return "Welcome to the nmap service! Visit /nmap to see your XML."


@app.route("/nmap")
def nmap():
    if request.args.get("format", "").lower() == "json":
        # Your solution here
        return "Not implemented"
    return send_from_directory("static", "nmap.xml", mimetype="text/plain")


@app.route("/health")
def health():
    return "Not implemented"


app.run(host="127.0.0.1", port=9000)
