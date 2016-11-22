import random
import copy


class board_2048(object):
	"""docstring for board_2048"""
	def __init__(self, b_siz):
		self.b_siz = b_siz
		self.board = [b_siz * [0] for i in range(b_siz)]
		self.possible_moves = ['l', 'r', 'u', 'd']
		self.move = {}
		self.move['l'] = self.move_l
		self.move['r'] = self.move_r
		self.move['u'] = self.move_u
		self.move['d'] = self.move_d


	def transpose_board(self):
		m = [self.b_siz * [0] for i in range(self.b_siz)]
		for i in range(self.b_siz):
			for j in range(self.b_siz):
				m[i][j] = self.board[j][i]

		self.board = m

	def reflect_board(self):
		m = [self.b_siz * [0] for i in range(self.b_siz)]
		for i in range(self.b_siz):
			for j in range(self.b_siz):
				m[i][j] = self.board[i][self.b_siz -1 - j]

		self.board = m

	def shift_l(self, row): return [i for i in row if i != 0]

	def move_l(self):
		print "before move:"
		self.print_board()

		move_score = 0
		m = []
		for row in self.board:
			m.append(self.shift_l(row))

		score = 0
		for i in range(len(m)):
			# print "this should be shifted: ", m[i]
			last = 0
			for j in range(1, len(m[i])):
				if (m[i][j] != 0) and (m[i][j] == m[i][last]):
					m[i][last] *= 2
					score += m[i][last]
					m[i][j] = 0
				last = j

			m[i] = self.shift_l(m[i])

		for row in m:
			row += [0] * (self.b_siz - len(row))


		self.board = m
		print "after move:"
		self.print_board()

		return score


	def move_r(self):
		self.reflect_board()
		score = self.move_l()
		self.reflect_board()
		return score


	def move_u(self):
		self.transpose_board()
		score = self.move_l()
		self.transpose_board()
		return score


	def move_d(self):
		self.transpose_board()
		self.reflect_board()
		score = self.move_l()
		self.reflect_board()
		self.transpose_board()
		return score
		
	def print_board(self):
		for row in self.board: print row

	def are_there_possible_moves(self):
		for row in self.board:
			for cell in row:
				if cell == 0:
					return True

		return False

	def get_next_move(self):

		max_score = 0
		max_move = None

		move_evaluation = {}
		board_backup = copy.deepcopy(self.board)

		for move in self.possible_moves:
			print "* evaluatiing score of moving: ", move
			self.board = copy.deepcopy(board_backup)
			move_evaluation[move] = self.move[move]()
			if move_evaluation[move] > max_score:
				max_score = move_evaluation[move]
				max_move = move
			print "\t\tmoving ", move, "generates score of ", max_score, "."

		
		self.board = copy.deepcopy(board_backup)

		if max_move: 	return max_move
		else: 			return random.choice(self.possible_moves)


		


	def place_2_in_a_random_cell(self):
		# print "placing a random 2 in: " *printerase#1*
		# self.print_board() *printerase#0*
		empty_cells = []
		for i in range(self.b_siz):
			for j in range(self.b_siz):
				if (self.board[i][j] == 0): 
					empty_cells.append((i,j))

		# print "empty_cells: ",
		# print empty_cells
		if not empty_cells: return False # 
		random_cell = random.choice(empty_cells)
		i = random_cell[0]
		j = random_cell[1]
		self.board[i][j] = 2
		# print "placed:" *printerase#1*
		# self.print_board() *printerase#0*
		return True


	def play(self):
		score = 0
		while self.place_2_in_a_random_cell():
			print "board state:"
			self.print_board()
			print "\n"
			next_move = self.get_next_move()
			print ">>>>> moving ", next_move, "!"
			score += self.move[next_move]()
			print "======================================================"

		return score




def main ():
	print "input the dimension of the board:	",
	b_siz = int(raw_input())	# board size

	game = board_2048(b_siz)
	score = game.play()

	print "======================================================"
	print "======================================================"
	print "======================================================"
	print "game over! score: ", score

	game.print_board()






if __name__ == '__main__':
	main()