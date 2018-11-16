def onlyVowels(s):
	'''
	recebe uma string e retorna a string sem as consontes
	'''
	retorno = ""
	for i in s:
		if i in ["a","e","i","o","u"]:
			retorno += i
	return retorno

def palindrome(s):
	return s == s[::-1]

risada = onlyVowels(input())



if palindrome(risada):
	print("S")
else:
	print("N")			