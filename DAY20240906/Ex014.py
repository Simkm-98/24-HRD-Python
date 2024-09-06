def sum(start, end) :
    hap = 0
    for i in range(start, end+1) :
        hap = hap + i
    print('%d ~ %d의 정수의 합계 : %d' % (start, end, hap))
sum(1, 10)
sum(100, 200)
sum(200, 300)