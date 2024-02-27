class FakerHandler:
    def __init__(self):
        pass

    def readCSV(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return f.readlines()
        except FileNotFoundError as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return None
        except Exception as e:
            return e
    
    def readCSVGenerator(self, file_path):
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    yield line
        except FileNotFoundError as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return None
        except Exception as e:
            return e