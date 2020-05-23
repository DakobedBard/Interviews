# def memoize(f):
#     memo = {}
#     def helper(x):
#         if x not in memo:
#             memo[x] = f(x)
#         return memo[x]
#     return helper
#
# @memoize
# def fibonnacci(n):
#     if n == 0 :
#         return 0
#     if n == 1:
#         return 1
#     return fibonnacci(n-1) + fibonnacci(n-2)
#
# print(fibonnacci(4))



def memofib(n, memo):
    if n in memo:
        return memo[n]
    else:
        return memofib(n-1, memo) + memofib(n-2, memo)

def fib(n):
    memo = {0:0, 1:1}
    return memofib(n, memo)

print("Memo fib "  + str(fib(5)))
