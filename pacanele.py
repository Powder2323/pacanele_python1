import random

#[ '📘' , '📦', '✏️', '🌯', '⭐️', '💎' , '🌌']  10 5 4 3 2 1 1
slots_counter = [0, 0, 0, 0, 0, 0, 0]
x = [0, 0, 0]

credit = 100
credit_early = credit
print("Nr de credite:", credit)
ok = True
while ok:
    n = int(input("Introdu nr de credite sa pariati: "))
    if(n<=credit):
        ok = False
    else:
        print("Nu aveti suficiente credite, mai aveti", credit,"de credite")
        
rotiri = int(input("Sa se zica nr de rotiri: "))
for i in range(rotiri):
    for counter in range(3):
        x[counter] = random.randint(1, 26)
    for counter in range(3):
        if(x[counter]<=5 or (x[counter]>20 and x[counter]<=25)):
            x[counter] = '📘'
            slots_counter[0] += 1
        elif(x[counter]>5 and x[counter]<=10):
            x[counter] = '📦'
            slots_counter[1] += 1
        elif(x[counter]>10 and x[counter]<=14):
            x[counter] = '✏️'
            slots_counter[2] += 1
        elif(x[counter]>14 and x[counter]<=17):
            x[counter] = '🌯'
            slots_counter[3] += 1
        elif(x[counter]>17 and x[counter]<=19):
            x[counter] = '⭐️'
            slots_counter[4] += 1
        elif(x[counter]==20):
            x[counter] = '💎'
            slots_counter[5] += 1
        else:
            x[counter] = '🌌'
            slots_counter[6] += 1

    print('')
    print(f'{x[0]} | {x[1]} | {x[2]}')
    print('')

    credit -= n

    if(slots_counter[0] == 2):
        credit += n * 0.5
        print(f'Ai castigat {n * 0.5} credite')
    elif(slots_counter[0] == 3):
        credit += n * 1
        print(f'Ai castigat {n * 1} credite')
    elif(slots_counter[1] == 2):
        credit += n * 1
        print(f'Ai castigat {n * 1} credite')
    elif(slots_counter[1] == 3):
        credit += n * 3
        print(f'Ai castigat {n * 3} credite')
    elif(slots_counter[2] == 2):
        credit += n * 2
        print(f'Ai castigat {n * 2} credite')
    elif(slots_counter[2] == 3):
        credit += n * 5
        print(f'Ai castigat {n * 5} credite')
    elif(slots_counter[3] == 2):
        credit += n * 4
        print(f'Ai castigat {n * 4} credite')
    elif(slots_counter[3] == 3):
        credit += n * 8
        print(f'Ai castigat {n * 8} credite')
    elif(slots_counter[4] == 2):
        credit += n * 5
        print(f'Ai castigat {n * 5} credite')
    elif(slots_counter[4] == 3):
        credit += n * 15
        print(f'Ai castigat {n * 15} credite')
    elif(slots_counter[5] == 2):
        credit += n * 20
        print(f'Ai castigat {n * 20} credite')
    elif(slots_counter[5] == 3):
        credit += n * 100
        print(f'Ai castigat {n * 100} credite')
    else:
        print("Nu ai castigat nimic")
        credit += 0

    slots_counter = [0, 0, 0, 0, 0 ,0, 0]
    x = [0, 0, 0]
    print(f'Nr de credite: {credit}')
    if(i!=rotiri-1):
        enter = input('Apasati enter pentru a roti in continuare')


print(f'Nr de credite finale: {credit}')
if(credit<credit_early):
    print(f'Ai iesit pe minus cu {credit_early - credit}')
elif(credit>credit_early):
    print(f'Ai iesit pe plus cu {credit-credit_early}')
else:
    print("Nu ai iesit pe profit")