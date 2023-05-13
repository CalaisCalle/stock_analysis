'''Main: Analyses some stocks or something idk'''
from alpha_vantage import base

def main():
    av = base.alpha_vantage_base()
    r = av.time_series("IBM")
    print(r.json())
    pass

if __name__=="__main__":
    main()