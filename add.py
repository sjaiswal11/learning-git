class Sum:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def sum(self):
        return self.number1 + self.number2
    
    if __name__ == '__main__':
        sum1 = sum(23,34)
        print(sum1.sum())