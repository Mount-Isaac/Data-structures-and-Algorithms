package datastructures

type Node struct {
	val  int
	next *Node
}

func (list Node) InsertSinglyLinkedList(data []int) Node {
	// insert head
	if list.next.val == nil {
		return list
	} else {
		list = Node{
			val:  data[0],
			next: &Node{},
		}
	}

	return list
}
