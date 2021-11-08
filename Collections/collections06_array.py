import array
import binascii

arr = array.array('i', range(5))
print(arr)

f = open("test_collection.txt", 'w+b')
arr.tofile(f)  # 준비 (스트림에 넣어놓은거)
f.flush()  # 파일 객체의 내용을 밀어넣기함 (스트림 -> file)

with open("test_collection.txt", 'rb') as f1:
    data = f1.read()
    # print(binascii.hexlify(data))

    f1.seek(0)  # 원래 위치로 커서 이동
    arr2 = array.array("i")
    arr2.fromfile(f1, len(arr))
    print(arr2)