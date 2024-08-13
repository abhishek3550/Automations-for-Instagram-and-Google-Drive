#Link https://instaloader.github.io/basic-usage.html#download-pictures-from-instagram
#pip install instaloader

import instaloader
username = input("enter insta username : ")
instaloader.Instaloader().download_profile(username,profile_pic_only=False)