import types

def flat_generator(list_of_lists):
    generat = (list_of_lists[i][j] for i in range(0, len(list_of_lists)) for j in range(0, len(list_of_lists[i])))
    return generat