from flask import Flask, request
from flask_cors import *

import qa

app = Flask(__name__)
CORS(app, supports_credentials=True)#配置跨域


# 这里默认的是get请求方式
@app.route('/hello', methods=["GET"])
@cross_origin(supports_credentials=True)#跨域
def hello_world():
    try:
        para = request.args['code']#获取链接里的code参数
        str1 = qa.answer_rule(para)#调用方法获取返回值给前端
        return str1
    except:
        return "客服没有包含相关信息哦，请进行其他的提问捏，或致电人工客服捏" #如果脚本无法找到返回值返回此信息


if __name__ == '__main__':
    # 这里host是后端地址，这里写0.0.0.0，表示的是这个接口在任何服务器上都可以被访问的到，只需要前端访问该服务器地址就可以的，port是该接口的端口号
    # debug = True ,表示的是，调试模式，每次修改代码后不用重新启动服务
    app.run(host='0.0.0.0', port=8081, debug=True)
