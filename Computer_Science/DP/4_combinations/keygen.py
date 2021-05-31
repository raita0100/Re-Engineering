from datetime import datetime
import os
import csv

class KeyGen:

    def __init__(self, keylength=9):

        # set the key_len if key_len known
        self.key_len = keylength

        # here we are storiing all common keys that can be typed
        self.look_up = [chr(i) for i in range(32,127) if chr(i)]

        # open a file for storing the values with name
        # _length_y-m-d_H:M_s
        self.f_name = str(self.key_len)+"_"+(datetime.now()).strftime("%y-%m-%d_%H:%M")+".csv"
        with open(self.f_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["len", "val"])
        f.close()

    def _Genarate(self):

        combies = [self.look_up[0]] * self.key_len
        # verify array initialised
        print(f"\n\nInitial array : \n{combies}\n\n")
        f = open(self.f_name, 'a')
        writer = csv.writer(f)

        writer.writerow([self.key_len, "".join(combies)])
        TL = len(self.look_up)
        # generating the combinations
        for n in range(pow(TL, self.key_len)):
            _c = ""
            k = n
            for i in range(self.key_len):
                _c += self.look_up[k % TL]
                k //= TL
            writer.writerow([self.key_len, _c])

        f.close()

        print(f"\n\tGenerated Keys : {TL}^{self.key_len} = {pow(TL, self.key_len)}\n\n")

from itertools import permutations, combinations, product
import pickle

class Simple_Keygen:

    def __init__(self, L: int):
        self.Look_Up = []
        self.Len = L
        self.f_start = str(self.Len)+"_"+(datetime.now()).strftime("%y-%m-%d_%H:%M")
        self.init_lookup()

    def init_lookup(self):
        for i in range(65, 91):
            self.Look_Up.append(chr(i))

        for i in range(97, 123):
            self.Look_Up.append(chr(i))

        for i in range(0, 10):
            self.Look_Up.append(str(i))

    def _Genarate_product(self):
        res = list(product(self.Look_Up, repeat=self.Len))
        with open(self.f_start+"_product.pkl", "wb") as f:
            pickle.dump(res, f)
        f.close()

    def _Genarate_cobinations(self):
        res = list(combinations(self.Look_Up, self.Len))
        with open(self.f_start+"_cobinations.pkl", "wb") as f:
            pickle.dump(res, f)
        f.close()

    def _Genarate_permutations(self):
        res = list(permutations(self.Look_Up, self.Len))
        with open(self.f_start+"_permutations.csv", "wb") as f:
            pickle.dump(res, f)
        f.close()

if __name__ == '__main__':

    # create a object and pass the length of key to generate
    #k = KeyGen(2)
    #k._Genarate()

    S = Simple_Keygen(12)
    S._Genarate_permutations()
