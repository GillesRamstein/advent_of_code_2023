#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define INPUT_FILENAME "input.txt"

void find_cv(const char *line, const size_t len, int *result) {
  char number[2];
  for (size_t i = 0; i < len; ++i) {
    if (isdigit(line[i])) {
      number[0] = line[i];
      break;
    }
  }
  for (size_t i = len; i+1 > 0; --i) {
    if (isdigit(line[i])) {
      number[1] = line[i];
      break;
    }
  }
  int value = atoi(number);
  // printf("%s, %i\n", number, value);
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
    // printf("(%zu) %s", read, line);
    find_cv(line, read-1, &result);
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
