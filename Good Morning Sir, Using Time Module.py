import time
name = str(input("Enter Your Sweet Name -  ")).title()
hour = int(time.strftime("%H"))
if hour>=0 and hour<12:
    print("Good Morning Sir, ",name)
    print("I Hope Your Day Will Go Good")
elif hour>=12 and hour<=17:
    print("Good Afternoon Sir,",name)
    print("Hope Your Remaining Day Will Go Good")
elif hour>17 and hour<=20:
    print("Good Evening Sir, ",name)
    print("Hope You Will Spent A Good Time In Evening Without Any Bitches With You")
elif hour>20 and hour<24:
    print("Good Night Sir, ",name)
    print("Hope You Will Have A Calm/Boom Night")
else:
    print("Please Check Your Clock")
    print("Enter Your/Someone's Name")
print("Here We Go \n Hope You Enjoyed Our Service",name)
