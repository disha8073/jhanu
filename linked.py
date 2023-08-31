import collections
linked_lst=collections.deque()

linked_lst.append('20')
linked_lst.append('40')
print("\nelement in the linked_lst:\n",linked_lst)

linked_lst.insert(0,'10')
print("\nadding the element '10':\n",linked_lst)

linked_lst.insert(2,'20')
print("\nadding the element '20':\n",linked_lst)

linked_lst.remove('20')
print("\nremoving the element:\n",linked_lst)

linked_lst.remove('10')
print("\nremoving the element:\n",linked_lst)

