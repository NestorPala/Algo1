// Pedir al usuario que ingrese números y mostrar su suma. Usar -1 como condición de corte.

#include <stdio.h>

int main() {
	float num = 0;
    int numero = 0, total = 0;
    
    while (numero != -1) {
		printf("Ingrese un numero mayor a cero o -1 para salir: ");
    	scanf("%f", &num);
		numero = (int)num; //por si el user es medio retrasaladix e ingresa números con coma

    	if (numero >= 0) {
    		total += numero;
			printf("Usted ha ingresado el numero: %d\n", numero);
		}
		else {
			if (numero != -1) {
				printf("Ingrese un numero 0 o mayor\n");
			}
		}
	}
	
	printf("La suma es %d", total);
	
    return 0;
}
