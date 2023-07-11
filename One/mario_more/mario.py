while True:
    height = int(input("Height: "))
    width = height + 1
    if height >= 0 and height <= 23:
        break

for i in range(1, height + 1):
    num_hashes = i
    num_spaces = width - num_hashes
    print(" " * num_spaces, end="")
    print("#" * num_hashes, end=" ")
    print("#" * num_hashes, end="")
    print(" " * num_spaces)
