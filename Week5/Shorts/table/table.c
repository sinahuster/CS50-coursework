#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    string phrase;
    struct node *node;
}
node;

node *table[26];

int hash(string phrase);
bool unload(node *list);

int main(void)
{
    // Add items
    for (int i = 0; i < 3; i++)
    {
        string phrase = get_string("Enter a new phrase: ");

        // Find phrase bucket
        int bucket = hash(phrase);
        printf("%s hashes to %i\n", phrase, bucket);
    }

}

// Return the correct bucket for a given phrase
int hash(string phrase)
{
    // Returns 0-25, depending on the first char of the phrase

    return toupper(phrase[0]) - 'A';
}
