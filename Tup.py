# defining the function to add a tuple to the list

def add_tp_ls(ls, tp):

# Add a tuple to the list

ls.append(tp)

return ls 

# defining the function to add a list to a tuple

def add_ls_tp(tp, ls):

# Add a list to the tuple

return tp + tuple(ls) 

# Defining list and tuple with values

ls = [10,15, 20, 50]

tp = (40, 60, 70, 80) 

print(f"The list after adding tuple: {add_tp_ls(ls, tp)}")

print(f"The tuple after adding list: {add_ls_tp(tp, ls)}")
