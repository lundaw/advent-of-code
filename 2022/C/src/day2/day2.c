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
        printf("Day1: (%d, %d)\n", result_p1, result_p2);
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

int day2_part1(const MatchupsContainer *container) {
    size_t total_score = 0;

    for (size_t i = 0; i < container->size; i++) {
        char *matchup = container->matchups[i];
        char opponent = matchup[0];
        char myself = matchup[2];

        if (opponent == 'A') {
            if (myself == 'X') {
                total_score += 1 + 3;
            }
            else if (myself == 'Y') {
                total_score += 2 + 6;
            }
            else {
                total_score += 3 + 0;
            }
        }
        else if (opponent == 'B') {
            if (myself == 'X') {
                total_score += 1 + 0;
            }
            else if (myself == 'Y') {
                total_score += 2 + 3;
            }
            else {
                total_score += 3 + 6;
            }
        }
        else {
            if (myself == 'X') {
                total_score += 1 + 6;
            }
            else if (myself == 'Y') {
                total_score += 2 + 0;
            }
            else {
                total_score += 3 + 3;
            }
        }
    }

    return total_score;
}

int day2_part2(const MatchupsContainer *container) {
    size_t total_score = 0;

    for (size_t i = 0; i < container->size; i++) {
        char *matchup = container->matchups[i];
        char opponent = matchup[0];
        char result = matchup[2];

        if (opponent == 'A') {
            if (result == 'X') {
                // Rock vs scissors, loss
                total_score += 3 + 0;
            }
            else if (result == 'Y') {
                // Rock vs rock, draw
                total_score += 1 + 3;
            }
            else {
                // Rock vs paper, win
                total_score += 2 + 6;
            }
        }
        else if (opponent == 'B') {
            if (result == 'X') {
                // Paper vs rock, loss
                total_score += 1 + 0;
            }
            else if (result == 'Y') {
                // Paper vs paper, draw
                total_score += 2 + 3;
            }
            else {
                // Paper vs scissors, win
                total_score += 3 + 6;
            }
        }
        else {
            if (result == 'X') {
                // Scissors vs paper
                total_score += 2 + 0;
            }
            else if (result == 'Y') {
                // Scissors vs scissors, draw
                total_score += 3 + 3;
            }
            else {
                // Scissors vs rock, win
                total_score += 1 + 6;
            }
        }
    }

    return total_score;
}