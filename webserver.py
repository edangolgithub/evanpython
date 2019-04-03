from flask import Flask

app=Flask(__name__)
@app.route("/p")
def home():
    return "hrllo"

if __name__=="__main__":
 app.run(debug=True)