import requests
from apscheduler.schedulers.background import BackgroundScheduler

def ping_server():
    try:
        url = "https://srijan-dev.onrender.com/"
        response = requests.get(url)
        print("Pinged:", response.status_code)
    except Exception as e:
        print("Ping failed:", e)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ping_server, 'interval', minutes=10)
    scheduler.start()
