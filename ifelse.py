print "You are in a dark room. Open door #1 or door #2?"

door = raw_input("> ")

if "1" in door:
    print "Fire everywhere. #1 hit fire alarm? #2 run in circles?"
    
    decision = raw_input("> ")

    if "1" in decision:
        print "probably a good idea"
    elif "2" in decision:
        print "you panicked, ded."
    else:
        print "you should be more decisive"
elif "2" in door:
    print "you made it to the land of beauty and wealth and joy and peace, good job"
