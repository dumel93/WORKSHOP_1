print('Think about a number. I will guess it in max 10 questions. Answer by yes or no.')


def mindreader():
    min = 0
    max = 1000
    for i in range(1, 11):
        guess = int((max - min) / 2 + min)
        print(guess)
        a = input("Did I guess?")
        if a == "yes":
            print("HUUURAAA")
            return None
        elif a == "no":
            duzo = input('To much?')
            if duzo == "yes":
                max = guess
                i += 1
                continue
            elif a == "no":
                less = input('To less?')
                if less == "yes":
                    min = guess
                    i += 1
                    continue
                elif less == "no":
                    print('Do not cheat.')
                    continue
            else:
                print("Enter either yes/no")

            continue

        else:
            print("Enter either yes/no")

mindreader()