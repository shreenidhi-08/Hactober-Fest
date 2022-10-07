from html.entities import name2codepoint


def name_recur(n):
  if n>1:
    print("NIkky");
    name_recur(n-1);
  else:
    return
name_recur(5)
