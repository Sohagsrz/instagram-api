import instaloader
import json
# get profile info instaloader
ig = instaloader.Instaloader() 

L = instaloader.Instaloader()
# media by id
media = instaloader.Post.from_shortcode(L.context, "C6rhDMIP4VX")

# dump all data
# encode jso and print preety
show = media._asdict()
 
# save as json in a file
with open("xdata.json", "w") as f:
    f.write(json.dumps(show, indent=4))
# reel get
reel = instaloader.Post.from_shortcode(L.context, "C6VY39sxdrS")
# dump all data
# encode jso and print preety
show = reel._asdict()
print(show)
posts = instaloader.Profile.from_username(L.context, "sohagsrz")
# dump all data
# encode jso and print preety
show = posts._asdict()
print(show)
print(posts.username)
print(posts.userid)
print(posts.biography)