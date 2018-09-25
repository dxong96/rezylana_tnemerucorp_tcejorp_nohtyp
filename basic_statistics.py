from function_3 import function_3
from function_4 import function_4
from function_5 import function5

def generate_stats():
    result = []
    result.append("FUNCTION 3 START")
    result.append(function_3(True))
    result.append("FUNCTION 3 END")
    result.append("FUNCTION 4 START")
    result.append(function_4())
    result.append("FUNCTION 4 END")
    result.append("FUNCTION 5 START")
    result.append(function5())
    result.append("FUNCTION 5 END")
    return '\n'.join(result)