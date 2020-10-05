import numpy as np

def print_header():
    print("\tWelcome to 'Guess My Number'!")
    print("\tI'm thinking of a number between 1 and 100.")
    print("\tTry to guess it in as few attempts as possible.\n")


def print_footer(the_number, tries):
    print("You guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")
    print("\n\nPress the enter key to exit.")    
    
def main():
    # print the greeting banner
    print_header()
    
    # set the initial values
    the_number = np.random.randint(low=1, high=101, size=1)
    guess = int(input("Take a guess: "))
    tries = 1
    
    # the game loop
    while guess != the_number:
        if guess > the_number:
            print("Lower ...")
        else:
            print("Higher...")
            
        guess = int(input("Take a guess: "))
        tries += 1
        
    print_footer(the_number, tries)
    
    
if __name__ == "__main__":
    main()