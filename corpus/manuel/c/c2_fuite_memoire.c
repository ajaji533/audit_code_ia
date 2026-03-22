#include <stdio.h>
#include <stdlib.h>

int main() {
    int *tableau = malloc(10 * sizeof(int));

    if (tableau == NULL) {
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        tableau[i] = i * 2;
    }

    printf("Première valeur : %d\n", tableau[0]);

    return 0;
}
