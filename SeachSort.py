class Sort(object):
	"""docstring for Sort"""
	def __init__(self, array):
		self.array=array
		self.n=len(self.array)
	@property
	def bubble(self):#ca c'est le tri a bulle
		for i in range(self.n):
			for j in range(0,self.n-1-i):
				if(self.array[j]>self.array[j+1]):
					self.array[j+1],self.array[j]=self.array[j],self.array[j+1]
		return self.array
	@property 
	def selection(self):#tri par selection
		self.min=0
		for i in range(self.n):
			self.min=i
			for j in range(i+1,self.n):
				if(self.array[self.min]>self.array[j]):
					self.min=j
			self.array[i],self.array[self.min]=self.array[self.min],self.array[i]
		return self.array

class Search(object):
	def __init__(self):
		pass
	def linear_search(self,tableau,element):#recherche sentinelle
		self.tableau=tableau
		self.data=element
		self.present=False
		self.pos=[]#dans cette liste je vais stocker tous les position ou l'element a ete trouver
		self.n=len(self.tableau)
		for i in range(len(self.tableau)):
			if(self.tableau[i]==self.data):
				self.pos.append(i+1)
				self.present=True
		if self.present==True:
			print('Element ',self.data,' trouver dans le tableau ',self.tableau,' a la position',self.pos)
		else:
			print("L'element ",self.data," n'apparrait pas dans le tableau ",self.tableau)
	def binary_search(self,tableau,element):
		#cette method de tri fonctione quand le tableau est trier
		#m'est comme j'ai deja la fonction pour trier je vais l'utiliser
		self.tableau=tableau
		self.data=element
		self.high=len(self.tableau)-1
		self.low=0
		self.found=False
		self.mid=0
		self.tableau=Sort(self.tableau).bubble
		while self.low<=self.high:
			self.mid=(self.high+self.low)//2
			if self.tableau[self.mid]==self.data:
				self.found=True
				print("L'element ",self.data," trouver dans le tableau",self.tableau," a la position ",self.mid+1)
				break
			else:
				if self.data<self.tableau[self.mid]:
					self.high=self.mid-1
				else:
					self.low=self.mid+1
		if self.found==False:
			print("L'element ",self.data," n'aparrait pas dans le tableau ",self.tableau)

p=Sort([-14,140,15,-1,2,4])
print(" 1 .Le tableu ",[-14,140,15,-1,2,4],"trier en utilsant le tri a bubble ")
print(p.bubble,end='\n\n')

S=Sort([1,6,3,9,5,-17,-89,45])
print(" 2. Le tableu ",[1,6,3,9,5,-17,-89,45],"trier en utilsant le tri par selection")
print(S.selection,end='\n\n')

ive=Search()
print(' 3. En utilisant la recherche sentinelle :',end='\n\n')
ive.linear_search([1,5,6,7,9,1,2,1],1)
print(' 4. En utilisant la recherche "binary search" :',end='\n\n')
ive.binary_search([1,5,6,7,9,1,2,1],1)

print(' 5. En utilisant la recherche sentinelle :',end='\n\n')
ive.linear_search([1,5,6,7,9,1,2,1],10)
print(' 6. En utilisant la recherche "binary search" :',end='\n\n')
ive.binary_search([1,5,6,7,9,1,2,1],15)

#par Ivan Tom
