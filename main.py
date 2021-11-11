import matplotlib.pyplot as plt
import numpy
import numpy as np

Matrix = [[4, -1, 0, -1, 0, 0, 0, 0, 0],
          [-1, 4, -1, 0, -1, 0, 0, 0, 0],
          [0, -1, 4, 0, 0, -1, 0, 0, 0],
          [-1, 0, 0, 4, -1, 0, -1, 0, 0],
          [0, -1, 0, -1, 4, -1, 0, -1, 0],
          [0, 0, -1, 0, -1, 4, 0, 0, -1],
          [0, 0, 0, -1, 0, 0, 4, -1, 0],
          [0, 0, 0, 0, -1, 0, -1, 4, -1],
          [0, 0, 0, 0, 0, -1, 0, -1, 4]]

plt.spy(Matrix)
plt.show()
Solv = [0.0625,
        0.0625,
        0.0625,
        0.0625,
        0.0625,
        0.0625,
        0.0625,
        0.0625,
        0.0625]
print(np.linalg.solve(numpy.array(Matrix), numpy.array(Solv)))
