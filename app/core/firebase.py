import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from firebase_admin import auth as firebase_auth
cred = credentials.Certificate('admin/credentials/firestore.json')

firebase_admin.initialize_app(cred, {
    'storageBucket': 'bridgecart-f6c1f.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()

auth = firebase_auth