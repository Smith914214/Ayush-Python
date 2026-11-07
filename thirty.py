word = " Saurabh "

for y in range(15, -15, -1):
    for x in range(-30, 30):
        # Heart equation
        formula = (x*0.05)**2 + (y*0.1)**2 - 1
        if formula**3 - (x*0.05)**2*(y*0.1)**3 <= 0:
            # Print letters from the word
            print(word[(x - y) % len(word)], end="")
        else:
            print(" ", end="")
    print()