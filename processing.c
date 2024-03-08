#include <stdlib.h>
#include <stdio.h>
#include <string.h>

FILE *file_ptr;
char file_content[5];

int* possible_moves(){};

void calculate(){};

int main(int argc, char const *argv[])
{
	int i,j, board[64];
	int count = 0;

	// get the board from the file
	file_ptr = fopen("temp.txt", "r");
	if (file_ptr == NULL) {
		printf("Error: Could not read the file\n");
		return 1; // Error
	}
	else {
		while (fgets(file_content, 5, file_ptr)){
			if (count == 1){
				i = atoi(file_content);
			}
			else if (count == 2) {
				j = atoi(file_content);
			}
			else {
				board[count-2] = atoi(file_content);
			}
			count++;
	  }
	}
	pclose(file_ptr);


	// we could make some tests to check, 
	// but we have predifined ways to run this file.
	if (strcmp(argv[1], "calculate") == 0){
		printf("Calculate\n");
	}
	else if (strcmp(argv[1], "poss_moves") == 0){
		printf("Possible moves\n");
	}

	return 0;
}