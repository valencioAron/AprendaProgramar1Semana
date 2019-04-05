/*
 * C�digo base para a atividade de programa�ao em Portugol - Conquer X
 */
programa {
    // incluindo a biblioteca Util para ajudar a sortear numeros aleatorios
    inclua biblioteca Util
    
    funcao imprimir_resultado_jogador(inteiro valor1, inteiro valor2, inteiro total, cadeia nome) {
        escreva("\nOs dados do jogador " + nome +  " foram: \t" + valor1 + "\t" + valor2)
        escreva("\nTotal do jogo: " + total)
    }
    
    funcao jogar_dados_imprimir(inteiro &valor1, inteiro &valor2, inteiro &total, cadeia nome) {
        /*
        Joga os dados duas vezes e faz o total
        */
        // sorteia os valores
	    valor1 = Util.sorteia(1,6)
	    valor2 = Util.sorteia(1,6)
	    total = valor1 + valor2
	    
	    // imprime a funcao
	    imprimir_resultado_jogador(valor1, valor2, total, nome)
    }
    
    
	funcao inicio() {
	    inteiro valor_sorteado1, valor_sorteado2, total1, total2
	    cadeia dummy
	    logico jogar
	    jogar = verdadeiro
	    
	    // inicializa as vari�veis
	    valor_sorteado1 = 0
	    valor_sorteado2 = 0
	    total1 = 0
	    total2 = 0
	    
	    enquanto (jogar) {
	        // come�ando o jogo
    		escreva("\nDigite seu nome ou escreva sair. Aperte enter para come�ar! ")
    		leia(dummy)
    		
    		// verifica se � para sair do jogo
    		se (dummy=="sair") {
    		    retorne
    		}
    	    
    	    // jogar o dado para o jogador
    	    jogar_dados_imprimir(valor_sorteado1, valor_sorteado2, total1, "JOGADOR")
    	    
    	    // jogar o dado para a m�quina
    	    jogar_dados_imprimir(valor_sorteado1, valor_sorteado2, total2, "MAQUINA")
    	    
    	    
    	    // imprime o resultado final
    	    se (total1>=total2) {
    	        escreva("\nVoc� ganhou!! Parab�ns")
    	    } senao {
    	        escreva("\nA m�quina ganhou!! Que pena")
    	    }
	    } 
	    
	}
}