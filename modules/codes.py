'''THE 'codes.py' module will print a list of any deminesions'''
def print_nested_list(mylist,level=0,indent=True):
    '''The function 'printnestedlist'will print the nested lists and takes two argumnet'''
    for i in mylist:
        if isinstance(i, list): 
          print_nested_list(i,level+1,indent) 
        else:
          if indent:
           for i in range(level):
              print("\t",end="")
          print(i)
nest =[1,2,3,[4,5]]
print_nested_list(nest,2,True)