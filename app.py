from weather import get_location_key, get_weather_data

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    city_name = request.form['place']
    weather_info = get_weather_data(city_name)
    return render_template('results.html', weather_info=weather_info)

if __name__ == '__main__':
    app.run(debug=True)
