#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "PASS.h"

int main() {

    struct data d1;
    int massPass = 12345;

    printf("Welcome to password manager!\nPlease login:");
    scanf("%d", &d1.password);

    if (d1.password != massPass) {
        printf("Invalid login");
    }

    printf("===============================\nWelcome Back Rythem !\n");
    printf("1.View saved pass\n2.New entry\n3.Exit\n");

    int option;
    switch (option) {
    case 1:
    break;

    case 2:
    break;

    case 3:
    break;

    default:
    printf("invalid opt");
        break;
    }



}




