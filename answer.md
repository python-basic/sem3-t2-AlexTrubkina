## ИСР

### 2.1. Разработать скрипт с функцией, которая строит таблицу истинности для логического выражения (по вариантам) для двух и трех аргументов (используются различные наборы значений аргументов). 


### 2.2. Разработать программу, которая выводит на экран с помощью ASCII-графики таблицу истинности на основе переданных ей на вход аргументов (логическое выражение, аргументы, результат вычисления выражения). Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 

```python
logical =[1, 1, 1]


delimiter  = "*"
space_symbol = " "
i = 1
# (A∨B)∧¬C
header = "* A *" + "* B *" + "* C *" + "* (A or B) and ¬C"+ " *"
table_width = len(header) # длина заголовка
print(header) # заголовок
print(delimiter * table_width) # разделение строк таблицы
inp_str = "* " + str(logical[0]) + " ** " + str(logical[1]) + " ** " + str(logical[2]) + " *"
res = "*       " + str(int((bool(logical[0]) or bool(logical[1])) and not bool(logical[2]))) + "         *"
print(inp_str + res)

while i <= 7 :
    print(delimiter * table_width)
    # меняю значения A B C
    if i == 7 or i == 3:
        del logical[0]
        logical.insert(2, 1)
    if i == 1:
        del logical[0]
        logical.insert(0, 0) 
    if i % 2 == 0 or i == 5 and i != 2:
        del logical[0]
        logical.insert(2, 0) 
    if i == 2:
        del logical[0]
        logical.insert(2, 0)
        logical.insert(1, 1)
    # вывожу значения A B C
    inp_str = "* " + str(logical[0]) + " ** " + str(logical[1]) + " ** " + str(logical[2]) + " *"
    # считаю результат
    res = "*       " + str(int((bool(logical[0]) or bool(logical[1])) and not bool(logical[2]))) + "         *"
    print(inp_str + res)
    i += 1
    
#(A→B)∧A)↔A∧B
print("\n")
i = 1
logical1 =[1, 1]
header = "* A *" + "* B *" + "* ((A -> B) and A) <-> A and B"+ " *"
table_width = len(header)
print(header) # заголовок таблицы
print(delimiter * table_width)
logical_q1 = (not bool(logical1[0]) or bool(logical1[1])) and bool(logical1[0]) 
# logical_q1 = (A→B)∧A
logical_q2 = bool(logical1[0]) and bool(logical1[1])
#logical_q2 = A∧B
logical_q3 = (not logical_q1 and not logical_q2) or (logical_q1 and logical_q2)
#logical_3 = (A→B)∧A)↔A∧B
inp_str = "* " + str(logical1[0]) + " ** " + str(logical1[1]) + " *"
res = "*           " + str(int(logical_q3)) + "                  *"
print(inp_str + res)
while i <= 3 :
    if i % 2 != 0:
        del logical1[1]
        logical1.insert(1, 0)
    else:
        del logical1[0]
        logical1.insert(1, 1)
    inp_str = "* " + str(logical1[0]) + " ** " + str(logical1[1]) + " *"
    logical_q1 = (not bool(logical1[0]) or bool(logical1[1])) and bool(logical1[0])
    logical_q2 = bool(logical1[0]) and bool(logical1[1])
    logical_q3 = (not logical_q1 and not logical_q2) or (logical_q1 and logical_q2)
    # результат 
    res = "*           " + str(int(logical_q3)) + "                  *"
    print(inp_str + res)
    i += 1

# B∧¬C∨¬(¬B→C∧B↔B)
print("\n")
i = 1
logical2 =[1, 1]
header = "* B *" + "* C *" + "* B and ¬C or ¬(¬B -> C and B <-> B)"+ " *"
table_width = len(header)
print(header)
print(delimiter * table_width)
logical_q1 = bool(logical2[0]) and not bool(logical2[1])
# logical_q1 = B∧¬C
logical_q2 = not((bool(logical2[0]) or bool(logical2[1])) and ((not bool(logical2[0]) and not bool(logical2[0])) or (bool(logical2[0]) and bool(logical2[0]))))
# logical_q2 = ¬(¬B→C∧B↔B)
logical_q3 = logical_q1 or logical_q2
# logical_q3 = B∧¬C∨¬(¬B→C∧B↔B)
inp_str = "* " + str(logical2[0]) + " ** " + str(logical2[1]) + " *"
res = "*           " + str(int(logical_q3)) + "                  *"
print(inp_str + res)
while i <= 3 :
    if i % 2 != 0:
        del logical2[1]
        logical2.insert(1, 0)
    else:
        del logical2[0]
        logical2.insert(1, 1)
    inp_str = "* " + str(logical2[0]) + " ** " + str(logical2[1]) + " *"
    logical_q1 = bool(logical2[0]) and not bool(logical2[1])
    logical_q2 = not((bool(logical2[0]) or bool(logical2[1])) and ((not bool(logical2[0]) and not bool(logical2[0])) or (bool(logical2[0]) and bool(logical2[0]))))
    logical_q3 = logical_q1 or logical_q2
    res = "*           " + str(int(logical_q3)) + "                  *"
    print(inp_str + res)
    i += 1

```

### 2.3. Разработать скрипт с функцией, которая для ряда Фибоначчи, где количество элементов, n = 22, возвращает подмножество значений или единственное значение (по вариантам). Для нахождения элемента требуется использовать слайсы. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории. 

```python
"""
Автор: Трубкина А. Ю. группа №1, подгруппа № 2

Дан список: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946

lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
Для данного списка, используя слайсы, обращение к элементам по индексу (не используя циклы или условные операторы) найдите:
3)Сумму элементов, расположенных на четных позициях, первой половины списка.
13)Сумму всех элементов списка с элементами, стоящими на нечетных местах в его первой половине.
"""
def main():
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    print(sm(lst))
    print(smh(lst))

#Сумма элементов, расположенных на четных позициях, первой половины списка.
def sm(lst = []):
    length = len(lst) // 2
    a = lst[:length]
    return sum(a[::2])

#Сумма всех элементов списка с элементами, стоящими на нечетных местах в его первой половине.
def smh(lst = []):
    length = len(lst) // 2
    b = sum(lst)
    a = lst[:length]
    c = sum(a[1::2])
    d = b + c
    return d
main()
```
### 2.4. Напишите программу с функцией, в которой будет реализовано решение физической задачи (по вариантам). Например: ящик, имеющий форму куба с ребром a см без одной грани, нужно покрасить со всех сторон снаружи. Найдите площадь поверхности, которую необходимо покрасить. Ответ дайте в квадратных сантиметрах. Решение задачи оформите в виде функции square(a), которая возвращает значение s. Например, при значении a = 30, square(30) вернет s = 4500. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.
