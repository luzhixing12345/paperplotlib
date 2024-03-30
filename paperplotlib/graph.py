import matplotlib.pyplot as plt


class Graph:
    """
    图表
    """

    def __init__(self) -> None:
        self.fig = plt.figure(num=1, figsize=(4, 4))
    

    def show(self):
        plt.show()
        
    def save(self, path: str = 'result.png', wide_picture=False):
        '''

        '''
        plt.plot()