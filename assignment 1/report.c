#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "report.h"

int comparator(const void *ptr1, const void *ptr2) //
{
    fileOrder *fo1 = (fileOrder *)ptr1;
    fileOrder *fo2 = (fileOrder *)ptr2;
    return (fo2->countValue - fo1->countValue); //
}

int report(fileOrder fo[], char path[], char word[], int nbFiles)
{
    FILE *report; // create a file for the report

    char pathReport[200]; // create a char array for the user input path concatenated with each text file or directory name
    pathReport[strlen(pathReport) - 1] = '\0';

    strcpy(pathReport, path);                   // copy the path to the pathReport
    strcat(pathReport, "\\report.txt");         // concatenate the report text file
    printf("the report name %s\n", pathReport); // to see if it works
    report = fopen(pathReport, "w");            // open and write in report file

    if (report) // if report is succesfully opened
    {

        // prints in file
        fprintf(report, "Target string: %s\nSearch begins in current folder: %s\n** Search Report **\nUpdates\t\t  File Name\n", word, path);

        // searches and finds empty space in array of fileOrder and sets a null value
        for (int i = nbFiles; i < SIZE; i++)
        {
            fo[i].file = NULL;
            fo[i].countValue = 0;
        }

        qsort(fo, SIZE, sizeof(fileOrder), comparator); // sorts array bigger to smaller count

        for (int i = 0; i < SIZE; i++) // goes through the entire fileOrder array and prints the file name and count value
        {
            if (fo[i].file != NULL) // skips if it has a null value
            {
                fprintf(report, "%d", fo[i].countValue);
                fprintf(report, "      \t\t");
                fprintf(report, "%s", fo[i].file);
                fprintf(report, "\n");
            }
        }
    }
    else
    {
        printf("Error! Failed to generate report Please try again."); // error message if report is not generated
        return 1;
    }

    fclose(report); // close the report.txt file

    return 0;
}