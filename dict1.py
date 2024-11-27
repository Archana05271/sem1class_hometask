#1
dict={"Lakme":["Foundation","Matte Finish Lipstick","Eyelinear","Facewash"],
      "Maybelline":["Pot Kajal","Concealer","Mascara","Powder","Primer"]
      }
costimetic=input().capitalize()
if costimetic in dict:
    print(f"List the {costimetic} products")
    for i in dict[costimetic]:
        print("->",i)
#2
d=int(input())
e=int(input())
operation=int(input())
match operation:
    case 1:
        a=d+e
        print(f"sum={a}")
    case 2:
        a=d-e
        print(f"sub={a}")
    case 3:
        a=d*e
        print(f"mul={a}")
    case 4:
        a=d/e
        print(f"div={a}")
    case 5:
        a=d**e
        print(f"exp={a}")
    case _:
        print("Invalid error")

    

    

              

              
              
              
              

