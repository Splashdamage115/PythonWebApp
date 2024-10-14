
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

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return render_template(
        "index.html",
          title="This is my homepage"
    )

@app.get("/form")
def form():
    return render_template(
        "Form.html",
          title="Welcome to the form"
    )

@app.post("/feedback")
def processTheData():
    ## print(request.form)
    ## print(f"Name: {request.form['the_name']}")
    ## print(f"Email: {request.form['the_email']}")
    ## print(f"Feedback: {request.form['the_comment']}")

    with open("data/feedback.txt","a") as fb:
        print(f"Name: {request.form['the_name']}", file = fb)
        print(f"Email: {request.form['the_email']}", file = fb)
        print(f"Feedback: {request.form['the_comment']}", file = fb)
        print("-"*60, file = fb)


    return redirect("/")

@app.get("/hello")
def hello():
    return "Hello from my first webapp."

app.run(debug = True)
