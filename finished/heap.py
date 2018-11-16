class Heap(object):

    def __init__(self, data):
        self.items = data
        for index in range(len(self.items) // 2, -1, -1):
            self.percolate_down(index)

    def percolate_down(self,index):
        while index * 2 + 1 < len(self.items):
            left = index * 2 + 1
            if index * 2 + 2 < len(self.items):
                right = index * 2 + 2
                #compare left and right
                if self.items[left] < self.items[right]:
                    if self.items[left] < self.items[index]:
                        self.items[index], self.items[left] = self.items[left], self.items[index]
                        index = left
                    else:
                        break
                else:
                    if self.items[right] < self.items[index]:
                        self.items[index], self.items[right] = self.items[right], self.items[index]
                        index = right
                    else:
                        break
            else:
                #compare root and left
                if self.items[left] < self.items[index]:
                    self.items[index], self.items[left] = self.items[left], self.items[index]
                else:
                    break

    def is_empty(self):
        return 0 == len(self.items)

    def size(self):
        return len(self.items)

    def pop(self):
        if len(self.items) != 0:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
            ret = self.items.pop()
            self.percolate_down(0)
            return ret
        return None

    #get value but not pop up
    def get(self):
        if len(self.items) != 0:
            return self.items[0]
        else:
            return None

    def add(self, item):
        self.items.append(item)
        self.percolate_up(len(self.items) - 1)

    def percolate_up(self, index):
        while (index - 1) // 2 >= 0:
            root = (index - 1) // 2
            if self.items[index] < self.items[root]:
                self.items[index], self.items[root] = self.items[root], self.items[index]
                index = root
            else:
                break

def main():
    h = Heap([9,5,6,2,3,10,4,1,8,7,0])
    h.add(-1)
    print(h.get())
    h.add(11)
    print(h.get())
    print(h.size())
    print(h.get())
    for i in range(h.size()):
        
        print(h.pop())
    
if __name__ == "__main__":
    main()

