import sys

Matches, Innings, truns, Wckts, tballs, HS = 0, 0, 0, 0, 0, 0


def cric():
    global Wckts, HS, Matches, Innings, truns, tballs
    Out = int(input("1 for out, 2 for not out, 3 to exit="))
    if Out == 1:
        Wckts += 1
    elif Out == 2:
        Wckts += 0
    elif Out == 3:
        print("Thanks for using this program.")
        sys.exit()
    else:
        print("Wrong input given. Try again.")
        cric()
    run = int(input("Runs scored in match="))
    balls = int(input("Enter no. of balls="))
    if run > HS:
        HS = run
    Matches += 1
    Innings += 1
    truns += run
    tballs += balls
    avg = truns / Wckts
    match(run, balls)
    career()
    cric()


def match(run, balls):
    print("\nThis match results: \nRuns:", run)
    print("SR:", (run * 100) / balls)


def career():
    print("\nCareer results:")
    print("Matches:", Matches)
    print("Innings:", Innings)
    print("Runs:", truns)
    print("Balls:", tballs)
    print("SR:", round((truns * 100) / tballs, 2))
    print("Avg:", truns / Wckts)
    print("HS", HS)
    print("\n")


cric()
