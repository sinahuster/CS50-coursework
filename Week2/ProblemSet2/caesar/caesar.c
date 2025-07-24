#include <cs50.h>
#include <inttypes.h>
#include <stdio.h>


int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    int k = strtoumax(argv[1]);

}
