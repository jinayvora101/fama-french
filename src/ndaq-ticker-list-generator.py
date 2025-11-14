from pandas import read_csv, to_datetime, notna

class NDAQ_Ticker_List:

    def __init__(self) -> None:
        self.changes = read_csv(r".\fama-french\dump\ndaq-ticker-change.csv", parse_dates=["Date"], date_format="%d/%m/%Y")
    
    def get_list(self, xdate):
        tickers = read_csv(r".\fama-french\dump\ndaq-ticker-list-20251101.csv")["Tickers"].to_list()

        for idx, (dt, add, rem) in self.changes.iterrows():
            try:
                if dt < xdate: break
                if notna(add): tickers.remove(add)
                if notna(rem): tickers.append(rem)
            except Exception as e:
                print(dt, add, e)

        return tickers


a = NDAQ_Ticker_List()

b = a.get_list(to_datetime("2025-11-01", format="%Y-%m-%d"))
c = len(b)
print(c)

d = a.get_list(to_datetime("2000-01-01", format="%Y-%m-%d"))
e = len(d)
print(e)