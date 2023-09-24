import statistics

stocks = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}
def print_all():
    for key in stocks:
        avg=statistics.mean(stocks[key])
        avg=round(avg,2)
        print(f"{key}==>{stocks[key]}==> avg: {avg}")

def add():
    s=input("Write down the stock ticker.")
    p=input("Write down the stock price.")
    if s in stocks:
        stocks[s].append(p)
        print(stocks)
    else:
        stocks[s]=[p]
        print(stocks)

def main():
    a=input("Write down the value of operation:")
    if a=="print":
        print_all()
    else:
        add()
main()







