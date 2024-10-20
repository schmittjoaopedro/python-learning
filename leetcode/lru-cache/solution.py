class LRUCache:

    def __init__(self, capacity: int):
        print(capacity)
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.index = {}

    def get(self, key: int) -> int:
        val = -1
        if key in self.index:
            item = self.index[key]
            self.put(key, item.val)
            val = item.val
        return val

    def put(self, key: int, value: int) -> None:
        if not self.head:
            item = Item(key, value)
            self.head = item
            self.tail = item
            self.index[key] = item
        else:
            if key not in self.index:
                item = Item(key, value)
                self.index[key] = item
                self.head.next = item
                item.prev = self.head
                self.head = item
                if len(self.index) > self.capacity:
                    self.tail.next.prev = None
                    del self.index[self.tail.key]
                    self.tail = self.tail.next
            else:
                item = self.index[key]
                item.val = value
                if item != self.head:
                    prevItem = item.prev
                    nextItem = item.next
                    if prevItem and nextItem:
                        prevItem.next = nextItem
                        nextItem.prev = prevItem
                        self.head.next = item
                        item.prev = self.head
                        item.next = None
                        self.head = item
                    else:
                        self.tail = nextItem
                        nextItem.prev = None
                        self.head.next = item
                        item.next = None
                        item.prev = self.head
                        self.head = item


class Item:
    key = None
    val = None
    prev = None
    next = None

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
