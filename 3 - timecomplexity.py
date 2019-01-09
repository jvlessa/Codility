def solution(X, Y, D):
    initial_coord = X
    final_coord = Y
    frog_jump = D

    jump_counter = 0

    while initial_coord < final_coord:
        jump_counter += 1
        initial_coord += frog_jump     

    return jump_counter

solution(10, 85, 30)