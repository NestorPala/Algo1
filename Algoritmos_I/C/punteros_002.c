
/*
Ejercicio 2 (tarea):
Enunciado: Crear un procedimiento que sume números ingresados por el usuario (los almacenará utilizando un puntero) y luego haga un print del resultado en el main.
(La resolución súbanla en un mensaje propio (no en el hilo de este mensaje))
*/


# include <stdio.h>
# include <stdbool.h> //true, false
# include <ctype.h> //tolower(str), toupper(str)


void sumar_numeros(float *acumulador) {
    float numero = 0;
    char opcion = ' ';
    bool seguir_ingresando = true;

    while (seguir_ingresando == true) {
        printf("Ingrese un numero:  ");
        scanf("%f", &numero);

        *acumulador += numero;

        //UTF-8: 168 = '¿'
        printf("%cDesea seguir ingresando numeros? (s/n)", 168);
        scanf(" %c", &opcion);

        if (tolower(opcion) == 'n') {
            seguir_ingresando = false;
        }
    }

}


int main() {
    float acumulador = 0;
    sumar_numeros(&acumulador);
    printf("La suma de todos los numeros ingresados es: %.2f", acumulador);

    return 0;
}
