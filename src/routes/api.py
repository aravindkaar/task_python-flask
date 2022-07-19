from flask import request,render_template
import requests
import json

def api(routes):
    @routes.route('/home')
    def index():
        # open api request to json placeholder API
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return render_template('index.html',data = response.json()[:20])
