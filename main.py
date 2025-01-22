# Ms.LaRose, and Vienna github test code
import random
def hello_world(name):
    return f"Hello {name}!"

def num_generator():
    num = random.randint(1,100)
    return num


def main():
    print("Welcome to my program. Please enter your name:\n")
    name=input()
    print(hello_world(name))
    print(num_generator())
          
          
main()