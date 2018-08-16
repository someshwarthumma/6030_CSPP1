'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def face_value_only(hand):
    '''
    To get only the face values of a given card
    '''
    temp = []
    for i in hand:
        if i[0] == 'J':
            temp.append(11)
        elif i[0] == 'Q':
            temp.append(12)
        elif i[0] == 'K':
            temp.append(13)
        elif i[0] == 'A':
            temp.append(14)
        elif i[0] == 'T':
            temp.append(10)
        else:
            temp.append(int(i[0]))

    return temp

def duplicate_pair(hand):
    temp=[]
    sorted_list = sorted(face_value_only(hand))
    for i in sorted_list:
        if sorted_list.count(i)==0:
            temp.append(i)
    return (max(temp)/100)+1


def high_card(hand):
    '''
    To find the high card
    '''
    temp = []
    for i in hand:
        if i[0] == 'J':
            temp.append(float(1.1))
        elif i[0] == 'Q':
            temp.append(float(1.2))
        elif i[0] == 'K':
            temp.append(float(1.3))
        elif i[0] == 'A':
            temp.append(float(1.4))
        elif i[0] == 'T':
            temp.append(float(1.0))
        else:
            temp.append(int(i[0])/int(10))
    return max(set(temp))

def is_full_house(hand):
    '''
    To check weather given hand is full house or not
    '''
    sorted_list = sorted(face_value_only(hand))
    if sorted_list[0] == sorted_list[1] == sorted_list[2]:
        if sorted_list[3] == sorted_list[4]:
            return True
    if sorted_list[0] == sorted_list[1]:
        if sorted_list[2] == sorted_list[3] == sorted_list[4]:
            return True
    return False

def is_three_of_a_kind(hand):
    '''
    To check weather the given hand is three of a kind or not
    '''
    sorted_list = sorted(face_value_only(hand))
    for i in range(len(sorted_list)-2):
        if sorted_list[i] == sorted_list[i+1] == sorted_list[i+2]:
            return True
    return False

def is_two_pair(hand):
    '''
    To check for Two  pair in hand
    '''
    sorted_list = sorted(face_value_only(hand))
    if len(set(sorted_list)) == 3:
        return True
    return False

def is_one_pair(hand):
    '''
    To check for a pair n a hand
    '''
    sorted_list = sorted(face_value_only(hand))
    if len(set(sorted_list)) == 4:
        return True
    return False

def is_four_of_a_kind(hand):
    '''
    To check the given hand four of a kind
    '''
    sorted_list = sorted(face_value_only(hand))
    for i in range(len(sorted_list)-3):
        if sorted_list[i] == sorted_list[i+1] == sorted_list[i+2] == sorted_list[i+3]:
            return True
    return False

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''

    temp = sorted(face_value_only(hand))
    for i in range(len(temp)-1):
        if int(temp[i+1])-int(temp[i]) == 1:
            pass
        else:
            return False
    return True

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    for i  in range(len(hand)-1):
        card1 = hand[i]
        card2 = hand[i+1]
        if card1[1] != card2[1]:
            return False
    return True

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    if is_flush(hand) and is_straight(hand):
        return 9
    if is_four_of_a_kind(hand):
        return 8
    if is_full_house(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_three_of_a_kind(hand):
        return 4
    if is_two_pair(hand):
        return 3
    if is_one_pair(hand):
        return duplicate_pair(hand)
        #return 2
    return high_card(hand)

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    #return 1

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    #print(key=hand_rank)
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    #print(HANDS)
    print(' '.join(poker(HANDS)))
