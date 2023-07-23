

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        if text[3] != "-":
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True
    
message  = "Call me at 412-555-1311 tomorrow. 412-550-1312 is my offce."
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone Number found: " + chunk)
print("Done")

