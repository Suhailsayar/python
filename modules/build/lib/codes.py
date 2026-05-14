'''THE 'codes.py' module will print a list of any deminesions'''
def print_nested_list(mylist,level):
    '''The function 'printnestedlist'will print the nested lists and takes two argumnet'''
    for i in mylist:
        if isinstance(i, list): 
          print_nested_list(i,level+1) 
          for i in range(level):
              print("\t",end="")
        else:
            print(i)
