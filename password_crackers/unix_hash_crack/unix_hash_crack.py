import crypt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', help='path to the dictonary you wish to check against (one word per line)', required=True)
parser.add_argument('-p', help='path to the list of passwords (one per line) format: "username:passwordHash"', required=True)
args = parser.parse_args()

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open(args.d, 'r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if(cryptWord == cryptPass):
			print('[+] Found Password: ' + word + '\n')
			return
	print('[-] Password Not Found.\n')
	return


def main():
	passFile= open(args.p)
	for line in passFile.readlines():
		if(':' in line):
			line = line.strip('\n')
			user = line.split(':')[0]
			cryptPass = line.split(':')[1]
			print('[*] Cracking Password For: '+str(user))
			testPass(cryptPass)
if __name__ == '__main__':
	main()