def get_weather_info(condition):
    if "rain" in condition.lower():
        picture = "rainy.jpg"
        sentence = "It's raining today. Don't forget your umbrella!"
    elif "cloud" in condition.lower():
        picture = "cloudy.jpg"
        sentence = "It's cloudy today."
    elif "clear" in condition.lower():
        picture = "clear.jpg"
        sentence = "It's a clear day!"
    else:
        picture = "default.jpg"
        sentence = "Weather condition unknown."
    return picture, sentence