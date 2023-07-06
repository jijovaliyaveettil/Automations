from flask import Flask

#Object of the class Flask
app = Flask(__name__) 

@app.route("/")
def create_app():
    return "Hello"

#Make changes automatically
if __name__ =="__main__":
    app.run(debug=True)