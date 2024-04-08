import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox, QLabel
from PyQt5.QtGui import QIcon

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tic Tac Toe')
        self.setWindowIcon(QIcon('icon.png'))  # Set the window icon
        self.setGeometry(100, 100, 300, 340)
        self.setStyleSheet("background-color: #2c3e50; color: white;")  # Dark mode background and text color
        self.initUI()
        
    def initUI(self):
        self.grid_layout = QGridLayout()
        self.buttons = []
        self.current_player = '⭕️'  # Circle emoji for player 1
        
        self.player_label = QLabel(f"Player's turn: {self.current_player}", self)
        self.player_label.setStyleSheet("font-size: 16px;")
        self.grid_layout.addWidget(self.player_label, 0, 0, 1, 3)
        
        button_size = 100  # Adjust the size as needed
        
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton('', self)
                button.setMinimumSize(button_size, button_size)  # Set minimum size
                button.setStyleSheet("font-size: 24px;")  # Increase font size for emojis
                button.clicked.connect(lambda state, i=i, j=j: self.button_clicked(i, j))
                self.grid_layout.addWidget(button, i + 1, j)
                row.append(button)
            self.buttons.append(row)
        
        self.setLayout(self.grid_layout)
        
    def button_clicked(self, i, j):
        button = self.buttons[i][j]
        if button.text() == '':
            button.setText(self.current_player)
            if self.check_winner():
                QMessageBox.information(self, 'Winner!', f'Player {self.current_player} wins!')
                self.reset_board()
            else:
                self.current_player = '❌' if self.current_player == '⭕️' else '⭕️'  # Switch between X and circle emojis
                self.player_label.setText(f"Player's turn: {self.current_player}")
    
    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != '':
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != '':
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != '':
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != '':
            return True
        return False
    
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
        self.current_player = '⭕️'  # Reset to circle emoji for player 1
        self.player_label.setText(f"Player's turn: {self.current_player}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))  # Set the application icon
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
