 /*
 * C�digo base para a atividade de programa�ao em Portugol - Conquer X
 */
 
programa {
    // incluindo a biblioteca Util para ajudar a sortear numeros aleatorios
    inclua biblioteca Util
    
	funcao inicio() {
	    inteiro valor_sorteado
	    
	    // sorteie 3 vezes o n�mero
	    para (inteiro i = 0; i < 4; i++)  {
	        valor_sorteado = Util.sorteia(0, 10)
		    escreva("Valor sorteado:" + valor_sorteado + "\n")    
	    }
	    
	}
}
