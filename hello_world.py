from flask import Flask

app = Flask(__name__)

def wrap_html(message):
    html = """
        <html>
        <head>
            <meta name="description" content="a whale fan site">
            <meta name="keywords" content="whale,whales,docker,fun,github,circleci">
        </head>
        <body>
            <div style='font-size:80px;'>
            <center>
                <image src="https://www.docker.com/sites/default/files/social/docker_facebook_share.png">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
    message = 'I like whales!'
    html = wrap_html(message)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
