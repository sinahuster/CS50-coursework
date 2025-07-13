#include <cs50.h>
#include <stdio.h>
#include <string.h>

int word_score(string word);

int main(void)
{
    string word1 = get_string("Player 1 : ");
    string word2 = get_string("Player 2 : ");

    int score1 = word_score(word1);
    int score2 = word_score(word2);

    if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else if (score2 < score1)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int word_score(string word)
{
    int points;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        toupper(word[1]);
        if (word[1] == ('A' || 'E'|| 'I' || 'L' || 'N' || 'O' || 'R' || 'S' || 'T' || 'U'))
        {
            points++;
        }
        else if (word[1] == ('D' || 'G'))
        {
            point += 2
        }
        else if (word[1] == ('B' || 'C'|| 'I' || 'L' || 'N' || 'O' || 'R' || 'S' || 'T' || 'U'))
    }
}
