package datastructures

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

type LinkedList struct {
	head *Node
}

func (list *LinkedList) InsertSinglyLinkedList(data int) {
	// create a new node
	newNode := &Node{val: data}

	if list.head == nil {
		list.head = newNode
	} else {
		current := list.head
		for current.next != nil {
			current = current.next
		}
		current.next = newNode
	}
}

func (list *LinkedList) PrintNodes(*LinkedList) {
	current := list.head
	if current == nil {
		fmt.Println("Linked list is empty")
		return
	}

	fmt.Println("Linked list: ")
	for current != nil {
		if current.next == nil {
			//  don't print --> on tail node
			fmt.Printf("%d", current.val)
		} else {
			fmt.Printf("%d-->", current.val)
		}
		current = current.next
	}
	fmt.Println()
}

func (list *LinkedList) ReverseSinglyLList(*LinkedList) LinkedList {
	current := list.head
	var prev *Node

	if current == nil {
		return *list
	}

	for current != nil {
		nextNode := current.next
		current.next = prev
		prev = current
		current = nextNode
	}
	list.head = prev
	return *list
}
