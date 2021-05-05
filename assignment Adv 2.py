# a simple program to print fibonacci series with terms upto the user entered no.
def febobobo(a):
    x=0
    y=1
    while x<a:
        z=x+y
        print(x)
        x,y=y,z
febobobo(int(input()))
