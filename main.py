from flask import Flask, redirect, url_for, render_template
#redirct and url_for allows redirect from a specific function
#grab an html file and render it as ome page

app = Flask(__name__) #create instance of flask web app

#define how to access the certain page

#@app.route("/") #default will go to home page. can define certain
                #pages after '/'

@app.route("/", methods=['GET','POST'])
def index():
    return "AlgoFlights"

def home(): #returns what is being displayed on the page using html file
    return render_template("home.html") #inline html

if __name__ == "main": #runs the app
    app.run(port=5000, debug = True) #allows for changes to be seen without restarting the server
    
