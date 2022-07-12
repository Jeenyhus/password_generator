import random

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# number = '123456789'
# symbol = ',._*!/&@'

# all = alphabet.lower() + number + alphabet.upper() + symbol
# length = 10
# password = ''.join(random.sample(all,length))

# print('The Password you have generated is :',password)

def generate_pword():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = '123456789'
    symbol = ',._*!/&@'
    pass_length = 10

    all = alphabet.lower() + number + alphabet.upper() + symbol
    password = ''.join(random.sample(all,pass_length))

    return password

if __name__ == '__main__':
    print(generate_pword())
