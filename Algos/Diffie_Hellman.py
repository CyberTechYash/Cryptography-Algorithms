from random import randint

if __name__ == '__main__':

    # Both the persons will be agreed upon the public keys G and P
    # A prime number P is taken
    P = int(input("Enter a prime number: "))

    # A primitive root for P, G is taken
    G = int(input("Enter the primitive root: " ))

    # Alice will choose the private key a
    a = int(input("The Private Key a for Alice is : "))

    # gets the generated key
    x = int(pow(G, a, P))

    # Bob will choose the private key b
    b = int(input("The Private Key b for Bob is : "))

    # gets the generated key
    y = int(pow(G, b, P))

    # Secret key for Alice
    ka = int(pow(y, a, P))

    # Secret key for Bob
    kb = int(pow(x, b, P))

    print("Secret key for the Alice is : ", ka)
    print("Secret Key for the Bob is : ", kb)