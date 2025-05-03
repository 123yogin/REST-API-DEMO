from flask import Flask

app = Flask(__name__)
app.debug = True

try:
    from controllers import controller
except Exception as e:
    print(e)