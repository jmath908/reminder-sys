#A reminder system for timed events

##toaster.show_toast("Hello World!!!",
##                   "Python is 10 seconds awsm!",
##                   icon_path="custom.ico",
##                   duration=10)
##
##toaster.show_toast("Example two",
##                   "This notification is in it's own thread!",
##                   icon_path=None,
##                   duration=5,
##                   threaded=True)
# Wait for threaded notification to finish
##while toaster.notification_active(): time.sleep(0.1)
from win10toast import ToastNotifier
toaster = ToastNotifier()
import time
val = input("Add a reminder? (y/n)") 
if(val=="y"):
    remindName = input("What would you like to be reminded of?")
    remindDesc = input("Enter short description")
    remindTime = input("When would you like the reminder? (enter minute value)")
    remT = float(remindTime)
    toaster = ToastNotifier()
    time.sleep(remT*60)
    toaster.show_toast(remindName,
                   remindDesc,
                   icon_path="stcross.png",
                   duration=remT)
    while toaster.notification_active(): time.sleep(0.1)

    
#def showreminders():
    
