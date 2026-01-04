import pyotp 
import time
import datetime

totp = pyotp.TOTP('JBSWY3DPEHPK3PXP')
totp_t1 = totp.now() # => returns the OTP (hash) value at t1
t1 = datetime.datetime.now()

print(f"At {t1}, the TOTP value is TOTP1={totp_t1}")
print("Compare current TOTP value with TOTP1:",totp.verify(totp_t1)) # => True

def get_time_remaining():
time_remaining = totp.interval - datetime.datetime.now().timestamp() % totp.interval
print(f"Time remaining for current OTP: {time_remaining} seconds")

print("Waiting for 30 seconds...")
time.sleep(30)

t2 = datetime.datetime.now()
totp_t2 = totp.now() # => returns the OTP value at t2

print(f"At {t2}, the TOTP value is TOTP2={totp_t2}")
print("Compare current TOTP value with TOTP1:",totp.verify(totp_t1)) # => False
print("Compare current TOTP value with TOTP2:",totp.verify(totp_t2)) # => False
