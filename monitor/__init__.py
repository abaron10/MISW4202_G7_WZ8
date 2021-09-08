from .app import *
import threading

def ping_servers():
    verify_life_servers()
    threading.Timer(5.0,ping_servers).start()

ping_servers()