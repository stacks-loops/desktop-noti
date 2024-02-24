import time 
import notify2 
from topnews import topStories 

# path to notification window icon 
ICON_PATH = "https://i.pinimg.com/564x/9d/ee/d5/9deed540271a1e024084f8cb1e675eec.jpg"
  
# fetch news items 
newsitems = topStories() 
  
# initialise the d-bus connection 
notify2.init("News Notifier") 
  
# create Notification object 
n = notify2.Notification(None, icon = ICON_PATH) 
  
# set urgency level 
n.set_urgency(notify2.URGENCY_NORMAL) 
  
# set timeout for a notification 
n.set_timeout(10000) 
  
for newsitem in newsitems: 
  
    # update notification data for Notification object 
    n.update(newsitem['title'], newsitem['description']) 
  
    # show notification on screen 
    n.show() 
  
    # short delay between notifications 
    time.sleep(15) 

    notify2.init("News Notifier")
    n = notify2.Notification(None, icon = ICON_PATH)
    n.set_timeout(10000)
    n.update(newsitem['title'], newsitem['description'])
    n.show()


