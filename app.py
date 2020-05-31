from flask import Flask,jsonify,request,render_template
from five import Db

app = Flask(__name__)
db = Db("localhost","root","","tunanone")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tunan")
def index1():
    return '欢迎访问图南的主页！'

@app.route("/userinfo")
def userinfo():
    userdata = {
        "name":"张三",
        "age":18,
        "high":"183cm"
    }
    return jsonify(userdata)

@app.route("/login",methods=["post"])
def userlogin():
    '''
    {"username":111,"password":111}
    '''
    # data = request.get_json()
    # username = data.get("username")
    # password = data.get("password")

    username = request.values.get("username")
    password = request.values.get("password")

    res = db.qurey("select password from user where username='{}';".format(username))
    if password == res[0][0]:
        userdata = {
            "name":"图南",
            "age":18,
            "high":"183cm"
        } 
        return jsonify(userdata)
    else:
        userdata = {"msg":"密码或者账号错误！"}
        return jsonify(userdata)

@app.route("/reg",methods=["post"])
def reg():
    '''
    {"username":111,"password":111}
    '''
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    res = db.commit("insert into user (username,password) values ('{}','{}');".format(username,password))
    return jsonify({"msg":res})



if __name__ == "__main__":
    app.run(debug=True)