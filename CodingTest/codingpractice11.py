list1 = [i*3 for i in range(0,6)]
list2 = [j*4 for j in range(0,6)]

list1 += list2
print(list1.count(12))

list3 = [1,2,3,4,5,5,5,5]
remove_set = [2,3,4]

result = [i for i in list3 if i not in remove_set]
print(result)

dict1 = dict()

dict1['Apple'] = '사과'
dict1['Strawberry'] = '딸기'
dict1['Orange'] = '오렌지'

if 'Apple' in dict1 :
    print('사과가 있습니다')

scores = [90, 85, 77, 65, 97]
cheating_list = {2,4}

for score_index in range(len(scores)):
    if score_index in cheating_list:
        continue
    print(scores[score_index])
