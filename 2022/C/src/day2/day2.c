#include "day2.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
    Rock, paper, scissors
    ---------------------

    Opponent's choices:
    - A -> rock
    - B -> paper
    - C -> scissors

    My instructions:
    - [PART 1]: X -> rock, Y -> paper, Z -> scissors
    - [PART 2]: X -> lose, Y -> draw, Z -> win

    Scoring:
    - Lose 0 points, draw 3 points, win 6 points
    - Selection is 1-2-3 in the order of the name of the game
*/

typedef struct MatchupsContainer {
    char **matchups;
    size_t size;
} MatchupsContainer;

#pragma region Forward declarations

int day2_parse_input(MatchupsContainer *container, const char *input_path);
int day2_part1(const MatchupsContainer *container);
int day2_part2(const MatchupsContainer *container);

#pragma endregion

void day2(const char *input_root) {
    const char *day = "day2";
    char *input_path = (char *)malloc(strlen(input_root) + strlen(day) + 1);
    strcpy(input_path, input_root);
    strcat(input_path, day);

    MatchupsContainer container = { .matchups = NULL, .size = 0 };
    if (day2_parse_input(&container, input_path) != -1) {
        int result_p1 = day2_part1(&container);
        int result_p2 = day2_part2(&container);
        printf("Day2: (%d, %d)\n", result_p1, result_p2);
    } else {
        fprintf(stderr, "Failed to read input file for day 1!");
    }

    for (size_t i = 0; i < container.size; i++) {
        free(container.matchups[i]);
    }
    free(container.matchups);
    free(input_path);
}

int day2_parse_input(MatchupsContainer *container, const char *input_path) {
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read_len;

    fp = fopen(input_path, "r");
    if (fp == NULL) {
        return -1;
    }

    while ((read_len = getline(&line, &len, fp)) != -1) {
        line[strcspn(line, "\r\n")] = '\0';

        char **temp = (char **) malloc(sizeof(char *) * (container->size + 1));
        for (size_t i = 0; i < container->size; i++) {
            temp[i] = container->matchups[i];
        }
        temp[container->size] = (char *) malloc(sizeof(char) * (read_len + 1));
        strcpy(temp[container->size], line);
        free(container->matchups);
        container->matchups = temp;
        container->size++;
    }

    fclose(fp);
    return 0;
}

int calculate_score_part1(const char *matchup) {
    if (strcmp("A X", matchup) == 0) return 1 + 3;
    if (strcmp("A Y", matchup) == 0) return 2 + 6;
    if (strcmp("A Z", matchup) == 0) return 3 + 0;

    if (strcmp("B X", matchup) == 0) return 1 + 0;
    if (strcmp("B Y", matchup) == 0) return 2 + 3;
    if (strcmp("B Z", matchup) == 0) return 3 + 6;

    if (strcmp("C X", matchup) == 0) return 1 + 6;
    if (strcmp("C Y", matchup) == 0) return 2 + 0;
    if (strcmp("C Z", matchup) == 0) return 3 + 3;
}

int day2_part1(const MatchupsContainer *container) {
    size_t total_score = 0;

    for (size_t i = 0; i < container->size; i++) {
        total_score += calculate_score_part1(container->matchups[i]);
    }

    return total_score;
}

int calculate_score_part2(const char *matchup) {
    if (strcmp("A X", matchup) == 0) return 3 + 0;
    if (strcmp("A Y", matchup) == 0) return 1 + 3;
    if (strcmp("A Z", matchup) == 0) return 2 + 6;

    if (strcmp("B X", matchup) == 0) return 1 + 0;
    if (strcmp("B Y", matchup) == 0) return 2 + 3;
    if (strcmp("B Z", matchup) == 0) return 3 + 6;

    if (strcmp("C X", matchup) == 0) return 2 + 0;
    if (strcmp("C Y", matchup) == 0) return 3 + 3;
    if (strcmp("C Z", matchup) == 0) return 1 + 6;
}

int day2_part2(const MatchupsContainer *container) {
    size_t total_score = 0;

    for (size_t i = 0; i < container->size; i++) {
        total_score += calculate_score_part2(container->matchups[i]);
    }

    return total_score;
}