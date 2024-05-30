import streamlit as st

# Initialize the game state
if 'game_state' not in st.session_state:
    st.session_state.game_state = [' ']*9
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

# Function to check for a winner
def check_winner(state):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if state[condition[0]] == state[condition[1]] == state[condition[2]] != ' ':
            return state[condition[0]]
    if ' ' not in state:
        return 'Draw'
    return None

# Function to handle a move
def make_move(index):
    if st.session_state.game_state[index] == ' ' and not st.session_state.game_over:
        st.session_state.game_state[index] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.game_state)
        if st.session_state.winner:
            st.session_state.game_over = True
        else:
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Display the game board
def display_board():
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            index = i*3 + j
            if st.session_state.game_state[index] == ' ' and not st.session_state.game_over:
                cols[j].button(' ', key=index, on_click=make_move, args=(index,))
            else:
                cols[j].button(st.session_state.game_state[index], key=index, disabled=True)

# Display the current game status
st.title("Tic-Tac-Toe")
display_board()
if st.session_state.winner:
    if st.session_state.winner == 'Draw':
        st.write("It's a draw!")
    else:
        st.write(f"Player {st.session_state.winner} wins!")
else:
    st.write(f"Current player: {st.session_state.current_player}")

# Reset button
if st.button('Restart Game'):
    st.session_state.game_state = [' ']*9
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False
