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
