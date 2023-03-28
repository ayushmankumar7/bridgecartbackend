import instaloader

# create an instance of Instaloader class
loader = instaloader.Instaloader()

# get a profile by username
profile = instaloader.Profile.from_username(loader.context, "ayushmankumar7")

print(dir(profile))
print(profile.get_profile_pic_url(), profile.full_name)
# iterate over each post and get its caption and image
for post in profile.get_posts():
    print(post.caption)
    print(post.video_url)
    print(dir(post))
    break 
    # loader.download_post(post, target="profile_pictures")