

class CsvReader():
    def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    
    def __enter__(self):
        pass
    def __exit__(self,exc_type, exc_val, exc_tb):
        pass