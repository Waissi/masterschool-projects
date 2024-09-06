def print_sticks(sticks):
    print(f"{sticks} in the pile.")


def bot_turn(sticks):
    take = sticks if sticks <= 3 else sticks % 4
    print(f"Player 1 takes: {take}")
    return take


def main():
    sticks = 21
    player = 1
    winner = 0
    print_sticks(sticks)
    while True:
        take = 0
        if player == 1:
            take = bot_turn(sticks)
        else:
            take = input(f"Player 2 takes: ")
            if take == '1' or take == '2' or take == '3':
                if sticks - int(take) < 0:
                    continue
                take = int(take)
            else:
                continue
        sticks -= take
        print_sticks(sticks)
        if sticks == 0:
            winner = player
            break
        player = 1 if player == 2 else 2
    print(f"Player {winner} won!")


if __name__ == "__main__":
    main()
