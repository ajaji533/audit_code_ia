#include <stdio.h>

void lire_nom() {
    char buffer[10];

    printf("Entrez votre nom : ");
    gets(buffer);

    printf("Bonjour %s\n", buffer);
}

int main() {
    printf("=== Programme de test C ===\n");
    lire_nom();
    return 0;
}
