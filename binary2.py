def factorial(n):
    res = 1

    for i in range(1, n + 1):
        res *= i
    return res

def binomialCoeff(n, k):
    res = 1

    if (k > n - k):
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

def num(n):
    c = binomialCoeff(2 * n, n)

    return c // (n + 1)


def countBST(n):
    count = num(n)

    return count

def countBT(n):

    count = num(n)

    return count * factorial(n)

if __name__ == '__main__':
    n = 12

    count1 = countBST(n)
    count2 = countBT(n)

    print("Count of BST with", n, "nodes is", count1)
    print("Count of binary trees with", n,
          "nodes is", count2)


