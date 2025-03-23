package datastructures

type Node struct {
	val  int
	next *Node
}

func (list *Node) Insert(data int) Node {
	// insert a new node in a linkedlist
	head := Node{
		val:  data,
		next: &Node{},
	}
	return head
}
