hash_table = list(0 for i in range(10))

print(hash_table)


# 해시 함수
def hash_func(key):
    return key % 10


# 주소 말해줄 key 데이터들
data1 = 'Andy'
data2 = 'Trump'
data3 = 'Dave'

# 키 값으로 활용하기 위해 위 데이터의 ASCII code를 가져오는 ord()
print(ord(data1[0]), ord(data2[0]), ord(data3[0])) # 데이터 키값 집합
print(ord(data1[0]), hash_func(ord(data1[0]))) # 키값, 함수 적용한 키값


# 해시 테이블에 값 저장
def storage_data(key_data, value):
    key = ord(key_data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


storage_data('Andy', '01011111111')
storage_data('Trump', '01022222222')
storage_data('Dave', '01033333333')


def get_data(key_data):
    key = ord(key_data[0])
    key_address = hash_func(key)
    return hash_table[key_address]


print(get_data('Andy'))
