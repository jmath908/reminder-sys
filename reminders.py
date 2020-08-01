#A reminder system for timed events


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
                   icon_path="",
                   duration=remT)
    while toaster.notification_active(): time.sleep(0.1)

    
#def showreminders():
    
