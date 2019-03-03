from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return app


app = create_app()


@app.route('/_check')
def healthcheck():
    return 'OK'



