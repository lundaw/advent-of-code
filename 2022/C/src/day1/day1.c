#include "day1.h"

#include "../common/utils.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct ElfGroupContainer {
    int *groups;
    int size;
} ElfGroupContainer;

#pragma region Forward declarations

int day1_parse_input(ElfGroupContainer *container, const char *input_path);
int day1_part1(const ElfGroupContainer *container);
int day1_part2(const ElfGroupContainer *container);

#pragma endregion

void day1(const char *input_root) {
    const char *day = "day1";
    char *input_path = (char *)malloc(strlen(input_root) + strlen(day) + 1);
    strcpy(input_path, input_root);
    strcat(input_path, day);

    ElfGroupContainer container = {.groups = NULL, .size = 0};
    if (day1_parse_input(&container, input_path) != -1) {
        int result_p1 = day1_part1(&container);
        int result_p2 = day1_part2(&container);
        printf("Day1: (%d, %d)\n", result_p1, result_p2);
    } else {
        fprintf(stderr, "Failed to read input file for day 1!");
    }

    free(container.groups);
    free(input_path);
}

int day1_parse_input(ElfGroupContainer *container, const char *input_path) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read_len;

    fp = fopen(input_path, "r");
    if (fp == NULL) {
        return -1;
    }

    int current_group = 0;
    while ((read_len = getline(&line, &len, fp)) != -1) {
        line[strcspn(line, "\r\n")] = '\0';

        if (line[0] == '\0') {
            // Allocate a larger container and copy over the elements, then append the new group sum
            // and finally free the original one
            int *temp = container->groups;
            container->groups = (int *)malloc(sizeof(int) * (container->size + 1));
            for (int i = 0; i < container->size; i++) {
                container->groups[i] = temp[i];
            }
            container->groups[container->size] = current_group;
            container->size++;
            free(temp);
            current_group = 0;

            continue;
        }

        current_group += atoi(line);
    }

    sort_int_array(container->groups, container->size);

    fclose(fp);
    return 0;
}

int day1_part1(const ElfGroupContainer *container) { return container->groups[0]; }

int day1_part2(const ElfGroupContainer *container) {
    return container->groups[0] + container->groups[1] + container->groups[2];
}