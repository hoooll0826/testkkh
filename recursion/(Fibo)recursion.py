#재귀 연습, 팩토리얼
#def factorial(n)
#    if n==0:
#        return 1
#    else:
#            return n*factorial(n-1)
#print(factorial(7))

#과제 피보나치를 recursion 으로 구현하기
def fibo(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    elif i>1:
        return fibo(i-1)+fibo(i-2)
k=1
while k<10:
    print(fibo(k))
    k=k+1


#하노이의 탑 해결을 위한 최소횟수를 n에 대해 계산해주는 함수 구현 (recursion)
