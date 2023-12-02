#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILENAME "input.txt"

const char *numbers[9] = {"one", "two",   "three", "four", "five",
                          "six", "seven", "eight", "nine"};

void find_cv(char *line, const size_t len, int *result) {
  size_t index[2] = {999, 0};
  char number[2] = {'a', 'a'};
  size_t pos;
  char *ptr;

  // left - real digits
  for (size_t i = 0; i < len; ++i) {
    if (isdigit(line[i])) {
      index[0] = i;
      number[0] = line[i];
      break;
    }
  }

  // right - real digits
  for (size_t i = len; i + 1 > 0; --i) {
    if (isdigit(line[i])) {
      index[1] = i;
      number[1] = line[i];
      break;
    }
  }
  // printf("%c (%zu), %c (%zu), \n", number[0], index[0], number[1], index[1]);

  // word digits
  for (size_t i = 0; i < 9; ++i) {

    size_t offset = 0;

    while ((ptr = strstr(line + offset, numbers[i])) != NULL) {
      pos = ptr - line;
      // printf("Found word '%s' at index: %zu\n", numbers[i], pos);

      // left
      if (pos <= index[0]) {
        index[0] = pos;
        number[0] = '0' + (i + 1);
        // printf("Improvement left: %c (%zu)\n", number[0], index[0]);
      }

      // right
      if (pos >= index[1]) {
        index[1] = pos;
        number[1] = '0' + (i + 1);
        // printf("Improvement right: %c (%zu)\n", number[1], index[1]);
      }

      offset = pos + 1;
    }
  }

  // calibration value
  int value = atoi(number);
  printf("-> %i\n\n", value);
  (*result) += value;
}

int main() {
  FILE *fp;
  char *line = NULL;
  size_t len = 0;
  ssize_t read = 0;
  size_t cnt = 0;
  int result = 0;

  fp = fopen(INPUT_FILENAME, "r");
  if (!fp) {
    exit(EXIT_FAILURE);
  }

  while ((read = getline(&line, &len, fp)) != -1) {
    printf("(%zu) %s", read, line);
    find_cv(line, read - 1, &result);
    cnt++;
  }

  printf("Number of lines parsed: %zu\n", cnt);
  printf("Final calibration value: %i\n", result);

  fclose(fp);
  if (line) {
    free(line);
  }
  exit(EXIT_SUCCESS);
}
