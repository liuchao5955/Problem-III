'''
Created on 2012-8-12

@author: Administrator
'''
def getsum(n, m):
    string = `m` + '='
    max = (1 + n) * n / 2
    if max < m:
        print ''
    else:
        for x in range(1, m / 2 + 1):
            if x != m - x and m - x < n + 1 and x < n + 1:
                print string + `x` + '+' + `(m - x)`
            getResult(m - x, string + `x`, x, n)    

def getResult(m, stri, j, n):
    for x in range(j + 1, m / 2 + 1):
        if x != m - x and m - x < n + 1 and x < n + 1 :
            print stri + '+' + `x` + '+' + `(m - x)`
        getResult(m - x, stri + '+' + `x`, x, n)    

getsum(6, 10)
