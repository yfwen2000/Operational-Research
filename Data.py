import numpy as np


def load_data():
    # # Problem 1-5(2)
    # # infinite optimal solution
    # A = np.array([[1, -1, -1,  0],
    #               [1, -5,  0, -1]])
    # b = np.array([0, -5])
    # C = np.array([2, -10, 0, 0])

    # # Problem 1-6(2)
    # # optimal value: -15.0000
    # # optimal variable: X = [0, 5, 0, 6, 0, 2].T
    # A = np.array([[3, 1, 2, 0, 1, 0],
    #               [1, 0, 1, 0, 2, 1],
    #               [1, 0, 2, 1, 2, 0]])
    # b = np.array([5, 2, 6])
    # C = np.array([-1, -3, -3, 0, 0, 0])

    # # Problem 1-6(3)
    # # optimal value: -3.5000
    # # optimal variable: X = [0, 3, 1, 0, 0, 1.5].T
    # A = np.array([[3, 1, -4, 0, 0, 2],
    #               [1, 0,  0, 1, 0, 6],
    #               [1, 0,  3, 0, 1, 2]])
    # b = np.array([2, 9, 6])
    # C = np.array([1, -1, 1, 1, 1, -1])

    # # Problem 1-7(2)
    # # finite optimal solution
    # A = np.array([[1,  1, -1,  0],
    #               [1, -1,  0, -1]])
    # b = np.array([1, 0])
    # C = np.array([-1, -1, 0, 0])

    # # Problem 2-2(1)
    # # Dual with the off-the-shelf base
    # # optimal value: 4.0000
    # # optimal variable: X = [4, 0, 0, 0, 4, 2].T
    # A = np.array([[-1, 1, -1, 1, 0, 0],
    #               [ 1, 1,  2, 0, 1, 0],
    #               [-1, 0,  1, 0, 0, 1]])
    # b = np.array([-4, 8, -2])
    # C = np.array([1, 2, 3, 0, 0, 0])

    # Problem 2-2(2) Dual
    # optimal value: 9.0000
    # optimal variable: X = [3, 0, 0, 0, 6, 4, 0].T
    # optimal dual variable: Lambda = [0, 0, -0.6]
    A = np.array([[-2, -4, -5, -1, 1, 0, 0],
                  [-2,  1, -7,  2, 0, 1, 0],
                  [-5, -2, -1, -6, 0, 0, 1]])
    b = np.array([0, -2, -15])
    C = np.array([3, 2, 1, 4, 0, 0, 0])

    # # Example 2-2, Page 45
    # # optimal value: 11.0000
    # # optimal variable: X = [1, 2, 0, 0, 0].T
    # # optimal dual variable: Lambda = [-1, -1]
    # A = np.array([[-1, -2, -3, 1, 0],
    #               [-2, -2, -1, 0, 1]])
    # b = np.array([-5, -6])
    # C = np.array([3, 4, 5, 0, 0])

    # x = int(input("input the num of constraint: "))
    # print("input the matrix A:")
    # A = []
    # for _ in range(x):
    #     A.append(list(map(int, input().split())))
    # b = list(map(int, input("input b separated by spaces: ").split()))
    # C = list(map(int, input("input C for all variables separated by spaces: ").split()))
    # A = np.array(A)
    # b = np.array(b)
    # C = np.array(C)

    return A, b, C
