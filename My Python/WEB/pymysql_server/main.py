from flask import Flask, render_template, request, redirect, url_for
from modules import mod_sql

app = Flask(__name__)

#localhost로 접속했을때
@app.route("/")
def index():
    return render_template("index.html")

#localhost/signup으로 접속했을때
@app.route("/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")
@app.route("/signup", methods=["POST"])
def signup_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _ads = request.form["_ads"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _regitdate = request.form["_regitdate"]

    sql = """
            INSERT INTO user_info VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
    _values = [_id, _password, _name, _phone, _ads, _gender, _age, _regitdate] #컬럼 순서에 맞게
    _db = mod_sql.Database()
    _db.execute(sql, _values)
    _db.commit()
    # print(request.form)
    return redirect(url_for('index'))

@app.route("/login", methods=["POST"])
def login():
    #DB -> SELECT문을 사용 -> index page input ID, PASSWORD 받아와서
    # SELECT문으로 조회
    #결과 값이 존재하면 return "login" 존재하지 않으면 return "Fail"
    # index.html 수정 main.py 수정 둘 다 해야함
    # 1.index.html /login url에 post형식으로 접속
    # ID, PASSWORD print 출력
    # 2.DB에서 SELECT문을 실행해서 user_info table 정보를 print() 출력
    # 3. SELECT문에 조건식을 추가하여 데이터의 유무 판별
    _id = request.form["_id"]
    _password = request.form["_password"]
    # print(_id, _password)  # 1번 완료
    
    sql = """
            SELECT * FROM user_info WHERE ID = %s AND password = %s
            """
    _values = [_id, _password]
    _db = mod_sql.Database()
    result = _db.executeAll(sql, _values)
     # 2번 완료

    if result:
        return render_template("welcome.html", 
                                name = result[0]["name"], 
                                id = result[0]["ID"])
    else :
        return redirect(url_for("index"))


    # return redirect(url_for('index'))
@app.route("/update", methods=["GET"])
def update():
    id = request.args["_id"]
    sql = """ 
            SELECT * FROM user_info WHERE ID = %s 
            """
    values = [id]
    _db = mod_sql.Database()
    result = _db.executeAll(sql, values)
    return render_template("update.html", info = result[0])
@app.route("/update", methods=["POST"])
def update_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _ads = request.form["_ads"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    sql = """ 
            UPDATE user_info SET 
            password = %s, 
            name = %s, 
            phone = %s, 
            gender = %s, 
            age = %s, 
            ads = %s, 
            WHERE ID = %s 
        """
    values = [_password, _name, _phone, _gender, _age, _ads, _id]
    _db = mod_sql.Database()
    _db.execute(sql, values)
    _db.commit()
    return redirect(url_for("/"))

@app.route("/delete", methods=["GET"])
def delete():
    _id = request.args["_id"]
    return render_template("delete.html", id = _id)
@app.route("/delete", methods=["POST"])
def delete_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _db = mod_sql.Database()
    s_sql = """ 
                SELECT * FROM user_info WHERE ID = %s AND password = %s 
            """
    d_sql = """ 
                DELETE FROM user_info WHERE ID = %s AND password = %s 
            """
    _values = [_id, _password]
    result = _db.executeAll(s_sql, _values)

    if result:
        _db.execute(d_sql, _values)
        _db.commit()
        return redirect(url_for('index'))
    else:
        return "패스워드가 일치하지 않습니다."
        
@app.route("/view", methods=["GET"])
def _view():
    # -> sql문 -> user_info left join ads_info ->
    # 조건 user_info ads = ads_info ads ->
    # columns -> user_info : name, ads, age / ads_info : register_count 쿼리문 작성
    # view.html을 render 쿼리문의 결과값을 데이터로 같이 보내주는 코드를 작성
    sql = """ 
            SELECT user_info.name, 
            user_info.ads, 
            user_info.age, 
            ads_info.register_count 
            FROM 
            user_info 
            LEFT JOIN 
            ads_info 
            ON 
            user_info.ads = ads_info.ads 
        """
    _db = mod_sql.Database()
    result = _db.executeAll(sql)
    key = list(result[0].keys())
    return render_template("view.html", result = result, keys = key)

app.run(port=80, debug=True)


# 회원탈퇴
# welcome.html -> /delete url로 접속 -> 로그인 한 ID 값을 전송
# delete -> password를 확인!(delete.html 페이지 생성) ->
# id password가 db에 존재하면 delete
# 존재하지 않으면 패스워드가 맞지 않습니다. 메세지를 페이지에 띄워주는 형식