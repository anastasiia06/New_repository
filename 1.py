print("1. Створити пустий кортеж.")
empty_tuple = ( ),
print (empty_tuple)

print("2. Створити кортеж із одного довільного елемента.")
one_element = 'B',
print (one_element)

print("3. Створити Кортеж_1 із 5 довільних елементів-чисел.")
tuple_1 = (1, 4, 7, 3, 9)
print(tuple_1)

print("4. Розпакувати його.")
a,b,c,d,e = tuple_1
print(a,b,c,d,e)

print("5. Розмножити вдвічі.")
print(tuple_1*2)  

print("6. Створити Кортеж_2 із 3 довільних елементів-рядків.")
tuple_2 = ("cat", "dog", "rabbit")
print(tuple_2)

print("7. Зробити запит на наявність 2х елементів у кортежі_2 (одне значення має бути у кортежі, інше – відсутнє).")
print(tuple_2.count("cat"),tuple_2.count("car"))
