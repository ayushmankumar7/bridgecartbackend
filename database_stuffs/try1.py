import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import instaloader
import requests
from firebase_admin import storage

# create an instance of Instaloader class
loader = instaloader.Instaloader()

# Use a service account.
cred = credentials.Certificate('bridgecart-f6c1f-firebase-adminsdk-xoszl-3ba1379dba.json')
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'bridgecart-f6c1f.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()

def add_new_profile(instagram_username):
    profile = instaloader.Profile.from_username(loader.context, f"{instagram_username}")
    doc_ref = db.collection(f"{instagram_username}").document(u"details")
    doc_ref.set({
        u"username": f"{instagram_username}",
        u"full_name": f"{profile.full_name}",
        u"profile_pic_url": f"{profile.get_profile_pic_url()}",
        u"is_business_account": f"{profile.is_business_account}",
        u"business_category_name": f"{profile.business_category_name}",
        u"media_count": f"{profile.mediacount}",
        u"follower_count": f"{profile.followers}",
        u"following_count": f"{profile.followees}",
    })

def refresh_instagram(instagram_username, num_posts=10):
    profile = instaloader.Profile.from_username(loader.context, f"{instagram_username}")
    doc_ref = db.collection(f"{instagram_username}")
    ids = [i.id for i in doc_ref.get()]
    np = 0
    for post in profile.get_posts():
        if post.mediaid in ids:
            continue
        else:
            np += 1
            # if post.typename == "GraphImage":
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
            # elif post.typename == "GraphVideo":
            #     doc_ref.document(f"{post.mediaid}").set({
            #         u"media_type": f"{post.typename}",
            #         u"caption": f"{post.caption}",
            #         u"media_url": f"{post.video_url}",
            #     })

            # elif post.typename == "GraphSidecar":
            #     doc_ref.document(f"{post.mediaid}").set({
            #         u"media_type": f"{post.typename}",
            #         u"caption": f"{post.caption}",
            #         u"media_url": [x.display_url for x in post.get_sidecar_nodes()],
            #     })

        if np == num_posts:
            break
            
def get_items(instagram_username):
    doc_ref = db.collection(f"{instagram_username}")
    return [i.to_dict() for i in doc_ref.get()]

def get_item_ids(instagram_username):
    doc_ref = db.collection(f"{instagram_username}")
    return [i.id for i in doc_ref.get()][::-1]

def get_item_by_id(instagram_username, media_id):
    doc_ref = db.collection(f"{instagram_username}").document(f"{media_id}")
    return doc_ref.get().to_dict()

# print(get_item_ids("ayushmankumar7"))
# add_new_profile("_flavoursome_bakery_kolkata_")
# refresh_instagram("_flavoursome_bakery_kolkata_")

# print(get_items("ozswell.ind")[::-1])

# doc_ref = db.collection(f"ayushmankumar7")
# # print(dir(doc_ref))
# print(len(doc_ref.get()))
# print(doc_ref.get())

# for i in doc_ref.get():
#     print(dir(i))
#     print(i.id)

# profile = instaloader.Profile.from_username(loader.context, f"ayushmankumar7")
# c = 0
# for i in profile.get_posts():
#     print(i.caption)
#     print(i.video_url)
#     print(i.url)
#     print(i.mediaid)
#     print(i.mediacount)
#     print(i.typename)
#     if i.typename == "GraphSidecar":
#         print(i.get_sidecar_nodes())
#         for x in i.get_sidecar_nodes():
#             print(x.display_url)
#     print(dir(i))
#     c += 1 

#     if c == 10:
#         break
    # loader.download_post(post, target="profile_pictures")

# import requests 

# requests.get("https://instagram.fccu3-1.fna.fbcdn.net/v/t51.2885-15/326692920_738904801189037_5783299639739571847_n.webp?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fccu3-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=Kya-BFyH-4QAX8NXP1G&edm=AOQ1c0wBAAAA&ccb=7-5&ig_cache_key=MzAyMjIxNTkyMTIwMTAwOTIzNQ%3D%3D.2-ccb7-5&oh=00_AfACkSY4b8zXBNg38KoQHaybNvj7Ac2tWO8LDdmIH4WN2Q&oe=6424D4E2&_nc_sid=8fd12b").content

# import sys
# import requests
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage
# import urllib

# # image_url = "https://instagram.fccu3-1.fna.fbcdn.net/v/t51.2885-15/326692920_738904801189037_5783299639739571847_n.webp?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fccu3-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=Kya-BFyH-4QAX8NXP1G&edm=AOQ1c0wBAAAA&ccb=7-5&ig_cache_key=MzAyMjIxNTkyMTIwMTAwOTIzNQ%3D%3D.2-ccb7-5&oh=00_AfACkSY4b8zXBNg38KoQHaybNvj7Ac2tWO8LDdmIH4WN2Q&oe=6424D4E2&_nc_sid=8fd12b" #we pass the url as an argument
# image_url = "https://i.ibb.co/6JxTJJB/Social-Fizz.png"
# # # cred = credentials.Certificate('bridgecart-f6c1f-firebase-adminsdk-xoszl-3ba1379dba.json')
# # # firebase_admin.initialize_app(cred, {
# # #     'storageBucket': 'gs://bridgecart-f6c1f.appspot.com'
# # # })

# # # urllib.request.urlretrieve(image_url, "greenland_04a.png")

# bucket = storage.bucket()


# # print(dir(bucket))
# # print(dir(bucket.get_blob("new_cool_image.jpg")))
# # print(bucket.get_blob("new_cool_image.jpg").bucket)
# # print(bucket.get_blob("new_cool_image.jpg")._get_download_url(bucket.get_blob("new_cool_image.jpg").client))


# image_data = requests.get(image_url).content
# blob = bucket.blob('new_folder/new_cool_image.jpg')
# blob.upload_from_string(
#         image_data,
#         content_type='image/jpg'
#     )
# print(blob.public_url)