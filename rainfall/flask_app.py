import flask
from rainfall import RainfallData
import yaml
import urllib
from urllib import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    with open("config/app.config", "r") as f:
        config = yaml.safe_load(f)
    x = urllib.request.urlopen(config['url'])
    listed_data = yaml.safe_load(x)
    rainfallObj = RainfallData(listed_data, config['location'])
    #rainfallObj = RainfallData('{}', config['location'])
    return (rainfallObj.get_rainfall_data())

if __name__ == '__main__':
    app.run()