def largest_prime(k: int) -> int:
    assert 2 <= k <= 100000, "k input is invalid"

    primeList = [True] * (k + 1)

    finalPrime = 0

    p = 2
    while p * p <= k:
        if primeList[p]:
            for i in range(p ** 2, k + 1, p):
                primeList[i] = False
        p += 1

    # Since 0 and 1 are not prime
    primeList[0] = False
    primeList[1] = False

    for j in range(len(primeList) - 1):
        if primeList[j]:
            finalPrime = j

    return finalPrime
