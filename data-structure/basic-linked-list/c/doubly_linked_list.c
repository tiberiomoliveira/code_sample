#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

struct node {
    uint8_t data;
    struct node* next;
    struct node* prev;
};

void add_node(struct node* head, uint8_t data) {
    struct node* new_node = NULL;

    new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->next = NULL;
    new_node->prev = NULL;

    while (head->next != NULL) {
        head = head->next;
    }

    head->next = new_node;
    new_node->prev = head;
}

void print_list(struct node* head) {
    while (head != NULL) {
        printf("%d<->", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

void search_data(struct node* head, uint8_t data) {
    uint8_t i = 0;

    while (head != NULL) {
        if (head->data == data) {
            printf("Found data %d at position %d\n", data, i);
            return;
        }
        i++;
        head = head->next;
    }

    printf("Can't find data %d\n", data);
}

void delete_data(struct node* head, uint8_t data) {
    while (head != NULL) {
        if (head->data == data) {
            break;
        }
        head = head->next;
    }

    if (head == NULL) {
        printf("Can't find data %d in the list\n", data);
    }

    head->prev->next = head->next;
    head->next->prev = head->prev;
    free(head);
    printf("Successfully delete data %d\n", data);
}

void delete_list(struct node** head) {
    struct node* tmp = NULL;

    while (*head != NULL) {
        tmp = *head;
        *head = (*head)->next;
        free(tmp);
    }

    printf("List deleted\n");
}

int main(void) {
    struct node* head = (struct node*)malloc(sizeof(struct node));

    head->data = 0;
    head->next = NULL;
    head->prev = NULL;

    add_node(head, 1);
    add_node(head, 2);
    add_node(head, 3);

    print_list(head);

    search_data(head, 2);
    search_data(head, 4);

    delete_data(head, 2);
    print_list(head);

    delete_list(&head);

    return 0;
}