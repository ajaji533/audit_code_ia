#include <stdio.h>
#include <string.h>

void copier_message(char *entree) {
    char destination[8];

    strcpy(destination, entree);

    printf("Message copié : %s\n", destination);
}

int main() {
    char texte[] = "Bonjour tout le monde";
    copier_message(texte);
    return 0;
}
