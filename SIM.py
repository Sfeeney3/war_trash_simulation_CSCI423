import sys
import games.war as war
import games.trash as trash

def main():
    if len(sys.argv) != 3:
        print("Usage: ./SIM <war|trash> <file_path>")
        sys.exit(1)

    game_type = sys.argv[1]
    file_path = sys.argv[2]

    try:
        if game_type == "war":
            N, T, L = war.war(file_path)
        elif game_type == "trash":
            N, T, L = trash.trash(file_path)
        else:
            print(f"Invalid game type: {game_type}. Choose either 'war' or 'trash'.")
            sys.exit(1)

        print(f"OUTPUT {game_type} turns {N} transitions {T} last {L:.5f}")

    except IOError as e:
        # Printing a descriptive error message
        print(f"Error handling the file: {e}")
        sys.exit(2)  # Exiting with a non-zero error code

if __name__ == "__main__":
    main()
