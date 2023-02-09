import random


def random_walk_2d(steps):
    position = [0, 0]
    walk = [position.copy()]
    for _ in range(steps):
        direction = random.randint(0, 3)
        if direction == 0:
            position[0] -= 1
        elif direction == 1:
            position[0] += 1
        elif direction == 2:
            position[1] -= 1
        else:
            position[1] += 1
        walk.append(position.copy())
    return walk


def main():
    walk = random_walk_2d(steps=20)
    print(walk)


if __name__ == '__main__':
    main()
