#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ordernar_3_numeros.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 


def main():

	num1 = 0; num2=0; num3=0; num4 = 0;
	
	print("Digite 3 números reais e veja o resultado na ordem crescente:\n");
	
	num1 = int(input('Digite o 1º número: ')) 
	num2 = int(input('Digite o 2º número: ')) 
	num3 = int(input('Digite o 3º número: '))
	
	print('--------------------------')
	
	if num1 == num2 and num2 == num3:
		
		print("Não tem por que vc ordernar isso!!!!!!\n"); 
		
	####################################
	#		num1 menor de todos
	####################################
	elif num1 <= num2 and num1 <= num3: 
		
		print("O primeiro número é o menor de todos.\nTenho apenas que ordernar o 2º e 3º número.\n* A variavel num1 permanece com o mesmo valor.\n"); 
		
		if num2 > num3:
			num2 = num3
			num3 = num4
	
	####################################
	#		num2 menor de todos
	####################################
	elif num2 <= num3 and num2 <= num1:
		
		print("O segundo número é o menor de todos.\nTenho apenas que ordernar o 1º e 3º número, que agora é o 2º e 3º.\n* A  variavel num1 recebe o valor num2\n"); 
		
		num4 = num2 #temporario
		if num1 >= num3:
			print("Veja que o 1º número digitado é maior ou (igual) o 3º.\nEntão a ordem fica \"num1 = num2\" \"num2 = num3\" e \"num3 = num1\" \n");
			num2 = num3
			num3 = num1
		else:
			print("Veja que o 3º número digitado é maior ou (igual) o 1º.\nEntão a ordem fica \"num1 = num2\" \"num2 = num1\" e \"num3 = num3\" \n");
			num2 = num1
		
		num1 = num4
		
	####################################
	#		num3 menor de todos
	####################################
	elif num3 <= num1 and num3 <= num2:
		
		print("O terceiro número é o menor de todos,\nTenho apenas que ordernar o 1º e 2º número digitado, que agora é o 2º e 3º.\nA variavel num1 recebe o valor num3\n"); 
		
		num4 = num3 #temporario
		if num1 >= num2:
			print("Veja que o 1º número é maior ou (igual) o 2º,\nEntão a ordem fica \"num1 = num3\" \"num2 = num2\" e \"num3 = num1\" \n");
			num3 = num1
		else:
			print("Veja que o 1º número é menor ou (igual) o 2º,\nentão a ordem fica \"num1 = num3\" \"num2 = num1\" e \"num3 = num2\" \n");
			num3 = num2
			num2 = num1
		
		num1 = num4;
			
	print('Resultado: ',num1,' ',num2,' ',num3)

	return 0

if __name__ == '__main__':
	main()
