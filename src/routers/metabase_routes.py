import jwt
import time
from config.app import app


def get_metabase_token():
    METABASE_SITE_URL = "https://esg-analytics.herokuapp.com"
    METABASE_SECRET_KEY = "9cf6478841b9bd9dc44668b68b27b8f9ce43fb47a930be05987c37819fcd3f70"
    payload = {
        "resource": {"dashboard": 1},
        "params": {
        },
        "exp": round(time.time()) + (60 * 120)  # 2-hour expiration
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + \
        token + "#theme=night&bordered=true&titled=true"

    return iframeUrl


@app.get("/metabaseconfig/{uid}")
def get_metabase_config(uid):
    if uid != False:
        return get_metabase_token()

    return 'invalid uid'
