from typing import Generator


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed


class RandomGen:
    def __init__(self, seed: int = 0) -> None:
        self.Random_gen = lcg(pow(2, 32), 134775813, 1, seed)

    def randint(self, k: int) -> int:
        """ DO checks if the list has a negative number.
            :pre: k should be greater than or equal to 1
            :post: result should be between 1 to k inclusive
            :complexity: Best = Worst = O(1)
        """
        num_arr = []
        result = 0
        counter = [0] * 16

        # 5 random number in num_arr
        for _ in range(5):
            temp = bin(next(self.Random_gen) >> 16) # converts to binary and shifts left 16 bits
            num_arr.append(temp)

        # counting 1's in each bit of each number in num_arr
        for num in num_arr:
            diff = 16 - len(num)
            for i in range(len(num)-1, 1, -1):
                if num[i] == '1':
                    counter[diff + i] += 1

        # producing new number for result
        for i in range(15, -1, -1):
            if counter[i] >= 3:
                # adds to result 2 ^ n, where n = 15-index (where 15-index is the position)
                result += 2 ** (15-i)

        return (result % k) + 1


if __name__ == "__main__":
    Random_gen = lcg(pow(2, 32), 134775813, 1, 0)
