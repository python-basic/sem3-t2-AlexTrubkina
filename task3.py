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
