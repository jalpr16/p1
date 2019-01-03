
# some useless comment

if __name__ == '__main__':
    print("Hello World!")
    while(True):
        try:
            print(list(map(int, input("Enter a list of numbers: ").split())))
        except ValueError:
            print("Told you to enter a list of numbers!")
        else:
            print("Thank you!")
        finally:
            print("This sentence will be shown regardless!")




