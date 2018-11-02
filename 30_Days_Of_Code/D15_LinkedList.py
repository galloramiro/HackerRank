class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
# _______________________________________________

    def insert(self,head,data): 
        newNode = Node(data)                        # Establece un nuevo nodo 
        if not head:                                # Si head es igual a None devuelve el newNode
            return newNode
        current = head                              # Establece el current como head
        while current.next:                         # Mientas exista un next en current
            current = current.next                  #
        current.next = newNode
        return head

#________________________________________________

mylist= Solution()
T=int(input())                                      # Toma el primero input que será el largo de la lista de números
head=None                                           # Establece la cavbeza de la lista en None
for i in range(T):                          
    data=int(input())                               # Pide un número para cada espacio del largo de la lista
    head=mylist.insert(head,data)                   # Para cada elemento llama a la funcion y le pasa los dos valores, data y head
mylist.display(head); 	                            # Una vez que termina el bucle llama a la función display de Solution