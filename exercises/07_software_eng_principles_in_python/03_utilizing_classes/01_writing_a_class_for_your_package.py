# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of Document
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text
