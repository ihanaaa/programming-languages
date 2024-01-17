#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <dirent.h>
#include "text.h"

int text(FILE *fp, FILE *ftemp, char word[])
{
    char fullstring[300]; // the string read in the fp text file
    int count = 0;        // to count how many of the words that have been changed in the text file

    size_t length = strlen(word); // length user input string is
    char lcword[length + 1];      // create a new char array to copy the user input string

    for (int c = 0; c < length; c++) // goes through the entire char array of the user input
    {
        lcword[c] = tolower((unsigned char)word[c]); // change the user input to lower case

        if ((c + 1) == length)
            lcword[c + 1] = '\0'; // to terminate it
    }

    while (fgets(fullstring, 300, fp) != NULL) // reads and gets line per line of the text file
    {
        size_t fslength = strlen(fullstring); // length of line of string read in file
        char lcfullstring[fslength + 1];      // create a new char array to copy string from the file in lowercase

        for (int b = 0; b < fslength; b++) // goes through the entire char array of the string from the file
        {

            lcfullstring[b] = tolower((unsigned char)fullstring[b]); // change the string to lowercase
            if ((b + 1) == fslength)
                lcfullstring[b + 1] = '\0'; // to terminate it
        }

        if (strstr(lcfullstring, lcword) != 0) // if the string from the file contains the user input
        {

            char *ptr1 = lcfullstring; // create a pointer that points to the start of the lowercase char array of the string in the file

            while ((ptr1 = strstr(ptr1, lcword)) != NULL) // pointer points to the start of user input within the lowercase string in the file
            {
                int position = ptr1 - lcfullstring; // the position of the pointer of the start of the user input within the lowercase string in the file

                for (int d = 0; d < fslength; d++) // goes through the entire char array of the string from the file

                { // if the index of the char array of the lowercase string from the file
                  // is the same as the position of the user input from start to end
                    if (d >= position && d < (position + length))
                    {
                        // change every character of the user input within the original string in the file in upper case
                        fullstring[d] = toupper((unsigned char)lcfullstring[d]);
                    }
                }
                ptr1 = ptr1 + (length); // moves the pointer after the last index of the user input within the lowercase string from the file
                count++;                // increment count
            }
        }

        printf("%s\n", fullstring); // print the string
        fputs(fullstring, ftemp);   // writes in the temp file the string
    }
    printf("The number of change is of %d\n\n", count); // prints the count value

    return count; // return count value
}