import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import dotenv_values
import json

# pull env variables
config = dotenv_values(".env")

# cred file path
cred_file_path = './src/config/esg-analytics.json'

cred_object = {
    "type": config['TYPE'],
    "project_id": config['PROJECT_ID'],
    "private_key_id": config['PRIVATE_KEY_ID'],
    "private_key": config['PRIVATE_KEY'],
    "client_email": config['CLIENT_EMAIL'],
    "client_id": config['CLIENT_ID'],
    "auth_uri": config['AUTH_URI'],
    "token_uri": config['TOKEN_URI'],
    "auth_provider_x509_cert_url": config['AUTH_PROVIDER_X509_CERT_URL'],
    "client_x509_cert_url": config['CLIENT_X509_CERT_URL'],
}


with open(cred_file_path, "w") as outfile:
    json.dump(cred_object, outfile)


cred = credentials.Certificate(cred_file_path)
firebase_admin.initialize_app(cred)
