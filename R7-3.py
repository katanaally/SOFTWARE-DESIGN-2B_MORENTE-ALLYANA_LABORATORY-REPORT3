def recursive_count(list_head):
   
    if list_head._next is None:
        return 1
    else:
        return 1 + recursive_count(list_head._next)