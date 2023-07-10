import time
import pyotp

key = pyotp.random_base32()

print (key)

totp = pyotp.TOTP(key)

print (totp.now())

time.sleep(30)
 