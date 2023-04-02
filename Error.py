print("Sri")

# Integar Check

def integar_error(input):
    checker = True
    try:
        int(input)
    except:
        checker = False
    return checker

# String Check

def string_error(input):
    checker = True
    try:
        str(input)
    except:
        checker = False
    return checker

# Double / Float Check

def Double_error(input):
    checker = True
    try:
        float(input)
    except:
        checker = False
    return checker
    

    






