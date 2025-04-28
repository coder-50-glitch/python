import random
while True:
    ch = input("enter a choice(rock, paper, sissor): ")
    posible_act = ["rock", "paper", "sissor"]
    comp_act = random.choice(posible_act)
    print(f"\n your choice{ch}, computer chose{comp_act}. \n")
    if( ch == comp_act):
        print("draw")
    elif(ch=="rock"):
        if(comp_act == "paper"):
            print("WIN")
        else:
            print("LOSE")
    elif(ch=="sissor"):
        if(comp_act == "paper"):
            print("WIN")
        else:
            print("LOSE")
    elif(ch=="paper"):
        if(comp_act == "rock"):
            print("WIN")
        else:
            print("LOSE")
    play_again=input("play again(y/n)")
    if(play_again !="y"):
        break
    