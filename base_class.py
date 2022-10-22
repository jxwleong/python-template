# Base class for all templates
import logging

class TemplateBaseClass:
    def __init__(self, logger=None):
        self.logger = logging.getLogger(__name__)
        self.log = self.logger.log  # Renaming the function for 'cleaner' call
