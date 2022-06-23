from abc import abstractclassmethod, abstractmethod
import abc

class FormalAlgorithmInterface(metaclass = abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'run') and 
        callable(subclass.run) and
        hasattr(subclass, 'get_alg_prompt') and 
        callable(subclass.get_alg_prompt) or
        NotImplemented)
        
    @abc.abstractmethod
    def run(self, game_window, canvas):
        """Wrapper method to run algorithm"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_alg_prompt(self):
        """This method returns prompt to be desiplayed just below header.
        It contains name of the algorithm and brief info about it:
        weighted/unweighted and if it guearantees shortest path"""
        raise NotImplementedError
