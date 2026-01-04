import pyotp 
import time
import datetime

secret_key = 'JBSWY3DPEHPK3PXP'
totp = pyotp.TOTP(secret_key)


def get_current_totp_value():
    return totp.now()

def get_time_remaining():
    return totp.interval - datetime.datetime.now().timestamp() % totp.interval

def verify(totp_entered):
    return totp.verify(totp_entered)