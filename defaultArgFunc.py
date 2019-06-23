# B_R_R
# M_S_A_W


"""
This function above does not throw an error, 
albeit when calling it we have not passed in any parameters. 
It is because we passed defaul parameters 
when we had defined it in the first place.
""""""


def hell_func(greet="Hello", name='You'):
    greet_inp=input("What is your welcome word: \n")
    nname=input("What is your name: \n")
    return "{},  {} :)".format(greet_inp, nname)

print(hell_func())
