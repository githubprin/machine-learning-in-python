from numbers import Numbers 
from typing import Callable, Iterable, Union

import config 
from formula import Formula 
from ADT.graph import Graph, Node, Edge 

class VariableNode(Node):
    def __init__(self, variable: str, value: Numbers):
        self.variable = variable
        self.value = value 

class OperationNode(Node):
    def __init__(self, operation: Callable):
        self.operation = operation  

class CompuationalGraph(Graph):
    def __init__(self, V: Iterable[Union[VariableNode, OperationNode]], E: Iterable[Edge]):
        super().__init__(graph.V, graph.E)

    def __call__(self, x: Numbers) -> Numbers:
        pass 

    def backpropagate(self, datum: Numbers, learning_rate: Numbers) -> None: 
        pass 

    @staticmethod 
    def formula_to_computational_grpah(formula: Formula, input_variable: str = 'x', output_variable: str = 'y') -> CompuationalGraph:
        pass     

class MachineLearningModel:
    def __init__(self, model, input_variable = 'x', output_variable = 'y', ):
        f = Formula(model)
        self.model = f
        self.computational_graph = formula_to_computational_grpah(f, input_variable = input_variable, output_variable = output_variable)

    def train(input_train_data: Iterable[Numbers], output_train_data: Iterable[Numbers]):
        pass 

    def test(input_test_data: Iterable[Numbers], output_test_data: Iterable[Numbers]):
        pass 


linear_regression = MachineLearningModel('y=ax+b')

if __name__ == '__main__':
    linear_regression.train() # equivalent to fit 



