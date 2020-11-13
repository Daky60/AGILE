def reload():
    if PLAYER.action == 2:
        PLAYER.ammo(+1)
    elif COMPUTER.action == 2:
        COMPUTER.ammo(+1)
