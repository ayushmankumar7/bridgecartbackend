import requests 

from scraper.instagram import get_profile, get_instagram_post
from core.firebase import db, bucket

def add_new_profile(instagram_username):
    profile = get_profile(instagram_username)
    doc_ref = db.collection(f"{instagram_username}").document(u"details")
    doc_ref.set(profile)

def refresh_instagram(instagram_username: str, num_posts: int = 10):
    posts = get_instagram_post(instagram_username, num_posts)
    doc_ref = db.collection(f"{instagram_username}")
    ids = [doc.id for doc in doc_ref.get()]
    for post in posts:
        if post.typename == "GraphImage" and "#bridgecart" in post.caption:
                image_data = requests.get(post.url).content
                blob = bucket.blob(f'{instagram_username}/{post.mediaid}')
                blob.upload_from_string(
                        image_data,
                        content_type='image/jpg'
                    )
                doc_ref.document(f"{post.mediaid}").set({
                    u"media_type": f"{post.typename}",
                    u"caption": f"{post.caption}",
                    u"media_url": f"https://firebasestorage.googleapis.com/v0/b/bridgecart-f6c1f.appspot.com/o/{instagram_username}%2F{post.mediaid}?alt=media",
                })

def get_items(instagram_username):
    doc_ref = db.collection(f"{instagram_username}")
    return [i.to_dict() for i in doc_ref.get()]

def get_item_ids(instagram_username):
    doc_ref = db.collection(f"{instagram_username}")
    return [i.id for i in doc_ref.get()][::-1]

def get_item_by_id(instagram_username, media_id):
    doc_ref = db.collection(f"{instagram_username}").document(f"{media_id}")
    return doc_ref.get().to_dict()