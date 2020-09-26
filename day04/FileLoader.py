import pandas as pd 


class FileLoader(object):
    def load(self, path):
        try:
            data = pd.read_csv(path)
        except:
            raise FileNotFoundError("file not found")
        print("Loading dataset of dimensions {} x {}".format(data.shape[0],data.shape[1]))
        return data 
    def display(self, df, n):
        print(df.head(n))

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("./housing.csv")
    # print(data)
    loader.display(data,10)
    # data.head(10)
    # print(data)
