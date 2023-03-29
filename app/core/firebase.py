import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

cred = credentials.Certificate('certificates/firestore.json')

firebase_admin.initialize_app(cred, {
    'storageBucket': 'bridgecart-f6c1f.appspot.com'
})

db = firestore.client()
bucket = storage.bucket()