import firebase_admin
from firebase_admin import credentials, auth
import os
import json


# cred file path
cred_file_path = './src/config/esg-analytics.json'

cred_object = {
    "type": os.environ['TYPE'],
    "project_id": os.environ['PROJECT_ID'],
    "private_key_id": os.environ['PRIVATE_KEY_ID'],
    "private_key": os.environ['PRIVATE_KEY'],
    "client_email": os.environ['CLIENT_EMAIL'],
    "client_id": os.environ['CLIENT_ID'],
    "auth_uri": os.environ['AUTH_URI'],
    "token_uri": os.environ['TOKEN_URI'],
    "auth_provider_x509_cert_url": os.environ['AUTH_PROVIDER_X509_CERT_URL'],
    "client_x509_cert_url": os.environ['CLIENT_X509_CERT_URL'],
}

# Create file from credentials object
with open(cred_file_path, "w") as outfile:
    json.dump(cred_object, outfile)

# Initialize Admin SDK by specifying file path
cred = credentials.Certificate(cred_file_path)
firebase_admin.initialize_app(cred)

# Remove file once SDK init is done
os.remove(cred_file_path)
