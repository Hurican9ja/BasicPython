def path(x):
    switcher = {
        '+': float(numbwer1) + float(numbwer2),
        '-': float(numbwer1) - float(numbwer2),
        '*': float(numbwer1) * float(numbwer2),
        '/': float(numbwer1) / float(numbwer2),
    }
    return switcher.get(x, "Mofo insert the correct option")


numbwer1 = float(input("Pwease enter a nyamber OwO : "))
numbwer2 = float(input("Pwease enter another nyamber UwU : "))
print("\n")
process = input("Pwease tell what to do with the nyambers i.e +,-,* or / : ")
result = path(process)
print("\n")
print(str(result) + " is your desired answer nyaa")
