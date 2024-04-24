from flask import Flask, render_template, request
import requests
import os

api_key = os.getenv('API_KEY')

app = Flask(__name__) # invoke the Flask class

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    
    elif request.method == 'POST':
        location = request.form['location']
        request_string = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        weather_result = requests.get(request_string)
        weather_result = weather_result.json()
        return render_template('post.html',content=weather_result)

if __name__ == '__main__':
    app.run() # Start the server listening for requests