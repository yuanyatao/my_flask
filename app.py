from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 设置上传文件的保存目录
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return upload()
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # 获取上传的文件
    uploaded_files = request.files.getlist('file')

    # 创建保存文件的文件夹
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    filenames = []
    for file in uploaded_files:
        if file:
            # 保存文件到服务器
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            filenames.append(filename)

    return render_template('index.html', filenames=filenames)

@app.route('/process', methods=['POST'])
def process():
    action = request.form.get('action')
    filename = request.form.get('filename')

    # 在这里添加相应按钮点击事件的处理逻辑
    # 根据 action 的值进行相应的操作

    return render_template('index.html', filenames=[filename])

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask
# from flask import url_for  # 
# from markupsafe import escape
# from flask import Flask, render_template
# name = "YT's watchlist"
# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]
# app = Flask(__name__) #注册

# @app.route('/') #添加多个装饰器
# @app.route('/index')
# @app.route('/home')   
# def index():
#     return render_template('index.html', name=name, movies=movies) #把参数传入

# @app.route('/user/<name>')
# def user_page(name):
#     return f'User: {escape(name)}'

# @app.route('/test')
# def test_url_for():
#     # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
#     print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
#     # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
#     print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
#     print(url_for('user_page', name='peter'))  # 输出：/user/peter
#     print(url_for('test_url_for'))  # 输出：/test
#     # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
#     print(url_for('test_url_for', num=2))  # 输出：/test?num=2
#     return 'Test page'