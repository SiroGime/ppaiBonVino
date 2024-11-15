from abc import ABC, abstractmethod

class IIterador(ABC):
    
    @abstractmethod
    def primero(self):
        pass
    
    @abstractmethod
    def haFinalizado(self):
        pass
    
    @abstractmethod
    def actual(self):
        pass
    
    @abstractmethod
    def cumpleFiltro(self):
        pass
    
    @abstractmethod
    def siguiente(self):
        pass