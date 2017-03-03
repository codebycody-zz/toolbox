import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='number of char to shift.', type=int, required=True)
parser.add_argument('-s', help='string to be ciphered', required=True)
args = parser.parse_args()
#use a string like this, instead of ord()
strs = 'abcdefghijklmnopqrstuvwxyz'

def shifttext(shift):
    inp  = args.s
    data = []
    #iterate over the text not some list
    for i in inp:
        # if the char is not a space ""
        if i.strip() and i in strs:
            data.append(strs[(strs.index(i) + shift) % 26])
        else:
            #if space the simply append it to data
            data.append(i)
    output = ''.join(data)
    return output

def main():
    print(shifttext(args.n))

if __name__ == '__main__':
    main()

