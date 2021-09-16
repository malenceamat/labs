import math


def φ(x):
    return x + 2*(math.log(x)-x+1.8)


def main():
    Δ = 2
    x = 3
    ε = 10**(-5)

    while not (abs(x-Δ) < ε):
        x = Δ
        Δ = φ(x)
    
    print('{:.6}'.format(x))


if __name__ == "__main__":
    main()
