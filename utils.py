def set_board(wolf, rabbits):
    field = []
    for i in range(5):
        row = []
        for i in range(5):
            row.append('  *  ')
        field.append(row)
    field[wolf.Xposition][wolf.Yposition] = '  В  '
        
    for rabbit in rabbits:

        field[rabbit.Xposition][rabbit.Yposition] = '  З  '
    for i in field:
        print(' '.join(i))
