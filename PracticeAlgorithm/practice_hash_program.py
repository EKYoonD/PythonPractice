hash_table = list(0 for i in range(10))
print(hash_table)


def hash_func(key):
    hash_key = key % 8
    return hash_key


def hash_storage(key_data, value):
    key_data = hash(key_data)
    hash_key = hash_func(key_data)
    hash_table[hash_key] = value


def get_hash_value(key_data):
    key_data = hash(key_data)
    hash_key = hash_func(key_data)
    return hash_table[hash_key]


hash_storage("Dave", "010-6461-5356")
hash_storage("July", "010-2324-1236")
hash_storage("Katie", "010-8923-1232")
hash_storage("Cory", "010-1234-1233")

print(get_hash_value("Dave"))
print(get_hash_value("Cory"))