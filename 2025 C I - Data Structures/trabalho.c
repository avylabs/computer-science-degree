#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

//------------------------------------------------------
// Cliente Struct
typedef struct cliente{
    int numero;
    char prioridade;
    struct cliente *proximo;
} Cliente;

//------------------------------------------------------
// Prototypes
Cliente * criar_cliente();
void inserir(Cliente **head, char pri);
void imprimirFilaClientes(Cliente *head);
void atenderCliente(Cliente **head);

//------------------------------------------------------
//Main function
int main(){
    Cliente *head = NULL;
    int menu;
    char pri;

    
        printf(
            "SISTEMA DE SENHAS\n"
            "Insira o número correspondente ao menu desejado:\n\n"
            "1 - Inserir\n"
            "2 - Imprimir Lista de Clientes\n"
            "3 - Atender Cliente\n"
            "4 - Sair\n\n"
            );
        do{
        scanf("%d", &menu);
        while (getchar() != '\n'); // Clear leftover characters from input buffer (fonte: www.w3schools.com)
        switch (menu) {
            case 1:
                printf("Insira a prioridade do novo cliente(P/C):\n");
                scanf("%c", &pri);
                while (getchar() != '\n');
                inserir(&head, pri);
                break;
            case 2:
                printf("Lista de clientes completa:\n\n");
                imprimirFilaClientes(head);
                break;
            case 3:
                atenderCliente(&head);
                break;
            case 4:
                printf("Saindo da aplicação...\n");
                return 0;
                break;
            default:
                printf(
                "SISTEMA DE SENHAS\n"
                "Insira o número correspondente ao menu desejado:\n\n"
                "1 - Inserir\n"
                "2 - Imprimir Lista de Clientes\n"
                "3 - Atender Cliente\n"
                "4 - Sair\n\n"
                );
                break;

        }
    }while(1);
    return 0;
}

//------------------------------------------------------
//Functions

Cliente * criar_cliente(){
    Cliente *novo_cliente = (Cliente*)malloc(sizeof(Cliente));
    return novo_cliente;
}

void inserirSemPrioridade(Cliente **head, char pri){
    Cliente *temp_head = *head;
    Cliente *novo_cli = criar_cliente();
    novo_cli -> prioridade = pri;
    int num;

    // Checa para ver se a lista está vazia.
    // E então adiciona o cliente com o número correto
    if(*head == NULL){
        num = 1;
        novo_cli -> numero = num;
        *head = novo_cli;
        printf("cliente No: %d inserido\n", num);
    }
    else{
        while(temp_head->proximo != NULL){
            temp_head = temp_head->proximo;
        }
        if(temp_head -> numero < 301){num = temp_head -> numero + 1;}
        else{num = 1;}
        novo_cli -> numero = num;
        temp_head->proximo = novo_cli;
        printf("cliente No: %d inserido\n", num);
    }
}

void inserirComPrioridade(Cliente **head, char pri){
    Cliente *temp_head = *head;
    Cliente *novo_cli = criar_cliente();
    novo_cli -> prioridade = pri;
    int num;

    // Checa para ver se a lista está vazia.
    // E então adiciona o cliente com o número correto
    if(*head == NULL){
        num = 301;
        novo_cli -> numero = num;
        *head = novo_cli;
        printf("cliente No: %d inserido\n", num);
    }
    else{
        while(temp_head->proximo != NULL){
            if(temp_head->proximo->prioridade == 'C') break;
            temp_head = temp_head->proximo;
        }
        if(temp_head->numero < 301){
            num = 301;
            novo_cli -> numero = num;
            novo_cli -> proximo = *head;
            *head = novo_cli;
            printf("cliente No: %d inserido\n", num);
            return;
        }else{num = temp_head -> numero + 1;}
        novo_cli -> numero = num;
        novo_cli -> proximo = temp_head -> proximo;
        temp_head->proximo = novo_cli;
        printf("cliente No: %d inserido\n", num);
    }
}

void inserir(Cliente **head, char pri){
    Cliente *temp_head = *head;
    if(pri == 'C'){
        inserirSemPrioridade(head, toupper(pri));
    }

    else if(pri == 'P'){
        inserirComPrioridade(head, toupper(pri));
    }

    else{
        printf("Prioridade Inválida\n");
        return;
    }
}

void imprimirFilaClientes(Cliente *head){
    Cliente *temp_head = head;
    while(temp_head != NULL){
        printf("%c %d\n", temp_head->prioridade, temp_head->numero);
        temp_head = temp_head->proximo;
    }

}

void atenderCliente(Cliente **head){
    Cliente *temp = *head;

    if(temp != NULL){
        printf("Atendendo cliente No: %d\n", temp->numero);
        temp = temp->proximo;
        free(*head);
        *head = temp;
    }
    else{
        printf("Não há clientes para atender.\n");
    }
}