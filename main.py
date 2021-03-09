import instaloader #pip install instaloader

pic = instaloader.Instaloader()
user = input("Enter the instagram id: ")
print(pic.download_profile(user, profile_pic_only = True))