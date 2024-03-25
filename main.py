from random import choice
from time import sleep

FILE_PATH = "skins.txt"


final = []
with open(f"{FILE_PATH}") as file:
    for line in file:
        skin, quant = line.split(",")
        for _ in range(int(quant)):
            final.append(skin)

if __name__ == "__main__":
    print(choice(final))
    sleep(5)
