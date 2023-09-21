from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return '没有选择文件'

    file = request.files['file']
    if file.filename == '':
        return '没有选择文件'

    if file:
        filename = file.filename
        file.save(os.path.join('static/uploads', filename))
        return render_template('index.html', filenames=get_filenames_from_folder('uploads'))

@app.route('/process/button1', methods=['POST'])
def process_button1():
    filenames = get_filenames_from_folder('products')
    # 处理按钮1的逻辑
    return render_template('index.html', filenames=filenames)

@app.route('/process/button2', methods=['POST'])
def process_button2():
    filenames = get_filenames_from_folder('products')
    # 处理按钮2的逻辑
    return render_template('index.html', filenames=filenames)

@app.route('/process/button3', methods=['POST'])
def process_button3():
    filenames = get_filenames_from_folder('products')
    # 处理按钮3的逻辑
    return render_template('index.html', filenames=filenames)

@app.route('/process/button4', methods=['POST'])
def process_button4():
    filenames = get_filenames_from_folder('products')
    # 处理按钮4的逻辑
    return render_template('index.html', filenames=filenames)

def get_filenames_from_folder(folder):
    folder_path = os.path.join('static', folder)
    filenames = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            filenames.append(filename)
    return filenames

if __name__ == '__main__':
    app.run()
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