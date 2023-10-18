#!/usr/bin/env python3


import sys
import games.war as war
import games.trash as trash

def main():
    if len(sys.argv) != 3:
        print("Usage: ./SIM <war|trash> <file_path>")
        sys.exit(1)

    game_type = sys.argv[1]
    file_path = sys.argv[2]

    # Just store the file path; don't read the values yet
    r_file_path = file_path

    try:

        if game_type == "war":

            war_game = war.war(r_file_path)

            while war_game.game_over == False:

                war_game.war_turn()

        elif game_type == "trash":
            trash_game= trash.trash(r_file_path)
            

            trash_game.play_game()
            trash_game.print_simulation_results()
            #print(f"OUTPUT trash turns: {trash_game.num_turns} transitions: {trash_game.transitions} transitions!")
        else:
            print(f"Invalid game type: {game_type}. Choose either 'war' or 'trash'.")
            sys.exit(1)



    except IOError as e:
        # Printing a descriptive error message
        print(f"Error handling the file: {e}")
        sys.exit(2)  # Exiting with a non-zero error code

if __name__ == "__main__":
    main()
