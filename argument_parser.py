# Template class for argument parser
import argparse
from ast import arg
import logging

from base_class import TemplateBaseClass


class ArgumentParserTemplate(TemplateBaseClass):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser()
        
    def setup_argument(self):
        pass
    
    def parse_argument(self):
        pass 
