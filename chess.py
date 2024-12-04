# determining which black pieces can be taken by a white piece in Chess


# Define valid chess pieces and their movement rules
VALID_CHESS_PIECES = {"pawn", "rook"}
CHESS_BOARD_COLUMNS = "abcdefgh"
CHESS_BOARD_ROWS = "12345678"


def is_valid_coordinate(coordinate):
    """Checks if the coordinate is valid (a-h and 1-8)."""
    return len(coordinate) == 2 and coordinate[0] in CHESS_BOARD_COLUMNS and coordinate[1] in CHESS_BOARD_ROWS

def parse_input(user_input):
    """Parses the user input into a piece and coordinate."""
    parts = user_input.split()
    if len(parts) != 2:
        return None, None
    piece, coordinate = parts
    if piece.lower() in VALID_CHESS_PIECES and is_valid_coordinate(coordinate):
        return piece.lower(), coordinate
    return None, None

def get_rook_moves(coord):
    """Returns all possible moves for a rook from a given position."""
    column, row = coord[0], coord[1]
    moves = set()
    for c in CHESS_BOARD_COLUMNS:
        if c != column:
            moves.add(c + row)
    for r in CHESS_BOARD_ROWS:
        if r != row:
            moves.add(column + r)
    return moves

def get_pawn_moves(coord):
    """Returns all possible capturing moves for a pawn from a given position."""
    column, row = coord[0], coord[1]
    row_index = CHESS_BOARD_ROWS.index(row)
    column_index = CHESS_BOARD_COLUMNS.index(column)
    moves = set()
    if row_index < len(CHESS_BOARD_ROWS) - 1:  # If not on the last row
        if column_index > 0:  # Capture to the left
            moves.add(CHESS_BOARD_COLUMNS[column_index - 1] + CHESS_BOARD_ROWS[row_index + 1])
        if column_index < len(CHESS_BOARD_COLUMNS) - 1:  # Capture to the right
            moves.add(CHESS_BOARD_COLUMNS[column_index + 1] + CHESS_BOARD_ROWS[row_index + 1])
    return moves

def get_moves(piece, coord):
    """Returns all possible moves for a given piece."""
    if piece == "rook":
        return get_rook_moves(coord)
    elif piece == "pawn":
        return get_pawn_moves(coord)
    return set()

# Chess Logic
white_piece = None
black_pieces = []

# Get the white piece
while not white_piece:
    user_input = input("Enter the white piece and its position (e.g., 'pawn a5'): ").strip()
    piece, coord = parse_input(user_input)
    if piece and coord:
        white_piece = (piece, coord)
        print(f"White piece added: {piece} at {coord}")
    else:
        print("Your input is Invalid. Enter a valid piece and position.")

# Get the black pieces
while len(black_pieces) < 16:
    user_input = input("Enter a black piece and its position (or 'done' to finish): ").strip()
    if user_input.lower() == "done":
        if len(black_pieces) >= 1:
            break
        else:
            print("There must be at least one black piece added before finishing.")
            continue

    piece, coord = parse_input(user_input)
    if piece and coord:
        if (piece, coord) in black_pieces:
            print(f"The black piece at {coord} is already added.")
        else:
            black_pieces.append((piece, coord))
            print(f"Black piece added: {piece} at {coord}")
    else:
        print("Your input is Invalid. Enter a valid piece and position.")

# Determine which black pieces can be taken
white_moves = get_moves(white_piece[0], white_piece[1])
capturable_pieces = [bp for bp in black_pieces if bp[1] in white_moves]

# Display the results
if capturable_pieces:
    print("The white piece can take these black pieces:")
    for piece, coord in capturable_pieces:
        print(f"{piece} at {coord}")
else:
    print("The white piece cannot take any black pieces.")

# Assumptions made:
# 1. The program only supports "pawn" and "rook" for white and black pieces.
# 2. A maximum of 16 black pieces can be added as per the requirements.
# 3. Duplicate black piece positions are not allowed.
# 4. The pawn only moves forward.
# 5. Input is case-insensitive for piece names and coordinates.
# 6. The program stops taking inputs once "done" is entered, if there is at least one black piece.
