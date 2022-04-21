employees = {'mike': 27000, 'john': 65000, 'rebecca': 60000, 'tom': 100000}

for k, v in employees.items():
    print("{0} : {1}".format(k, str(v)))


employees = [('mike', 27000), ('john', 65000), ('rebecca', 60000), ('tom', 100000)]

for k, v in employees:
    print("{0} : {1}".format(k, str(v)))

    