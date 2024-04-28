import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
special_characters="!@#$%^&*,./<>?;\_"

upper, lower, nums,special = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if special:
    all += special_characters

length=20
password=" ".join(random.sample(all,length))
print(password)