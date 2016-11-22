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
					m[i][j] = 0
				last = j

			m[i] = self.shift_l(m[i])

		for row in m:
			row += [0] * (self.b_siz - len(row))


		self.board = m
		print "after move:"
		self.print_board()




			


	def move_r(row):
		pass

	def move_u(row):
		pass

	def move_d(row):
		pass
		
	def print_board(self):
		for row in self.board: print row

	def are_there_possible_moves(self):
		for row in self.board:
			for cell in row:
				if cell == 0:
					return True

		return False

	def get_next_move(self):
		# return random.choice(self.possible_moves)
		return 'l'

	def place_2_in_a_random_cell(self):
		print "placing a random 2 in: "
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
		print "placed:"
		# self.print_board() *printerase#0*
		return True


	def play(self):
		while self.place_2_in_a_random_cell():
			self.move[self.get_next_move()]()
			print "after move:"
			# self.print_board() *printerase#0*
			print "======================================================"



def main ():
	print "input the dimension of the board:	",
	b_siz = int(raw_input())	# board size



	game = board_2048(b_siz)
	game.play()

	print "game over!"

	# game.print_board()
	





if __name__ == '__main__':
	main()