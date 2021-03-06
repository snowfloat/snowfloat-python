"""Client global settings."""
import os
import ConfigParser

HTTP_TIMEOUT = 10
HTTP_RETRIES = 3
HTTP_RETRY_INTERVAL = 5

HOST = 'api.snowfloat.com:443'
API_KEY_ID = ''
API_SECRET_KEY = ''
USER_API_KEY_ID = ''
USER_API_SHARING_KEY = ''

DEFAULTS = {
    'host': 'api.snowfloat.com:443',
    'user_api_key_id': '',
    'user_api_sharing_key': ''
    }

CONFIG = ConfigParser.ConfigParser(DEFAULTS)
for loc in (os.curdir, os.path.expanduser("~"), "/etc/snowfloat"):
    try:
        source = open(os.path.join(loc, "snowfloat.conf"))
        CONFIG.readfp(source)
        API_KEY_ID = CONFIG.get('snowfloat', 'api_key_id')
        API_SECRET_KEY = CONFIG.get('snowfloat', 'api_secret_key')
        HOST = CONFIG.get('snowfloat', 'host')
        USER_API_KEY_ID = CONFIG.get('snowfloat', 'user_api_key_id')
        USER_API_SHARING_KEY = CONFIG.get('snowfloat', 'user_api_sharing_key')
        source.close()
        break
    except IOError:
        pass
