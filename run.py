import flask
import random
import os


app = flask.Flask(__name__)

# 主页展示templates/index.html
@app.route('/')
def index():
    return flask.render_template('index.html')

# 随机返回一个图片的URL
@app.route('/random_pic')
def random_image_display():
    # 指定图片文件夹路径
    image_folder = os.path.join(app.static_folder, 'pic', 'club')
    
    # 获取文件夹中所有文件
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    
    # 如果没有图片文件，返回404错误
    if not images:
        return "No images found", 404
    
    # 随机选择一个图片文件
    selected_image = random.choice(images)
    
    # 返回图片文件，使其在浏览器中展示
    return flask.send_from_directory(image_folder, selected_image)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9527)