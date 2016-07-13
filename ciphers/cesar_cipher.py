#use a string like this, instead of ord()
strs='abcdefghijklmnopqrstuvwxyz'
def shifttext(shift):
	inp=raw_input('Input text here: ')
	data=[]
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