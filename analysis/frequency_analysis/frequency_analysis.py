import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='number of char to group by', default=1)
parser.add_argument('-f', help='file to be analyzed')
parser.add_argument('-s', help='string to be analyzed')
args = parser.parse_args()



def analysis_content():
    char_dictionary = {}
    if(args.s):
        content = args.s
    elif(args.f):
        content = args.f
        print('this option isn\'t completed yet please check back soon')
        exit()
    else:
        print('Please set content to be analyzed')
        exit()

    for i in content:
        char_dictionary[i] = content.count(i)


    return char_dictionary

def main():
    print(analysis_content())

if __name__ == '__main__':
    main()
