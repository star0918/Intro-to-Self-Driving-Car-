import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        # if matrix is a 1x1 matrix, then return the only value, self.g[0][0]
        # if matrix is a 2x2 matrix, 
        #   [[ a , b],
        #    [ c , d]]
        #then det = ad - bc
        if self.h == 1 :
            return self.g[0][0]
        else :
            return self.g[0][0]*self.g[1][1]-self.g[1][0]*self.g[0][1]
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            trace+=self.g[i][i]
        return trace
        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.determinant()==0:
            raise(ValueError, "Singular Matrix does not have an inverse.")
        # TODO - your code here
        # if matrix is a 2x2 matrix, 
        #   [[ a , b],
        #    [ c , d]]
        #then inverse of the matrix = 
        #           [[ d , -c],
        #  (1/det)*  [ -b , a]]
        res=zeroes(self.h, self.w)
        if self.h == 1 :
            if self.g[0][0] != 0 : 
               res.g[0][0]=1/self.g[0][0]           
        else :
            res.g[0][0]=float(self.g[1][1])/self.determinant()
            res.g[1][1]=float(self.g[0][0])/self.determinant()
            res.g[1][0]=-1.0*self.g[1][0]/self.determinant()
            res.g[0][1]=-1.0*self.g[0][1]/self.determinant()
                        
        return res
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
         #The transpose of a matrix is a new matrix whose rows are the columns of the original
        res=zeroes(self.w, self.h)
        for i in range(self.w):
            for j in range(self.h):  
                res[i][j]=self.g[j][i]
        return res
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        res=zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                res.g[i][j]=self.g[i][j]+other.g[i][j]

        return res

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        res=zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):               
                 res.g[i][j]=self.g[i][j]*(-1)
                        
        return res
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        res=zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                res.g[i][j]=self.g[i][j]-other.g[i][j]

        return res
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        # First, we need to make sure the dimention matches
        if self.w!=other.h:
            raise(ValueError, "Matrices can only be multipled if self.w==other.h") 
            
        res=zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                res.g[i][j]=0
                for k in range(self.w):
                    res.g[i][j]+=self.g[i][k]*other.g[k][j]
        return res
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            res=zeroes(self.h, self.w)
            for i in range(self.h):
                for j in range(self.w):
                    res.g[i][j]=self.g[i][j]*other
        return res
            
