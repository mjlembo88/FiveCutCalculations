def five_cut():


    a = float(input(print('Measurement A')))
    b = float(input(print('Measurement B')))
    l = float(input(print('Cut 5 lenght')))
    p = float(input(print('Pivot lenght')))

    c = a - b
    off_set_per_in = c / 4
    off_set = (c / 4)/l
    print(f"the off set amount is : {round(off_set_per_in,5)}in per liner inch")

    move_val = off_set * p

    if off_set_per_in <= .001 and off_set_per_in >= -.001:
        print("Congraulations your sled is perfect! /n No adjustment needed")
    elif move_val > 0:
        print(f"Move fence Backward: {round(move_val,3)}in ")
    else:
        print(f"Move fence Forward: {round(move_val,3) * -1}in")


exit = True

while exit:
    five_cut()
    exit = input("Enter x to exit")
    if exit.lower() == "x":
        exit = False
