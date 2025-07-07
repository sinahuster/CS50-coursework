#include <cs50.h>
#include <stdio.h>

void print_row(int n, int row);

int main(void)
{
    int n;
    while (n < 1 || n > 8)
    {
        n = get_int("Height: ");
    }
    for (int row = 1; row <= n; row++)
    {
        print_row(n, row);
    }
}
void print_row(int n, int row)
{

    int i;
    for (i = n - row; i > 0; i--)
    {
        printf(" ");
    }
    for (int j = 0; j < row; j++)
    {
        printf("#");
    }


    printf("\n");
}
