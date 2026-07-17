A=1
B=2
C=3
print('до обмена: A =', A, ', B =', B, ', C =', C)

A, B, C = C, A, B
print('после обмена: A =', A, ', B =', B, ', C =', C)



array = [10, 14, 25, 33, 47, 50, 61, 78, 82, 95, 100, 112, 120, 134, 141, 150]

for i in range(len(array)):
    if i % 5 == 0:
        print(array[i])




word1 = input()
word2 = input()

print(word1.replace("У", "").replace("у", ""))
print(word2.replace("У", "").replace("у", ""))