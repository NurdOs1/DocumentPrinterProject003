# src/document.py
from typing import List

from src.printers import PrinterStrategy


class Document:
    def __init__(self, pages: List[str]) -> None:
        self.pages = pages

    def print_document(self, printer: PrinterStrategy) -> None:
        for page in self.pages:
            printer.print_page(page)
