
import json

# there should be at least 2 lines of comments
# another useless comment

def draw_text_rectangle(width, height):
    if type(width) != int or type(height) != int:
        raise ValueError
   
    def draw_entire_line():
        for _ in range(width):
            print("O", end='')
        print()

    def draw_middle_line():
        print("O", end='')
        for _ in range(width-2):
            print(" ", end='')
        if width >= 2:
            print("O", end='')
        print()

    if height >= 1:
        draw_entire_line()
    if height >= 3:
        for _ in range(height-2):
            draw_middle_line()
    if height >= 2:
        draw_entire_line()


if __name__ == '__main__':
    try:
        print(list(map(int, input("Enter a list of numbers: ").split())))
    except ValueError:
        print("Told you to enter a list of numbers!")
    else:
        print("Thank you!")
    
    try:
        width, height = map(int, input("Enter width and height in integer: ").split())
        draw_text_rectangle(width, height)
    except ValueError:
        print("Told you to enter them in integer!")
    else:
        print("Thank you!")

with open('output', 'w') as f:
    json.dumps([1, 'simple', 'list'])

