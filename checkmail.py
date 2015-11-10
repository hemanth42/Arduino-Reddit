import arduino_reddit, sys

    
if len(sys.argv) >= 2:
    try:
        username = sys.argv[1]
        password = sys.argv[2]
    except:
        print("Enter both the username and password")
        exit()
        
    if len(sys.argv) > 3:
        port = sys.argv[3]        
        arduino_reddit.mailcheck(username, password, port)
    else:
        arduino_reddit.mailcheck(username, password)

else:
    username = input("Enter Username: \n")
    password = input("Enter Password: \n")
    arduino_reddit.mailcheck(username, password)
