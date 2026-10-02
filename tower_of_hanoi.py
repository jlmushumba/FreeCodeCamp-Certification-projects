def hanoi_solver(n):
    # TODO: 
    # if n is even:
    #   the top disk on peg on will do these moves:
    #   given that  named pegs => P:
    #   the moves are: P1 > P2 > p3 > ... and repeat
    # if n is odd:
    #   the moves will be P1 > P3 > P2 > ,,, and continue
    # nite that. ukora circle, for example, p1> p2>p3>p1...
    # 
    # and note that to evey move the first peg make
    # you make another legal move simultaneously. this is because you are left 
    # with one legal move when the disk 1 is moved.
    # 
    # the legal moves as given from freecode camp:
    # - You can move only top-most disks.
    # - You can move only one disk at a time.
    # - You cannot place larger disks on top of smaller ones.
    # #
    p1 = [num for num in range(n,0,-1)]
    p2 =[]
    p3 = []

    moves = 0
    string = ""

    #initial move
    string += f"{p1} {p2} {p3}\n"

    max_moves = (2 ** n) - 1 

    if n % 2 == 0:
       direction = [p1,p2,p3]
       

        
    elif n % 2 == 1:
        direction = [p1,p3, p2]

    current_index = 0
    while moves < max_moves:
        
        
        next_index = (current_index + 1) % 3

        current_peg = direction[current_index]
        next_peg = direction[next_index]


        disk = current_peg.pop()
        next_peg.append(disk)
        string += f"{p1} {p2} {p3}\n"
        moves += 1

        #next legal move

        if moves == max_moves:
            break
        peg_a_index = ((next_index + 2) % 3)
        peg_a = direction[peg_a_index]
        peg_b_inex = ((next_index - 2) % 3)
        peg_b = direction[peg_b_inex]
        # print("next_index:", next_index)
        # print("peg_a:", peg_a)
        # print("peg_b:", peg_b)
        if not peg_a:
            # move from peg_b to peg_a
            peg_a.append(peg_b.pop())
            moves += 1
            string += f"{p1} {p2} {p3}\n"
            

        elif not peg_b:
            # move from peg_a to peg_b
            peg_b.append(peg_a.pop())
            moves += 1
            string += f"{p1} {p2} {p3}\n"
            

        elif peg_a[-1] < peg_b[-1]:
            # move peg_a → peg_b
            peg_b.append(peg_a.pop())
            moves += 1
            string += f"{p1} {p2} {p3}\n"
            

        else:
            # move peg_b → peg_a
            peg_a.append(peg_b.pop())
            moves += 1
            string += f"{p1} {p2} {p3}\n"
            


        current_index = next_index
    return string.removesuffix("\n")

print(hanoi_solver(2))


        
