from flask import Flask
from flask import request
import requests,re
#################################
app = Flask(__name__)
#################################
#################################

#I just want to be able to manipulate the parameters
@app.route('/tiktok', methods=['GET', 'POST'])
def login():
    url = request.args.get('url')
    try:
        u = (f'https://godownloader.com/api/tiktok-no-watermark-free?url={url}&key=godownloader.com')
        req = requests.get(u)
        res = req.content
        res1 = str(res)
        res2 = re.findall(r'video_no_watermark":"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*")',res1)
        res3 = str(res2)
        res4 = res3.split("\"")
        res5 = res4[0]
        finish = res5[3:]
        return finish
    except:KeyError
    return " Invalid url "
#################################

if __name__ == '__main__':
    app.run()
