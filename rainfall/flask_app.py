import flask
from rainfall import RainfallData
import yaml
import urllib
from urllib import request
import requests

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger('__name__')
logger.info('Rainfall Service Started' )

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    try:
        with open("config/app.config", "r") as f:
            config = yaml.safe_load(f)
        r = requests.get(config['url'])
        if r.status_code == 200:
            logger.info('Fetching data from %s' % config['url'])
            request_data = urllib.request.urlopen(config['url'])
            listed_data = yaml.safe_load( request_data )
            rainfallObj = RainfallData(listed_data, config['location'])
            return ("<h2 style='color:blue'>"+rainfallObj.get_rainfall_data() +"</h2>")
    except:
        logger.error('Something wrong with config file or API site is not available.')
    return ("Site is in maintenance mode, and will get back soon !")

if __name__ == '__main__':
    app.run()