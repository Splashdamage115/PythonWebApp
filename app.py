
#
# HTTP status codes:
#   
#   100-199: informational messages.
#   200-299: all OK messages.
#   300-399: redirection messages.
#   400-499: client error messages.
#   500-599: server error messages.
#



#
# HTTP methods:
#   
#   GET: (optionally) send data to the web server; request a resource from the server;
#                   ask the server to do something. This is what web browsers use for most interactions with the server
#   POST: sends data from the client to the server (in bulk), typically from a HTML <form>. the SUBMIT button.
#

from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template(
        "index.html",
          title="This is my homepage"
    )

@app.get("/hello")
def hello():
    return "Hello from my first webapp."

app.run(debug = True)
