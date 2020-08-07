def get_indices_of_item_weights(weights, length, limit):
    d = {}

    for i in range(length):
        curr = weights[i]
        # check if current weight is in the cache/dict
        if curr in d:
            # if it is, set prev to the curr value 
            prev = d[curr]
            return (i, prev)
        # now hash key is the smaller weight
        d[limit - weights[i]] = i 

    return None
