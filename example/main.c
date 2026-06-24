#include <stdio.h>

int main(void) {
    int arr[1000] = {0};

    int size = 0;

    while (1) {
        int userInput;
        scanf(" %d", &userInput);

        if (userInput == -1) {
            break;
        }

        if (userInput != 1 && userInput != 0) {
            continue;
        }

        arr[size++] = userInput;
    }

    int prev = arr[0];
    int cur;

    int available = (prev == 0) ? 1 : 0;
    int isAvailable = 0;

    for (int i = 1; i < size; i++) {
        cur = arr[i];

        if (cur == 1 && prev == 1) {
            printf("Rule has been break\n");
            return 0;
        }

        if (prev == 0 && cur == 1) {
            if (!isAvailable && available != 0) {
                available--;
            }
            prev = cur;
            continue;
        }

        if (prev == 1 && cur == 0) {
            prev = cur;
            isAvailable = 1;
            continue;
        }

        isAvailable = 0;
        prev = cur;
        available++;
    }

    if (!available) {
        printf("No urinals available\n");
    }
    else if (available == 1) {
        printf("There is %d urinal available\n", available);
    }
    else {
        printf("There are %d urinals available\n", available);
    }

    return 0;

}
