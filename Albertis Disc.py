# make Albertis Disc

stat_disc = "ABCDEFGILMNOPQRSTVXZ1234"
move_disc = "gklnprtuz&xysomqihfdbace"

"""
Lost letters in Alberti's Disc:

H = FF
J = II
K = QQ
U = VV
W = XX
Y = ZZ

"""



#def encode(stat, move, text):

lst_stat = []
lst_text = []
new_lst = []

result = ""

def set_stat_code(stat):

    global s_disc

    for x in range(len(stat_disc)):
        if stat == stat_disc[x]:
            s_disc = stat_disc[x:] + stat_disc[:x]
            return s_disc

def show_set_text(text):
    
    for i, j in enumerate(text):
        lst_stat.append((i, j))
    for x in lst_stat:
        for a, b in enumerate(s_disc):
            if x[1] == b:
                lst_text.append((a, x[1]))
    

def set_move_code(move):
    global m_disc

    for y in range(len(move_disc)):
        if move == move_disc[y]:
            m_disc = move_disc[y:] + move_disc[:y]
            return m_disc


def encrypt_code():
    for i,j in enumerate(m_disc):
        for y, z in enumerate(lst_text):
            if i == z[0]:
                new_lst.append((y, j))

    print(new_lst[0])
                    

if __name__ == "__main__":

    # invoke inputs to set the code
    stat = input("Choose a letter from stat disc: ").capitalize()
    move = input("Choose a letter from move disc: ")
    text = input("Put a text you want cipher: ").upper()

    # invoke stat code
    print("The stat code is:\n",set_stat_code(stat))

    # invoke move code
    print("The move code is:\n",set_move_code(move))

    #show the text with code
    show_set_text(text)
    encrypt_code()