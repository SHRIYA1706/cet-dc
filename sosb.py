from flask import Flask
app = Flask(__name__)

l=[]
soscalls=[]

@app.route('/add/<x>/<y>/<useid>')
def adduser(x,y,useid):
    global l
    l=l+[[useid,x,y]]
    return "done"

@app.route('/getsos/<uid>/<x>/<y>/<wh>/<sev>/<chk>')
def getsos(uid,x,y,wh,sev,chk):
    global soscalls
    soscalls+=[[uid,x,y,wh,sev,chk]]
    return "done"

@app.route('/delsos/<uid>')
def delsos(uid):
    global soscalls
    for x in soscalls:
        if x[0]==uid:
            soscalls.pop(soscalls.index(x))
    return "done"

@app.route('/polsos')
def polsos():
    global soscalls
    txt=""
    for x in soscalls:
        txt+=(" ").join(x) +":"
    soscalls=[]    
    return txt

if __name__ == '__main__':
   app.run(debug = True)
