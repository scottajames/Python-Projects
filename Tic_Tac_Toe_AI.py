X = "X"
O = "O"
Empty = " "
Tie = "TIE"
Num_squares = 9;

def instructions():
    """Display game instructions."""
    print(
        """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.
        You will make your move known by entering a number, 0-8. this number will correspond to the board position as illustrated:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        There are around 20,000 moves either of us can make and I have already calculated them all
        Prepare yourself, human. the ultimate battle is about to begin. \n
        """)

    def ask_yes_no(question):
        """Ask a yes or no question"""
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
            return response

    def pieces():
        """Determine if player or computer goes first."""
        go_first = ask_yes_no("Do you require the first move? (y/n)")
        if go_first == "y":
            print("\n then take the first move. You will need it.")
            human = X
            computer = O
        else: 
            print("\n Your bravery will be your undoing... I will go first.")
            computer = X
            humans = O
            return computer, human

        def new_board():
            """Create new game board."""
            board = []
            for square in range(Num_squares):
                board.append(Empty)
                return board

            def display_board(board):
                """Display game board on screen."""
                print("\n\t", board[0], "|", board[1], "|", board[2])
                print("\t", "---------")
                print("\t", board[3], "|", board[4], "|", board[5])
                print("\t", "---------")
                print("\t", board[6], "|", board[7], "|", board[8], "\n")

                def legal_moves(board):
                    """Create list of legal moves."""
                    moves= []
                    for square in range(Num_squares):
                        if board[square] == Empty:
                            moves.append(square)
                            return moves

                        def winner(board):
                            """Determind the game winner."""
                            Ways_to_win ((0, 1, 2),
                                         (3, 4, 5),
                                         (6, 7, 8),
                                         (0, 3, 6),
                                         (1, 4, 7),
                                         (2, 5, 8),
                                         (0, 4, 8),
                                         (2, 4, 6))

                            for row in Ways_to_win:
                                if board[row[0]] == board[row[1]] == board[row[2]] !=Empty:
                                    winner = board[row[0]]
                                    return winner

                                if Empty not in board:
                                    return Tie

                                