import re
import pickle

def main():

    f_path = 'fseven_data'

    fp = open(f_path, 'rb')

    data = str(fp.read())
    data = data.split("\\x")
    _arr = []
    for i in data:
        if i != '':
            match = re.match('(^[\dAaBbCcDdEeFf]+).*', i)
            _arr.append(int(match.groups()[0], 16))
    with open('conv_com.dat','wb') as f:
        pickle.dump(_arr, f)
        f.close()

if __name__ == '__main__':

    main()
