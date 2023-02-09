import random


def random_walk(steps):
    position = 0
    walk = [position]
    for _ in range(steps):
        coin = random.randint(0, 1)
        if coin == 0:
            position -= 1
        else:
            position += 1
        walk.append(position)
    return walk


def main():
    walk = random_walk(steps=20)
    print(walk)


if __name__ == '__main__':
    main()
