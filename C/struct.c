#include <stdio.h>


typedef struct {
    int edad;
    char nombre[30]; //O también "char* nombre;"
    char genero[30]; 
} humano_t;


void cumpleanios(humano_t* persona) {
    // (*persona).edad += 1 se escribe de manera cómoda como:
    persona -> edad += 1;

    // Si el objeto de la izquierda no es un puntero, uso "." en vez de "->"
}


int main(){
    // Manera no recomendada de inicializar structs
	humano_t raul = {24, "Raul", "Masculino"};

	printf("Hola soy Raul y tengo %d a%cos\n", raul.edad, 164);

    // Pasamos la variable por referencia
    cumpleanios(&raul);

    printf("Ahora tengo %d a%cos\n", raul.edad, 164);

	return 0;
}
