'''#Write a python function oddTuples(aTup) that takes a some numbers
 in the tuple as input and
returns a tuple in which contains
odd index values in the input tuple'''
def odd_tuples(a_tup):
    '''aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    return a_tup[::2]
def main():
    '''This program is used to extract the odd elements from a tuple.'''
    data = input()
    data = data.split(" ")
    a_tup = ()
    for j in range(len(data)):
        a_tup += ((data[j]),)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
