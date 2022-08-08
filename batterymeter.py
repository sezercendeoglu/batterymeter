import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()

plugged = battery.power_plugged

percent = battery.percent

des=str(percent)+"% \n"

if plugged:
    des+="Battery is charging."

if percent>=30:
    Notification(
        title="Battery Notification",
        description=des,
        duration=10,
        urgency="criticial",



    ).send()