import ast

def prettyprint(node, no_of_space):
    for f in ast.iter_fields(node):
        print(" "*no_of_space, f)
    for n in ast.iter_child_nodes(node):
        prettyprint(n, no_of_space+2)
a = """
def func(one,two,three):
   if two<three:

       p = xyz(one,two,three)

       func(one,two,p-1)
       func(one,p+1,three)

"""

t = ast.parse("""
def fact(n):
    return n * fact(n-1)
""")
prettyprint(t, 0)
def build_paths_py(node, paths, path_so_far):
  for field in ast.iter_fields(node):
    if(field[0] != 'body'):
      path_so_far += field[0]
      path_so_far += type(field[1]).__name__

  for child_node in ast.iter_child_nodes(node):
    build_paths_py(child_node, paths, path_so_far)

  if path_so_far:
    print(path_so_far)

build_paths_py(t, [], "")
