// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];

    // Read each word in the file
    while(fscanf(source, "%s", buffer) != EOF)
    {
        node *new_word = malloc(sizeof(node));
        new_word->next = NULL;
        strcpy(new_word->word, buffer);

        // Obtain the hash value of the word
        int index = hash (new_word->word);

        // Add each word to the hash table
        if (table[index] == NULL)
        {
            // Assign new word the index in the hash table
            table[index] = new_word;
        }
        else
        {
            // Prepend the word to the list which is found at the index of the hash table
            new_word->next = table[index];
            table[index] = new_word;
        }

    }

    // Close the dictionary file
    fclose(source);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
