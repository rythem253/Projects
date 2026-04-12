#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "test.h"

int main () {

    struct callMe s1;

    int num;
    char name1[20];

    printf("Whats ur name? ");
    scanf("%s", name1);
    printf("Whats ur age? ");
    scanf("%d", &num);

    s1.data = num;
    s1.name = malloc(strlen(name1)+1);
    strcpy(s1.name, name1);

    printf("%s ", s1.name);
    printf("%d", s1.data);

}

