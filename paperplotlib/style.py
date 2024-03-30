
from enum import Enum

class FontFamily(Enum):
    TIMES = 'Times New Roman'
    HELVETICA = 'Helvetica'
    
    
class GraphColor(Enum):
    BLACK = 'black'
    WHITE = 'white'
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    ORANGE = 'orange'
    PURPLE = 'purple'
    PINK = 'pink'
    
class GraphColomnStyle(Enum):
    FILL = 'fill'
    OUTLINE = 'outline'
    NONE = 'none'
