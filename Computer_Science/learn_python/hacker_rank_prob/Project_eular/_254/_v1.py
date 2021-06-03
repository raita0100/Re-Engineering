# Enter your code here. Read input from STDIN. Print output to STDOUT
factorials = {}
for i in range(10):
    if i == 0:
        factorials[i] = 1
    else:
        factorials[i] = i*factorials[i-1]

sf_look_up = {}

# subroutine for adding up digits
def get_sum(n):
    _ts = 0
    for i in str(n):
        _ts += int(i)
    return _ts

# subrouteen for sf(n)
def sf(n):
    if n in sf_look_up.keys():
        return sf_look_up[n]
    _s = 0
    for i in str(n):
        _s += factorials[int(i)]
    sf_look_up[n] = get_sum(_s)
    return (n, sf_look_up[n])

def sg(i):
    vr = 0
    if i in sf_look_up.values():
        vr = [idx for idx, k in sf_look_up.items() if k == i][0]
    else:
        ii = 1
        while True:
            if ii in sf_look_up.keys():
                res = (ii, sf_look_up[ii])
            else:
                res = sf(ii)
            if res[1] == i:
                vr = res[0]
                break
            ii+=1
    return get_sum(vr)


def main(n, m):
    _s = 0
    for i in range(1, n+1):
        _s += sg(i)
    print(_s%m)

if __name__ == '__main__':

    q = int(input())
    in_arr = []
    while q > 0:
        _l = [int(i) for i in input().split(" ")]
        in_arr.append(_l)
        q-=1
    for i in in_arr:
        main(i[0], i[1])
