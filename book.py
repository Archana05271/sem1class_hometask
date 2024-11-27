#1
n=int(input("enter the number of books")) 
l=[] 
for i in range(n):
    books=input()
    l.append(books) 
print("1)display_books 2)add_books 3)remove_book") 
while True:
    option=int(input("enter the option"))
    match option:
        case 1:
            def display_books():
                for i in l:
                    print(i)
            display_books()
        case 2:
            def add_books():
                add=input("Enter the book to be added")
                l.append(add)
                print("After add:",l)
            add_books()
        case 3:
            def remove_books():
                remove=input("Enter the book to be removed")
                l.remove(remove)
                print("After Remove:",l)
            remove_books()
        case _:
            quit()
#2
d={"Shampoo":7,"Masala":10,"biscuits":6} 
print("1)display 2)add 3)remove") 
while True:
    choice=int(input("enter the choice:"))
    match choice:
        case 1:
            def display():
                for i in d.items():
                    print(i)
            display()
        case 2:
            def add_new_product():
                product=input("enter the product name")
                quantity=int(input("enter the product's quantity:"))
                d[product]=quantity
                print("after adding products and quantity:",d)
            add_new_product()
        case 3:
            def remove():
                remove=input("Enter the removing product:")
                if remove in d:
                    del d[remove]
                    print("after removing the product:",d)
            remove() 
        case _:
            quit()
