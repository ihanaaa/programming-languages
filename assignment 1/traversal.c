#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/stat.h>
#include <dirent.h>
#include "traversal.h"
#include "text.h"

int nbFiles = 0;    // initialize the integer for the number of total files to 0
fileOrder fo[SIZE]; // create an array of struct fileOrder created in traversal.h of size SIZE which is defined as 200 in traversal.h

int traversal(char path[], char word[])
{

    DIR *dir;              // create directory pointer
    struct dirent *dentry; // create pointer to the structure dirent
    FILE *fp;              // the file that is being read
    FILE *ftemp;           // the temporary file
    struct stat filepath;  // create a stat structure to know directory type

    char pathConcat[200]; // create a char array for the user input path concatenated with each text file or directory name
    pathConcat[strlen(pathConcat) - 1] = '\0';
    char pathTemp[200]; // create a char array of the temp file concatenated with the user input path
    pathTemp[strlen(pathTemp) - 1] = '\0';
    char reportConcat[200]; // create char array for report name of files
    reportConcat[strlen(reportConcat) - 1] = '\0';

    size_t length = strlen(word); // length user input string is
    char newword[length + 1];     // create a new char array to copy the user input string

    for (int a = 0; a < length; a++) // goes through the entire char array of the user input
    {
        newword[a] = toupper((unsigned char)word[a]); // change the user input to upper case

        if ((a + 1) == length)
            newword[a + 1] = '\0'; // to terminate it
    }
    // print the user input length, the original user input, the original user input in upper case
    printf("The length is %d.\n\nThe old word is %s and the new word is %s.\n\n", length, word, newword);

    dir = opendir(path); // opens the directory pointing to the path

    strcpy(pathConcat, path);       // copy user input path to char array of pathConcat
    strcat(pathConcat, "\\");       // concatenate '\' to the user input path
    strcpy(pathTemp, path);         // copy user input path to char array of pathTemp
    strcat(pathTemp, "\\temp.txt"); // concatenate '\temp.txt' to create or open a temp text file using the user input path

    if (dir == NULL) // to check if the directory worked
    {
        printf("Error! Failed to open directory. Please try again."); // print error message
        return 0;                                                     // ends the function early if error occurs
    }

    while (dentry = readdir(dir)) // loop for reading the directory dir to read every entry and store it in the structure dent
    {
        // if directory is pointing to the current directory (.) or parent directory (..)
        if (strcmp(dentry->d_name, ".") != 0 && strcmp(dentry->d_name, "..") != 0)
        {
            stat(dentry->d_name, &filepath); // file located in directory and address of stat structure

            if (dentry->d_name[0] == '.' || S_ISDIR(filepath.st_mode)) // if it is a directory
            {
                printf("Directory: %s\n", dentry->d_name); // prints the directory name
                strcat(pathConcat, dentry->d_name);        // concatenate the current path\ with the file name for the recursion
                traversal(pathConcat, word);               // call in the recursion for the directory
                strcpy(pathConcat, path);                  // copy back the path to the pathConcat
                strcat(pathConcat, "\\");                  // concatenate '\' to the pathConcat
            }
            // if it is the temp file or the report file, skip
            else if (strcmp(dentry->d_name, "temp.txt") == 0 || strcmp(dentry->d_name, "report.txt") == 0)
            {
                continue; // continue and go to the next file
            }
            else if (strstr(dentry->d_name, ".txt")) // if it is a text file
            {
                printf("Text File: %s\n", dentry->d_name); // prints the text file name

                ftemp = fopen(pathTemp, "w"); // later replace with user input

                strcat(pathConcat, dentry->d_name);          // concatenate the current path\ with the file name for the recursion
                printf("Path Concat is %s\n\n", pathConcat); // shows if the change was successful
                fp = fopen(pathConcat, "r");                 // open the text file

                strcpy(reportConcat, pathConcat); // copy the concatenated path to the report name
                reportConcat[0] = ' ';            // remove the . directory
                reportConcat[1] = ' ';            // remove the '\'

                fo[nbFiles].countValue = text(fp, ftemp, word);      // the count value from text function, store it in the struct and text function occurs
                fo[nbFiles].file = malloc(strlen(reportConcat) + 1); // copies space in fileOrder array from the name of the file
                strcpy(fo[nbFiles].file, reportConcat);              // copy the report name to the fileOrder array

                // prints message of the number of files, the file name and the count
                printf("the string for file at %d should be %s with a count of %d\n\n", nbFiles, fo[nbFiles].file, fo[nbFiles].countValue);
                nbFiles++; // increment the nb Files

                fclose(ftemp);      // need to close the temp file to be able to reopen and use it again as a temp
                fclose(fp);         // need to close the current file pointed by the directory to be able to remove it
                remove(pathConcat); // remove the original file

                rename(pathTemp, pathConcat);                  // rename the temp file as the original file with the modifications
                strcpy(pathConcat, path);                      // change the path that is concatenated into the original start of the path
                strcat(pathConcat, "\\");                      // concatenate '\' to the pathConcat
                printf("Path Original is %s\n\n", pathConcat); // shows if the change was successful
            }
        }
    }

    if (closedir(dir) == -1) // if directory closed succesfully
    {
        printf("Error! Failed to close directory. Please try again."); // prints error message if directory did not close succesfully
        return 1;
    }

    return nbFiles; // returns number of files for the function
}
