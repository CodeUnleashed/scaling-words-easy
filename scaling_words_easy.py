scale = int(input())

word = [
        'U   U SSSSS AAAAA',
        'U   U S     A   A',
        'U   U SSSSS AAAAA',
        'U   U     S A   A',
        'UUUUU SSSSS A   A'
]

for line in word:
        for index in range(scale):
                for letter in line:
                        print(letter * scale, end="")

                print('')