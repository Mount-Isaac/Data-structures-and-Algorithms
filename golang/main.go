package main

import "dsa/datastructures"

func main() {
	// instantiate an object of a singly linked list (sll)
	sll_obj := datastructures.LinkedList{}

	//  insert nodes from a slice of elements
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	for _, number := range nums {
		sll_obj.InsertSinglyLinkedList(number)
	}

	// print the inserted nodes
	sll_obj.PrintNodes(&sll_obj)
	sll_obj.ReverseSinglyLList(&sll_obj)
	sll_obj.PrintNodes(&sll_obj)
}
