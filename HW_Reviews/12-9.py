# Задача 9. Да се напише програма, която да брои четните и нечетните числа в даден списък от цели числа, използвайки lambda.

l = [1,2,3,4,5]

evens = list(filter( lambda x:x%2==0, l ))
# for el in evens:
# 	print(el)

odds = list(filter( lambda x:x%2, l ))



print(f'Evens: {len(evens)}')
print(f'Odds: {len(odds)}')