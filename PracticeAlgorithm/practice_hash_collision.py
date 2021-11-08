hash_table = list(0 for i in range(10))
print(hash_table)


def hash_func(key):
    hash_key = key % 8
    return hash_key


def hash_storage(key_data, value):
    key_data = hash(key_data)
    hash_key = hash_func(key_data)
    if hash_table[hash_key] is not None:
        for index in range(len(hash_table[hash_key])):
            if hash_table[hash_key][index][0] == key_data:
                hash_table[hash_key][index][1] = value
                return
        hash_table[hash_key].append(hash_key)
    else :
        hash_table[hash_key] = value
    hash_table[hash_key] = value


def get_hash_value(key_data):
    key_data = hash(key_data)
    hash_key = hash_func(key_data)
    return hash_table[hash_key]
