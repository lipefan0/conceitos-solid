# pdf, txt, excel

from abc import ABC, abstractmethod

class Documents(ABC): # generic class
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass

class DocumentPDF(ABC): # isp
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentsTXT(ABC): # isp
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentsExcel(ABC): # isp
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass