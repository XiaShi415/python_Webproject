from flask import Flask,render_template
app = Flask(__name__) #创建Flask类实例

@app.route('/root/')     #使用route装饰器，告诉哪个URL才能触发我们的函数
def hellow_world():
    return("根目录")

@app.route('/profile/<int:uid>/')     #使用route装饰器，告诉哪个URL才能触发我们的函数
def hellow_world_shild(uid):
    user = {'nickname':'Xiashi  '}
    return render_template("profile.html",user = user)

if __name__ == '__main__':
    app.run(debug=True)