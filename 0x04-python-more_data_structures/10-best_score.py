def best_score(a_dictionary):
    if a_dictionary:
        v = list(a_dictionary.values())
        k = list(a_dictionary.keys())
        return k[v.index(max(v))]
    # return max(a_dictionary, key=a_dictionary.get)
