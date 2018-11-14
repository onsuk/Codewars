'''
Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.
And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature?
As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array and be ready for anything else which is not clearly specified ;)
'''

# def tribonacci(signature, n):
#     res = signature[:n]
#     for _ in range(n-3):
#         res.append(sum(res[-3:]))
#     return res


# def tribonacci(signature, n):
#     sig_len = len(signature)
#     while sig_len < n:
#         sig_len += 1
#         signature.append(sum(signature[-3:]))
#     return signature[:n]

# generator
# def gen_tribonacci(max_num, *sig):
#     a,b,c = sig[0],sig[1],sig[2]
#     for _ in range(max_num):
#         yield a+b+c
#         a,b,c = b,c,a+b+c

# def tribonacci(signature, n):
#     for x in gen_tribonacci(n-3, *signature):
#         signature.append(x)
#     return signature[:n]


# generator expression

def tribonacci(signature, n):
    gen_tri = (sum(signature[-3:]) for _ in range(n-3))
    for v in gen_tri:
        signature.append(v)
    return signature[:n]

signature = [1, 1, 1]
n = 10

print(tribonacci(signature, n))

