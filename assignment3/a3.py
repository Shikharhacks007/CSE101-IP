import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''

    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None

    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg * (np.pi / 180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]])

    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''

        x_dim, y_dim = 1.2 * x_dim, 1.2 * y_dim
        plt.plot((-x_dim, x_dim), [0, 0], 'k-')
        plt.plot([0, 0], (-y_dim, y_dim), 'k-')
        plt.xlim(-x_dim, x_dim)
        plt.ylim(-y_dim, y_dim)
        plt.grid()
        plt.show()


class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''

    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A = A
        self.A_or = A

    def translate(self, dx, dy=None, alpha=0):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''

        if alpha == 0:                                       # if the function is called from outside the
            self.dx = dx                                     # class then there is no need to store old A,hence alpha=0
            self.dy = dy
            if self.dy is None:
                self.dy = dx
            else:
                self.dy = dy

            self.A_or = self.A
            Shape.translate(self, self.dx, self.dy)          # initializes the translate matrix in parent class
            final = np.dot(self.T_t, np.transpose(self.A))   # calculates the dot product between two matrices
            self.A = np.transpose(final).tolist()            # a transpose is used to get all x,y,z co ordinates
            x_p, y_p, z_p = zip(*self.A)
            x_p = list(x_p)
            x_p = [np.round(i, 2) for i in x_p]              # rounding every element before sending
            y_p = list(y_p)
            y_p = [np.round(i, 2) for i in y_p]              # rounding every element before sending
            return x_p, y_p
        else:
            self.dx = dx
            self.dy = dy
            if self.dy is None:
                self.dy = dx
            else:
                self.dy = dy
            Shape.translate(self, self.dx, self.dy)             # translates the object to the desired place
            final = np.dot(self.T_t, np.transpose(self.A))      # calculates the dot product between two matrices
            self.A = np.transpose(final).tolist()               # a transpose is used to get all x,y,z co ordinates
            x_p, y_p, z_p = zip(*self.A)
            x_p = list(x_p)
            x_p = [np.round(i, 2) for i in x_p]                 # rounding every element before sending
            y_p = list(y_p)
            y_p = [np.round(i, 2) for i in y_p]                 # rounding every element before sending
            return x_p, y_p

    def scale(self, sx, sy):
        '''
        Function to scale the polygon

        This function takes 2 arguments: sx and sx

        This function returns the final coordinates
        '''
        self.sx = sx
        self.sy = sy
        # import copy
        temp = self.A
        tempx = []
        tempy = []
        for i in self.A:                            # finding the centre of the object to find the centre of the object
            tempx.append(i[0])
            tempy.append(i[1])
        mid_x = sum(tempx) / len(tempx)
        mid_y = sum(tempy) / len(tempy)

        self.translate(-1 * mid_x, -1 * mid_y, 1)   # translating the object to the centre to rotate
        Shape.scale(self, self.sx, self.sy)         # initializing the scale matrix in parent class
        coordinates = np.transpose(self.A)          # finding the transpose
        final = np.dot(self.T_s, coordinates)       # finding the dot product of matrices
        self.A = np.transpose(final).tolist()       # transposing back
        self.translate(mid_x, mid_y, 1)             # translating object back to the moved place

        x_p, y_p, z_p = zip(*self.A)
        x_p = list(x_p)
        x_p = [np.round(i, 2) for i in x_p]
        y_p = list(y_p)
        y_p = [np.round(i, 2) for i in y_p]
        self.A_or = temp
        return x_p, y_p

    def rotate(self, deg, rx=0, ry=0):
        '''
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates
        '''
        self.deg = deg
        self.rx = rx
        self.ry = ry
        temp = self.A
        self.translate(-1 * self.rx, -1 * self.ry, 1)           # translating to the origin to make the rotation
        Shape.rotate(self, self.deg)                            # initializing the rotation matrix in the shape class
        final = []
        final = np.dot(self.A, np.transpose(self.T_r))          # finding the dot product of two matrices
        self.A = final
        self.translate(self.rx, self.ry, 1)                     # translating back to the position

        x_p, y_p, z_p = zip(*self.A)                            # getting x ,y,z co ordinates
        x_p = list(x_p)
        x_p = [np.round(i, 2) for i in x_p]
        y_p = list(y_p)
        y_p = [np.round(i, 2) for i in y_p]
        self.A_or = temp
        return x_p, y_p

    def plot(self):
        '''
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''

        figure, axes = plt.subplots()           # using subplots to make the axis
        self.A_or.append(self.A_or[0])          # appending a point in the back so that a closed figure is formed
        x, y, z = zip(*self.A_or)
        plt.plot(x, y, linestyle="--")          # plotting the old figure with dashed lines
        self.A_or.pop()
        self.A.append(self.A[0])
        xs, ys, zs = zip(*self.A)
        plt.plot(xs, ys, linestyle="-")         # plotting the new figure with filled lines
        axes.set_aspect(1)
        x_dim = max(max(x),max(xs),abs(min(x)),abs(min(xs)))  # max(abs(x),abs(xs))
        y_dim =max(max(y),max(ys),abs(min(y)),abs(min(ys)))
        Shape.plot(self, x_dim, y_dim)          # plotting the figure by calling the parent plot
        self.A.pop()

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''

    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.or_x = x
        self.or_y = y
        self.or_radius = radius

    def translate(self, dx, dy, alpha=0):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''

        if alpha == 0:                                      # if the function is called from outside the
            self.dx = dx                                    # class then there is no need to store old A,hence alpha=0
            self.dy = dy
            self.or_x = self.x
            self.or_y = self.y
            self.or_radius = self.radius

            Shape.translate(self, dx, dy)                   # translating the object to the desired position
            c = np.array([[self.x], [self.y], [1]])
            final = np.dot(self.T_t, c)                     # calculating the dot product

            self.x = np.round(final[[0][0]][0], 2)
            self.y = np.round(final[[1][0]][0], 2)
            self.radius = np.round(self.radius, 2)
            return np.round(self.x, 2), np.round(self.y, 2), np.round(self.radius, 2)

        else:                                               # if the function is called from outside the class
            self.dx = dx
            self.dy = dy
            Shape.translate(self, dx, dy)
            c = np.array([[self.x], [self.y], [1]])
            final = np.dot(self.T_t, c)

            self.x = np.round(final[[0][0]][0], 2)
            self.y = np.round(final[[1][0]][0], 2)
            self.radius = np.round(self.radius, 2)
            return np.round(self.x, 2), np.round(self.y, 2), np.round(self.radius, 2)

    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''

        Shape.scale(self, sx, sx)                               # initializing the scale matrix in the parent class
        self.or_radius = self.radius
        s = np.array([[self.radius], [self.radius], [1]])
        final = np.dot(self.T_s, s)                             # finding th dot product of two matrices
        self.radius = final[0][0]
        return np.round(self.x, 2), np.round(self.y, 2), np.round(self.radius, 2)

    def rotate(self, deg, rx=0, ry=0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.or_x = self.x
        self.or_y = self.y
        self.radius  = self.radius
        temp = Polygon([[self.x, self.y, 1]])
        x, y = temp.rotate(deg, rx, ry)
        self.x = x[0]
        self.y = y[0]
        return np.round(self.x, 2), np.round(self.y, 2), np.round(self.radius, 2)  # sending rounded values

        # self.deg = deg
        # self.rx = rx
        # self.ry = ry
        #
        # self.translate(-1.0 * self.rx, -1.0 * self.ry)
        # Shape.rotate(self, self.deg)
        # coordinates = np.array([self.x, self.y, 1])
        # final = np.dot(self.T_r, coordinates)
        # temp = np.transpose(final).tolist()
        # self.x = temp[0]
        # self.y = temp[1]
        # return np.round(self.x, 2), np.round(self.y, 2), np.round(self.radius, 2)

    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        figure, axes = plt.subplots()                        # creates subplots to define axis and other components
        old = plt.Circle((self.x, self.y), self.radius, fill=False, linestyle="-") # stores the old circle
        new = plt.Circle((self.or_x, self.or_y), self.or_radius, fill=False, linestyle="--")  # stores the new circle
        axes.set_aspect(1)  # sets the aspect ratio to 1
        axes.add_artist(old)    # adds the circle onto the graph
        axes.add_artist(new)    # adds the circle onto the graph

        x_dim = max([abs(self.x)+abs(self.radius)+2,abs(self.or_x)+abs(self.or_radius)+2])
        y_dim = max([abs(self.y)+abs(self.radius)+2,abs(self.or_x)+abs(self.or_radius)+2])
        Shape.plot(self, x_dim, y_dim)  # calls the parent plot to plot the graph
        self.or_x = self.x
        self.or_y = self.y
        self.or_radius = self.radius


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    queries = ["R deg (rx) (ry)", "T dx (dy)", "S sx (sy)", "P"]
    verbose = int(input("to plot after transformation Enter 1 or 0: "))
    if verbose == 1:
        co = []
        test_case = int(input("Enter the number of test cases: "))
        for i in range(test_case):
            shape = int(input("Enter the type of shape: "))
            if shape == 0:
                co = []
                sides = int(input("Enter the number of Sides: "))
                for j in range(sides):
                    temp = list(map(float, input("enter (x{},y{}): ".format(j + 1, j + 1)).split()))
                    temp.append(1)
                    co.append(temp)
                q = int(input("Enter the number of Quries: "))
                for l in range(len(queries)):
                    print(str(l+1) +")"+ str(queries[l]))

                p = Polygon(co)
                for m in range(q):
                    to_do = list(map(str, input().split()))
                    if to_do[0] == "R":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))
                        while len(args) < 3:
                            args.append(0)
                        x, y, z = zip(*p.A)
                        x = [np.round(space, 2) for space in x]
                        y = [np.round(space, 2) for space in y]
                        for point in x:
                            print(point, end = " ")
                        for point in y:
                            print(point, end=" ")

                        print()
                        po, go = p.rotate(float(args[0]), float(args[1]), float(args[2]))
                        for p_o in po:
                            print(p_o, end=" ")
                        for g_o in go:
                            print(g_o, end=" ")
                        print()
                        p.plot()

                    elif to_do[0] == "T":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))
                        while len(args) < 2:
                            args.append(args[0])
                        x, y, z = zip(*p.A)
                        x = [np.round(space, 2) for space in x]
                        y = [np.round(space, 2) for space in y]
                        for point in x:
                            print(point, end = " ")
                        for point in y:
                            print(point, end=" ")

                        print()
                        po, go = p.translate(float(args[0]), float(args[1]))
                        for p_o in po:
                            print(p_o, end=" ")
                        for g_o in go:
                            print(g_o, end=" ")
                        print()
                        p.plot()

                    elif to_do[0] == "S":
                        args = []
                        # print(to_do[1:])
                        for n in to_do[1:]:
                            args.append(float(n))

                        while len(args) < 2:
                            args.append(args[0])

                        x, y, z = zip(*p.A)
                        x = [np.round(space, 2) for space in x]
                        y = [np.round(space, 2) for space in y]
                        for point in x:
                            print(point, end = " ")
                        for point in y:
                            print(point, end=" ")

                        print()
                        po, go = p.scale(float(args[0]), float(args[1]))
                        for p_o in po:
                            print(p_o, end=" ")
                        for g_o in go:
                            print(g_o, end=" ")
                        print()
                        p.plot()

                    elif to_do[0] == "P":
                        args = []
                        # print(to_do[1:])
                        for n in to_do[1:]:
                            args.append(float(n))

                        p.plot()

                    elif to_do[0] == "-1":
                        break

                    else:
                        continue

            elif shape == 1:
                co = list(map(float, input("Enter the centre and the Radius of the Circle: ").split()))
                c = Circle(co[0], co[1], co[2])
                q = int(input("Enter the number of Quries"))
                for l in range(len(queries)):
                    print(str(l+1) +")"+ str(queries[l]))
                for l in range(0, q):
                    to_do = list(map(str, input().split()))

                    if to_do[0] == "R":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))

                        while len(args) < 3:
                            args.append(0)

                        print(float(c.x), float(c.y), float(c.radius))
                        po = c.rotate(float(args[0]), float(args[1]), float(args[2]))
                        for p_o in po:
                            print(p_o, end=" ")
                        print()
                        c.plot()

                    elif to_do[0] == "T":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))

                        while len(args) < 2:
                            args.append(args[0])
                        print(c.x, c.y, c.radius)
                        po = c.translate(float(args[0]), float(args[1]))
                        for p_o in po:
                            print(p_o, end=" ")
                        print()
                        c.plot()

                    elif to_do[0] == "S":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))

                        print(c.x, c.y, c.radius)
                        po = c.scale(float(args[0]))
                        for p_o in po:
                            print(p_o, end=" ")
                        print()
                        c.plot()

                    elif to_do[0] == "P":
                        c.plot()

                    elif to_do[0] == "-1":
                        break

                    else:
                        continue

            elif shape == -1:
                break

            else:
                continue

    else:
        co = []
        test_case = int(input("Enter the number of test cases: "))
        for i in range(test_case):
            shape = int(input("Enter the type of shape: "))
            if shape == 0:
                sides = int(input("Enter the number of Sides: "))
                for j in range(sides):
                    temp = list(map(float, input("enter (x{},y{}): ".format(j + 1, j + 1)).split()))
                    temp.append(1)
                    co.append(temp)
                q = int(input("Enter the number of Quries: "))
                for l in range(len(queries)):
                    print(str(l + 1) + ")" + str(queries[l]))

                p = Polygon(co)
                for m in range(q):
                    to_do = list(map(str, input().split()))

                    if to_do[0] == "R":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))
                        while len(args) < 3:
                            args.append(0)

                        x, y, z = zip(*p.A)
                        x = [np.round(space, 2) for space in x]
                        y = [np.round(space, 2) for space in y]
                        for point in x:
                            print(point, end=" ")
                        for point in y:
                            print(point, end=" ")

                        print()
                        po, go = p.rotate(float(args[0]), float(args[1]), float(args[2]))
                        for p_o in po:
                            print(p_o, end=" ")
                        for g_o in go:
                            print(g_o, end=" ")
                        print()

                    elif to_do[0] == "T":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))
                        while len(args) < 2:
                            args.append(args[0])

                        x, y, z = zip(*p.A)
                        x = [np.round(space, 2) for space in x]
                        y = [np.round(space, 2) for space in y]
                        for point in x:
                            print(point, end=" ")
                        for point in y:
                            print(point, end=" ")

                        print()
                        po, go = p.translate(float(args[0]), float(args[1]))
                        for p_o in po:
                            print(p_o, end=" ")
                        for g_o in go:
                            print(g_o, end=" ")
                        print()

                    elif to_do[0] == "S":
                        args = []
                        # print(to_do[1:])
                        for n in to_do[1:]:
                            args.append(float(n))

                        while len(args) < 2:
                            args.append(args[0])

                        x, y, z = zip(*p.A)
                        x = [np.round(space, 2) for space in x]
                        y = [np.round(space, 2) for space in y]
                        for point in x:
                            print(point, end=" ")
                        for point in y:
                            print(point, end=" ")

                        print()
                        po, go = p.scale(float(args[0]), float(args[1]))
                        for p_o in po:
                            print(p_o, end=" ")
                        for g_o in go:
                            print(g_o, end=" ")
                        print()

                    elif to_do[0] == "-1":
                        break

                    else:
                        continue

            elif shape == 1:
                co = list(map(float, input("Enter the centre and the Radius of the Circle: ").split()))
                c = Circle(co[0], co[1], co[2])
                q = int(input("Enter the number of Quries"))
                for l in range(len(queries)):
                    print(str(l + 1) + ")" + str(queries[l]))
                for l in range(0, q):
                    to_do = list(map(str, input().split()))

                    if to_do[0] == "R":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))

                        while len(args) < 3:
                            args.append(0)

                        print(float(c.x), float(c.y), float(c.radius))
                        po = c.rotate(float(args[0]), float(args[1]), float(args[2]))
                        for p_o in po:
                            print(p_o, end=" ")
                        print()

                    elif to_do[0] == "T":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))

                        while len(args) < 2:
                            args.append(args[0])
                        print(c.x, c.y, c.radius)
                        po = c.translate(float(args[0]), float(args[1]))
                        for p_o in po:
                            print(p_o, end=" ")
                        print()

                    elif to_do[0] == "S":
                        args = []
                        for n in to_do[1:]:
                            args.append(float(n))

                        print(c.x, c.y, c.radius)
                        po = c.scale(float(args[0]))
                        for p_o in po:
                            print(p_o, end=" ")
                        print()

                    elif to_do[0] == "-1":
                        break

                    else:
                        continue

            elif shape == -1:
                break

            else:
                continue


print()
print("Thank you for using our geometric Visualizer and maker")
print("Stay home and stay safe")
