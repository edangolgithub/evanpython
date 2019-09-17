from flask import Flask,render_template

dict={
    1:"evan",
    2:"shyam",
    3 :"hari"
}
def getval(id):
    if id in dict.keys():
       #print(id)
       return dict[id]
    return None

app=Flask(__name__)

@app.route("/")
def xyz():
    return render_template('abc.html',x="rendered through python")

@app.route("/evan")
def a():
    return "hello evan"

@app.route("/p/<int:id>")
def p(id=100):
    val=getval(id)   
    if not val:
        #print(val)
        #print(id)
        return render_template('abc.html',x="id doesnt exist sorry")        
    return val
if __name__=="__main__":
    app.run(debug=True)