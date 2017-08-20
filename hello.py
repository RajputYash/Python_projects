print "hello"
print "let\'s get started"
spy_name = raw_input("what is your name:")
if len(spy_name)>0:
    spy_salutation= raw_input("what we call you(Mr. or Mrs.) :")
    spy_name=spy_salutation + " " + spy_name


    print (spy_name + " " +"what\'s your name ")


    spy_age=0
    spy_rating=0.0
    spy_is_online= False

    spy_age=raw_input("what is your age:")
    spy_age=int(spy_age)
    if (spy_age)>18:
        print spy_age

        spy_rating=raw_input("what is your rating:")
        print "Great ace"
        spy_rating=float(spy_rating)
        if spy_rating>4.5:
             print "Great ace"

        elif spy_rating >3.5 and spy_rating <=4.5:
            print "you are the good ones"


        elif spy_rating >2.5 and spy_rating <=3.5:
             print "you can always do better"
        else:
            print "work hard"

        spy_is_online=True

        print"Authentication completed" + " " +  spy_name + " " + "age:" + " " +str(spy_age) +" " + "rating:" + " " + str(spy_rating) + " "  + " online_status:" + str(spy_is_online) + " " + " " "proud to have you on board"

    else:
        print "age is invalid"

else:
    print "you do not enter valid name"



