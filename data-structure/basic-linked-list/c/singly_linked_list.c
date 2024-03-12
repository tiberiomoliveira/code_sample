#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct node {
    int8_t data;
    struct node* next;
};

void add_node(struct node* head, int8_t data) {
    struct node* new_node = NULL;

    new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = NULL;

    while (head->next != NULL) {
        head = head->next;
    }

    head->next = new_node;
}

void print_list(struct node* head) {
    while (head != NULL) {
        printf("%d->", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

void search_data(struct node* head, uint8_t search_data) {
    uint8_t i = 0;
    while (head != NULL) {
        if (head->data == search_data) {
            printf("Found data on position %d\n", i);
            return;
        }
        i++;
        head = head->next;
    }
    printf("Can't find data in the list\n");
}

void delete_data(struct node* head, uint8_t data) {
    struct node* prev_node = NULL;

    while (head != NULL) {
        if (head->data == data) {
            break;
        }
        prev_node = head;
        head = head->next;
    }

    if (head == NULL) {
        printf("Can't find the data %d to delete\n", data);
        return;
    }

    prev_node->next = head->next;
    free(head);
    printf("Successfully deleted the node with data %d\n", data);
}

void delete_list(struct node** head) {
    struct node* node = NULL;

    while (*head != NULL) {
        node = *head;
        *head = (*head)->next;
        free(node);
    }
    printf("Linked list cleared\n");
}

int main(void) {
    struct node *head = NULL;

    head = (struct node*)malloc(sizeof(struct node));
    head->data = 0;
    head->next = NULL;

    add_node(head, 1);
    add_node(head, 2);
    add_node(head, 3);

    print_list(head);

    search_data(head, 2);
    search_data(head, 4);

    delete_data(head, 2);
    print_list(head);
    delete_data(head, 4);

    delete_list(&head);

    return 0;
}