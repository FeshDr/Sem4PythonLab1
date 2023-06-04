
def chek_len_decor(func):
    def inner(*args, **kwargs):
        if(len(args)+len(kwargs) > 10):
            print("Bad func")
        else:
            func(*args,**kwargs)       
    return inner

#@chek_len_decor
def test2(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs:
        print(i)

if __name__ == "__main__":


    type<"ClassName", ("Родители",{"отребуьы"})>

    test = chek_len_decor(test2)

    test(1,2,3,4,5,6,7,7,7,7,7,9)
    test(1,2,3)

    #test2(1,2,3)