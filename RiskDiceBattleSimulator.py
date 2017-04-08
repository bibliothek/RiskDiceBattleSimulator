import random
import sys


def cli():
    args = sys.argv
    if __file__ in args:
        args.remove(__file__)
    if len(args) < 2 or len(args) > 3:
        print "Wrong number of arguments. Enter the number of attackers and defenders. Optionally you can also define the number of tries."
    else:
        try:
            attackers = int(args[0])
            defenders = int(args[1])
            if len(args) == 3:
                runs = int(args[2])
                run_many(runs, attackers, defenders)
            else:
                print risiko(attackers, defenders)
        except ValueError:
            print "Wrong Arguments. Please enter the numbers of attackers, defenders and tries separated by spaces."


def w6():
    return random.randrange(1, 7)


def risiko(attackers, defenders):
    #termination condition
    if attackers <= 1:
        return "Defenders win. %i defenders remain." % defenders
    if defenders <= 0:
        return "Attackers win. %i attackers remain." % attackers

    #If the number of attackers is 2, only 1 may attack.
    if attackers == 2:
        a = w6()
        v = [w6()]
        if defenders >= 2:
            v.append(w6())
            v.sort()
        if a > v[-1]:
            defenders -= 1
        else:
            attackers -= 1
        return risiko(attackers, defenders)


    #2 or 3 attackers are attacking.
    a = [w6(), w6()]
    if attackers >= 4:
        a.append(w6())

    a.sort()
    if defenders >= 2:
        v = [w6(), w6()]
        v.sort()
        if a[-1] > v[-1]:
            defenders -= 1
        else:
            attackers -= 1
        if a[-2] > v[-2]:
            defenders -= 1
        else:
            attackers -= 1
    elif defenders == 1:
        v = w6()
        if a[-1] > v:
            defenders -= 1
        else:
            attackers -= 1
    return risiko(attackers, defenders)


def run_many(runs, attackers, defenders):
    victory_a = 0
    victory_d = 0
    for i in range(runs):
        a = risiko(attackers, defenders)
        if "Attackers" in a:
            victory_a += 1
        else:
            victory_d += 1
    print "The attackers won %i times, the defenders %i times." % (victory_a, victory_d)


if __name__ == "__main__":
    cli()