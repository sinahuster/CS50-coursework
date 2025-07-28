#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    int votes;
} candidate;

int main(void)
{
    // Define the number of candidates
    const int num = 3;
    candidate candidate[num];

    // Populate the array with users input
    for (int i = 0; i < num; i++)
    {
        candidate[i].name = get_string("Name: ");
        candidate[i].votes = get_int("Votes: ");
    }

    int highest_vote = 0;
    for (int i = 0; i < num; i++)
    {
        if (candidate[i].votes > highest_vote)
        {
            highest_vote = candidate[i].votes;
        }
    }

    for (int i = 0; i < num; i++)
    {
        if (candidate[i].votes == highest_vote)
        {
            printf("%s\n", candidate[i].name);
        }
    }
}
