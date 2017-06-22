"""
Sriharsha Samala
"""

import os.path
import textract

ROOT = './SampleText'
"""
root folder holding documents
"""

class TextMiner(object):
    """
    text miner for various document formats
    """
    def __init__(self):
        self = self

    def read_document(self, filename):
        """
        reading a .pdf, .txt, .doc, .docx files
        -----------------------------------------
        to read .doc files on a Unix system, antiword must be installed
        Ubuntu: sudo apt-get install antiword
        """
        if not os.path.exists(filename):
            print "file does not exist"
            return ""
        
        extracted_text = ""
        try:
            extracted_text = textract.process(filename)
        except Exception:
            print "File not valid document: " + filename
            os.remove(filename)
        return extracted_text


def test():
    """
    test TextMiner functions
    """
    miner = TextMiner()

    test_file = "sample.doc"

    print miner.read_document(ROOT + '/' + test_file)

