#ifndef _TRAVERSALH_
#define _TRAVERSALH_
#define SIZE 200 // define a size value of 200 to be used across the .c and .h file 

// ifndef checks if the given token has been defines earlier in the file

typedef struct
{
    char *file;
    int countValue;
} fileOrder; // create a struct with char array for the file name and integer value for the count of number of change made

int traversal(char *, char *); // call in traversal funtion in header

#endif
// endif closes the ifndef