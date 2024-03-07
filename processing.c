#include <stdlib.h>
#include <stdio.h>

FILE *file_ptr;
char file_content[100];

int main(int argc, char const *argv[])
{
	file_ptr = fopen("content.txt", "r");
	if (file_ptr == NULL) {
	  printf("Could not read the file\n");
	}
	else {
	  while (fgets(file_content, 5, file_ptr)){
		printf("%s", file_content);
	  }
	}
	printf("Done\n");
	pclose(file_ptr);

	return 0;
}