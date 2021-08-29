with open("sample.txt", 'a') as times_tables:
    for i in range(2, 13):
        for j in range(1, 13):
            answer = i * j
            print("{0:<2} times {1:<2} is {2:<3}".format(i, j, answer), file=times_tables)
        print("-" * 20, file=times_tables)
