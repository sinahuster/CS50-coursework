#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    string phrase;
    struct node *next;
}
node;

#define LIST_SIZE 2

bool unload(node *list);

int main(void)
{
    node *list = NULL;

    // Add items to the list
    for (int i = 0; i < LIST_SIZE; i++)
    {
        string phrase = get_string("Enter a new phrase: ");

        // Add phrase to new node in list
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        n->phrase = phrase;
        n->next = list;
        list = n;
    }

    // Free all memeory that has been used
    if (!unload(list))
    {
        printf("Error freeing the list.\n");
        return 1;
    }

}

bool unload(node *list)
{
    // Free all allocated nodes
    node *ptr = list;

    while (ptr != NULL)
    {
        ptr = list->next;
        free(list);
        list = ptr;
    }
    return true;
}
