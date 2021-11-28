import os
import copy

class Level:

	matrix = []
	matrix_history = []
	
	def __init__(self,set,level_num):   
		
		del self.matrix[:]
		del self.matrix_history[:]

		# Create level
		with open(os.path.dirname(os.path.abspath(__file__)) + '/levels/' + set + '/level' + str(level_num), 'r') as f:
			for row in f.read().splitlines():     
				self.matrix.append(list(row))	

	
		
	def getMatrix(self):	#trả về giá trị là 1 ma trận mới
		return self.matrix  

	def addToHistory(self,matrix):	#lưu lịch sử di chuyển của người chơi vào matrix_history
		self.matrix_history.append(copy.deepcopy(matrix))


	def getLastMatrix(self): 	#pop ma trận đã được lưu ở matrix_history mỗi khi bấm U để hoàn tác
		if len(self.matrix_history) > 0:
			lastMatrix = self.matrix_history.pop()	
			self.matrix = lastMatrix		
			return lastMatrix
		else:
			return self.matrix		
	
	
	#lấy vị trí người chơi
	def getPlayerPosition(self):     
		for i in range (0,len(self.matrix)):
			for k in range (0,len(self.matrix[i])-1):
				if self.matrix[i][k] == "@":
					return [k,i]	

	def getBoxes(self):	# lấy vị trí những thùng hàng chưa được đẩy về đích
		boxes = []    
		for i in range (0,len(self.matrix)):
			for k in range (0,len(self.matrix[i])-1):
				if self.matrix[i][k] == "$":
					boxes.append([k,i])
		return boxes
	def getTarget(self):  #lấy vị trí các điểm đích khi chưa có thùng hàng được đẩy vào
		target=[]
		for i in range (0,len(self.matrix)):
			for k in range (0,len(self.matrix[i])-1):
				if self.matrix[i][k] == ".":
					target.append([k,i])
		return target

		