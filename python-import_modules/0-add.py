#0. Import a simple function from a simple file

if __name__ == "__main__":
 import add_0

 a = 1
 b = 2

result = add_0.add(a,b)
print("a = {} and b = {} FAKE add() => {} - {}".format(a,b,a,b))