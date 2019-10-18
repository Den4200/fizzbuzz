# Fizzbuzz

class Fizzbuzz:

    def __init__(self, num):
        self.num = int(num)

    def fizzbuzz(self):
        nums = []
        for x in range(1, self.num + 1):
            
            if x % 3 != 0 and x % 5 != 0:
                nums.append(x)
            
            elif x % 3 == 0 and x % 5 == 0:
                nums.append('Fizzbuzz')

            elif x % 3 == 0:
                nums.append('Fizz')

            elif x % 5 == 0:
                nums.append('Buzz')

        return nums

def main():
    fizzbuzz = Fizzbuzz(input('Integer: ')).fizzbuzz()

    for num in fizzbuzz:
        print(num)

if __name__ == '__main__':
    main()
