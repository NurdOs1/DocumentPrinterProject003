# src/printers.py
from abc import ABC, abstractmethod

class PrinterStrategy(ABC):
    @abstractmethod
    def print_page(self, page: str) -> None:
        pass
# src/printers.py
class InkjetPrinter(PrinterStrategy):
    def print_page(self, page: str) -> None:
        print(f"Напечатать страницу на струйном принтере: {page}")

class LaserPrinter(PrinterStrategy):
    def print_page(self, page: str) -> None:
        print(f"Напечатать страницу на лазерном принтере: {page}")
