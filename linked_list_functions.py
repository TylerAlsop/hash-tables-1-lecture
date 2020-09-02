##################### Linked List Functions #####################

    def linked_list_find(self, key):
        current_node = self.head

        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node.next

        return None

    def linked_list_delete(self, key):
        current_node = self.head

        if current_node.key == key:
            self.head = current_node.next
            return current_node

        previous_node = current_node
        current_node = current_node.next

        while current_node is not None:
            if current_node.key == key:
                previous_node.next = current_node.next
                return current_node
            else:
                previous_node = current_node
                current_node = current_node.next

        return None

    def linked_list_insert_at_head(self, key, value):
        node = HashTableEntry(key, value)
        node.next = self.head
        self.head = node

    def linked_list_insert_or_overwrite_value(self, key, value):
        node = self.linked_list_find(value)

        if node is None:
            self.linked_list_insert_at_head(HashTableEntry(key, value))
        else:
            node.value = value