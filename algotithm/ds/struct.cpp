/* Struct é uma estrutura de dados que permite 
   diferente tipos (semelhante a um objeto no js)*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>


int explicacao() {
	/* Estrtura aninhada */
	struct endereco {
		char rua[50];
		char cep[50];
	};	

	/* Estrutura básica */
	struct aluno {
		int numero_da_matricula;
		float nota[3];
		float media;
		struct endereco end; /* Struct aninhado */
	};


	/* Define um novo tipo de dado */ 
	typedef struct prova {
		float nota;
		float nota_minima;
	} Prova;
	
		struct aluno felipe;
	felipe.numero_da_matricula = 120;
	felipe.nota[0] = 8.5;
	felipe.nota[1] = 7.2;
	felipe.nota[2] = 5.4;
	felipe.media = (felipe.nota[0] + felipe.nota[1] + felipe.nota[2]) / 3.0;
	
	printf("Média do Felipe é: %2f\n", felipe.media);
	system("pause");
	return(0);

};

typedef struct {
	int dia;
	int mes;
	int ano;
} Data;

typedef struct {
	int codigo;
	char nome[200];
	Data dt_nas;
} Aluno;

int main() {

	
	Aluno a;
	
	setlocale(LC_ALL, "pt");
	a.codigo = 0;
	strcpy(a.nome, "NULL");
	a.dt_nas.dia = 0;
	a.dt_nas.mes = 0;
	a.dt_nas.ano = 0;
	
	printf("\n O codigo do aluno é: %d", a.codigo);
	printf("\n O nome do aluno é: %s", a.nome);
	printf("\n E sua data de nascimento é: %d/%d/%d", a.dt_nas.dia, a.dt_nas.mes, a.dt_nas.ano);
	printf("\n \n ");
	
	printf("DIgite o codigo do Aluno: ");
	scanf("%d%*c", &a.codigo);
	printf("\n DIgite o nome do Aluno: ");
	scanf("%s%*c", &a.nome);
	printf("\n DIgite o dia de nascimento do Aluno: ");
	scanf("%d%*c", &a.dt_nas.dia);
	printf("\n DIgite o mes de nascimento do Aluno: ");
	scanf("%s%*c", &a.dt_nas.mes);
	printf("\n DIgite o ano de nascimento do Aluno: ");
	scanf("%s%*c", &a.dt_nas.ano);
	printf("\n \n ");
	
	printf("\n O codigo do aluno é: %d", a.codigo);
	printf("\n O nome do aluno é: %s", a.nome);
	printf("\n E sua data de nascimento é: %d/%d/%d", a.dt_nas.dia, a.dt_nas.mes, a.dt_nas.ano);
	printf("\n \n ");	
	
	system("pause");
	return(0);
};
