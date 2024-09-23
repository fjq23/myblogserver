import flask

# 用当前脚本名称实例化Flask对象，方便flask从该脚本文件中获取需要的内容
app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template('index.html')

# 启动一个本地开发服务器，激活该网页
app.run()


