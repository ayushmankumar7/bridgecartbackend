import instaloader

loader = instaloader.Instaloader()

def get_profile(username: str):
    profile = instaloader.Profile.from_username(loader.context, f"{username}")
    return {
        "username": profile.username,
        "full_name": profile.full_name,
        "biography": profile.biography,
        "external_url": profile.external_url,
        "profile_pic_url": profile.profile_pic_url,
        "is_business_account": profile.is_business_account,
        "business_category_name": profile.business_category_name,
        "media_count": profile.mediacount,
        "follower_count": profile.followers,
        "following_count": profile.followees,
    }

def get_instagram_post(username: str, num_post: int = 10):
    profile = instaloader.Profile.from_username(loader.context, f"{username}")
    posts = []
    for i, post in enumerate(profile.get_posts()):
        posts.append(post)
        if i == num_post:
            break
    return posts

