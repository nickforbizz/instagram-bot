from time import sleep
from instapy import InstaPy
from instapy import smart_run



username = ''
password = ''
session = InstaPy(username="mkenyadaima.co.ke", 
                password="Mkenyadaima@2022", 
                headless_browser = False)


with smart_run(session):
    session.set_relationship_bounds(enabled=True, 
                                    delimit_by_numbers=True, 
                                    max_followers=9500, 
                                    min_followers=50, 
                                    min_following=50)
    # session.set_quota_supervisor(enabled=True, 
    #                             peak_comments_daily=240, 
    #                             peak_comments_hourly=21)
    session.like_by_tags(["travel", "photography", "arts", "fashion", "landscape", "summer"],amount=35)
    session.set_dont_like(["naked", "nsfw", "massage", "sex"])
    session.set_do_follow(True, percentage=25)
    session.set_do_comment(enabled=True, percentage=25)
#     comments= [
#                     # either "icecave" OR "ice_cave" will satisfy this:
#                     {'mandatory_words': ["icecave", "ice_cave"], 'comments': ["Nice shot. Ice caves are amazing", "Cool. Aren't ice caves just amazing?"]},

#                     # either "high_mountain" OR ("high" AND "mountain") will satisfy this:
#                     {'mandatory_words': ["high_mountain", ["high", "mountain"]], 'comments': ["I just love high mountains"]},

#                     # Only ("high" AND "tide" together) will satisfy this:
#                     {'mandatory_words': [["high", "tide"]], 'comments': ["High tides are better than low"]},

#                     # Only "summer" AND ("lake" OR "occean") will satisfy this:
#                     {'mandatory_words': [["summer", ["lake", "occean"]]], 'comments': ["Summer is so fun"]}

#                 ]
# session.set_comments(comments)
