# |------------------------------------<< Linked List code using Python >>----------------------------------------|

#creating a Node
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#Class Linked-List
class Linkedlist:
    def __init__(self):
        self.head=None

    #---<< Insertion Operations>>----|

    def insert_at_beginning(self,data):
        self.head=Node(data,self.head)

    def insert_at_index(self,data,index):
        node=Node(data,None)
        if index <=0 or index > self.length_of_ll()+1:
            raise Exception("index out of range")    
        elif not self.head:
            if index==1:
                self.head=node
                return
            else:
                raise Exception("Empty LinkedList")
        elif index == self.length_of_ll():
            return self.insert_at_end(data)
        
        elif index == 1:
            return self.insert_at_beginning(data)
        itr=self.head
        count=1
        while itr and count!=index-1:            
            count+=1
            itr=itr.next
        node.next=itr.next
        itr.next=node

    def insert_at_end(self,data):
        node=Node(data,None)
        if not self.head:
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node

#---<< Length of the Linked-List >>---|
    def length_of_ll(self):
        if not self.head:
            return 0
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    
    #---<< Deletion Operations >>---|
    def remove_first_element(self):
        if not self.head:
            print("linkedlist is empty")
            return
        self.head=self.head.next

    def remove_at_index(self,index):
        if index <=0 or index > self.length_of_ll()+1:
            raise Exception("invalid index!")
        elif index==1:
            return self.remove_first_element()
        elif index == self.length_of_ll():
            return self.remove_last_element()
        else:
            itr=self.head
            count=1
            while count!=index-1 and itr:
                count+=1
                itr=itr.next
            itr.next=itr.next.next

    def remove_last_element(self):
        if not self.head:
            print('empty linkedlist')
            return
        itr=self.head
        while itr.next.next!=None:
            itr=itr.next
        itr.next=None


    #---<< Reversing a Linked-List >>---|
    def reverse(self):
        if not self.head:
            raise Exception("Empty linked list")

        curn=self.head
        perv=None
        while curn != None:
            next=curn.next
            curn.next=perv
            perv=curn
            curn=next
        self.head=perv
        
        

  


    #---<< Printing of Linked-List>>---|
    def print_ll(self):
        if not self.head:
            print("empty linkedlist")
            return
        itr=self.head
        while itr:
            print(itr.data,end="==>")
            itr=itr.next
        print("none")



#---<< Creating Object for class >>---|
if __name__=='__main__':
    ll=Linkedlist()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(5)
    ll.insert_at_end(11)
    ll.insert_at_end(345)
    ll.insert_at_end(12)
    ll.insert_at_end(13)
    ll.insert_at_index(800,7)
    ll.insert_at_index(100,1)
    ll.insert_at_index(8700,11)
    ll.insert_at_index(143,1)
    ll.print_ll()
    ll.reverse()
    ll.print_ll()

    






    