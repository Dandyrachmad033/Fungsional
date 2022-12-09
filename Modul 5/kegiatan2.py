import random

def move_r(ypos, xpos):
    if xpos == 9: raise Exception
    else:
        xpos += 1
        return xpos, ypos

def move_l(ypos, xpos):
    if xpos == 0: raise Exception
    else:
        xpos -= 1
        return xpos, ypos
    
def move_up(ypos, xpos):
    if ypos == 0: raise Exception
    else:
        ypos -= 1
        return xpos, ypos
    
def move_dw(ypos, xpos):
    if ypos == 9: raise Exception
    else:
        ypos += 1
        return xpos, ypos
    
def main():
    board = [["-" for x in range(10)] for y in range(10)]

    while True:
        player_xpos, player_ypos = random.randint(0,9), random.randint(0,9)
        goal_xpos, goal_ypos = random.randint(0,9), random.randint(0,9)
        if not player_xpos == goal_xpos and not player_ypos == goal_ypos: break

    board[player_ypos][player_xpos], board[goal_ypos][goal_xpos] = "A", "O"

    while True:
        for i in board: print(" ".join(i))
        if player_xpos == goal_xpos and player_ypos == goal_ypos:
            print("You win!")
            break
        print(" 1. Cek Posisi\n 2. Geser Kanan\n 3. Geser Kiri\n 4. Geser Atas\n 5. Geser Bawah\n 6. Keluar\n"+"="*26,"\nPilihan: ", end="")
        choice = int(input())
        if choice == 1:
            print("Posisi A: (%d,%d)" % (player_xpos, player_ypos))
        elif choice == 2:
            try:
                player_xpos, player_ypos = move_r(player_ypos, player_xpos)
                board[player_ypos][player_xpos],board[player_ypos][player_xpos-1] = "A","-"
            except Exception:
                print("Geser Kanan Gagal")
        elif choice == 3:
            try:
                player_xpos, player_ypos = move_l(player_ypos, player_xpos)
                board[player_ypos][player_xpos],board[player_ypos][player_xpos+1] = "A","-"
            except Exception:
                print("Geser Kiri Gagal")
        elif choice == 4:
            try:
                player_xpos, player_ypos = move_up(player_ypos, player_xpos)
                board[player_ypos][player_xpos],board[player_ypos+1][player_xpos] = "A","-"
            except Exception:
                print("Geser Atas Gagal")
        elif choice == 5:
            try:
                player_xpos, player_ypos = move_dw(player_ypos, player_xpos)
                board[player_ypos][player_xpos],board[player_ypos-1][player_xpos] = "A","-"
            except Exception:
                print("Geser Bawah Gagal")
        elif choice == 6: break
        
main()