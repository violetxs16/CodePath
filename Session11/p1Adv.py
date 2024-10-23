#Problem 1: Selective DNA Deletion
#As a biologist, you are working on editing a long strand of DNA represented 
# as a linked list of nucleotides. Each nucleotide in the sequence is represented 
# as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') 
# representing the nucleotide.

#Given the head of the linked list dna_strand and two integers m and n, write 
# a function edit_dna_sequence() that simulates the selective deletion of 
# nucleotides in a DNA sequence. You will: - Start at the beginning of the DNA strand.
#  - Retain the first m nucleotides from the current position. - Remove the next 
# n nucleotides from the sequence. - Repeat the process until the end of the DNA 
# strand is reached.

#Return the head of the modified DNA sequence after removing the mentioned nucleotides.

#Evaluate the time and space complexity of your solution. Define your variables 
# and provide a rationale for why you believe your solution has the stated time 
# and space complexity.

#UMPIRE stands for:

#Understand what the interviewer is asking for by using test cases and questions about the problem.
#Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.
#Plan the solution with appropriate visualizations and pseudocode.
#Implement the code to solve the algorithm.
#Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.
#Evaluate the performance of your algorithm and state any strong/weak or future potential work.

#Understanding: Input we are given a linked list, and we will keep the first m number of nodes and remove the next n number of nodes
#We keep going until we run out

#Match: Linked list

#Plan: Iterate through the linked list, implement counter for m and n, & reset counter after we reach certain number of nodes 
#Once the counter reaches two, we save the refernce of the node then we continue going through the linked list till we
#hit counter n then we connect the new node(start of m node)
#Possible edge cases: length is zero  = 
#given m and n that is bigger than the length of the linked list
#       -condition to check if 

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    counter_m = 0
    counter_n = 0
    current = dna_strand
    #m_cond = true
    #n_cond = false
    m_node = None

    while(current):
       # if counter_m == m:
        #    m_node = current
         #   counter_m = 0 #Reset counter
          #  i = 0
           # while(i < n):
        
        #we need to check that the node is existing        
        i = 0 

        while(i < m and current):
            i += 1
            current = current.next
        m_node = current

        j = 0
        while(j < n and current):
            j += 1
            current = current.next
        
        if current:
            m_node.next = current
        else:
            m_node = None #We reached the end

    return dna_strand



#pseudocode
#at 1 our position is 0 in the m counter so we increment
#we are now at m = 1
#at 2 our position in the m counter is 1 so we increment
#We are now at m = 2
#our m is now at capacity, so we need to switch to n
#at 3 our position in the n counter is 0 so we increment
#we are now at n = 1
#at 4 our position in the n counter is 1 so we increment



dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

#1 -> 2 -> 6 -> 7 -> 11 -> 12
#Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
#(1 -> 2) show in black nodes.
#Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
#Continue with the same procedure until reaching the tail of the Linked List.