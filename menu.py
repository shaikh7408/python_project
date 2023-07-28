from app import books
USER_CHOICE='''
Enter one of following
-'b' took at 5 star book
-'c' to took at the cheapest book
-'n' to just get next avialbe book
-'q' to exit
'''
def print_best_book():
    best_book=sorted(books,key=lambda x:x.rating*-1)[:10]#here if you want sorting at time acroding to multiple thing
     # then well take tuple in the tuple seperated by multple thing like (x.rating*-1,x.price)this
    # sorting tow thinsg first one is acording to rating then price but first priority was rating
    for book in  best_book:
        print(book)
def cheapest_best_book():
    best_book=sorted(books,key=lambda x:x.price)[:10]
    for book in  best_book:
        print(book)

next_book_genrator=(x for x in books)
print(next(next_book_genrator))
def get_next_book():
    print (next(next_book_genrator))
def menu():
    print("shaikh imaduddin")
    user_input=input(USER_CHOICE)
    while user_input!='q' :
        if user_input=='b':
            print_best_book()
        elif user_input=='c':
            cheapest_best_book()
        elif user_input=='n':
            get_next_book()
        else:
            print('please enter a vailid commond')
        user_input=input(USER_CHOICE)


menu()