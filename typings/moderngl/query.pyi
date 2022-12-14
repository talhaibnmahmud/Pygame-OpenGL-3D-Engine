"""
This type stub file was generated by pyright.
"""

__all__ = ['Query']
class Query:
    '''
        This class represents a Query object.
    '''
    __slots__ = ...
    def __init__(self) -> None:
        ...
    
    def __repr__(self): # -> Literal['<Query>']:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __enter__(self): # -> Self@Query:
        ...
    
    def __exit__(self, *args): # -> None:
        ...
    
    @property
    def samples(self) -> int:
        '''
            int: The number of samples passed.
        '''
        ...
    
    @property
    def primitives(self) -> int:
        '''
            int: The number of primitives generated.
        '''
        ...
    
    @property
    def elapsed(self) -> int:
        '''
            int: The time elapsed in nanoseconds.
        '''
        ...
    


