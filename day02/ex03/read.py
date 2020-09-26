from csvreader import CsvReader
if __name__== "__main__":
    withCsvReader('good.csv') as file:
    data= file.getdata()
    header= file.getheader()
