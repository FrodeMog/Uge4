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
        
    def getNameData(self, file_path, name):
        try:
            lines_with_name = []
            with open(file_path, 'r') as f:
                for line in f:
                    if name in line:
                        lines_with_name.append(line)
            return lines_with_name
        except FileNotFoundError as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return None
        except Exception as e:
            return e

    def getNameDataGenerator(self, file_path, name):
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    if name in line:
                        yield line
        except FileNotFoundError as e:
            print(f"Error reading CSV file {file_path}: {e}")
            return None
        except Exception as e:
            return e