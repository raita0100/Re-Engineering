import argparse

# initialising the arguement
ap = argparse.ArgumentParser()

ap.add_argument('-b', '--base', type = int, required = True, help = "Base of number")
ap.add_argument('-n', '--num', type = int, required = True, help = "Number to conv")

args = vars(ap.parse_args())

_set = [chr(i) for i in range(32, 127) if chr(i)]

print(_set)

def gen(b, n):

    print(f"\n\t==> {n}_{b}")
    #to store the digits
    _d = []

    while n > 0:
        _d.append(n%b)
        n = n//b

    print(f"\n\n:Base converted = {_d}\n")

    #for i in range(len(_d)):
    #        print(f"{_d[i]}*({b}^{i})", end = " + ")
    #print("\n\n")

gen(args['base'], args['num'])
