#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "traversal.h"
#include "report.h"

extern fileOrder fo[SIZE]; // use extern to use the function fileOrder with a defined size value of 200 that is both defined elsewhere
int main()
{

    char string[200]; // create a char string for the user input

    printf("Please enter a string you want to alter: "); // print message
    fgets(string, 200, stdin);                           // get string
    string[strlen(string) - 1] = '\0';                   // to remove the extra \n created at the end

    // receives number of files from the traversal function where the path is the current path directory and the word is the user input
    int nbFiles = traversal(".", string);
    report(fo, ".", string, nbFiles); // call in the report function with the filerOrder array, current path, the user input, and the number of files

    for (int i = 0; i < nbFiles; i++) // goes through the entire fileOrder array
    {
        free(fo[i].file); // deallocates the memory allocated by a call to malloc in the traversal function
    }

    system("pause"); // to avoid it from closing immediately
    return 0;
}