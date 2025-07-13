import streamlit as st 
import requests

def currenc_finder(ammount,base="USD",fc):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    
    price = data["rates"]["fC"]
    print(price * ammount)
    
def main():
    a = int(input("enter the amount :"))
    b = input("enter the base:")
    fc = input("enter the initial currency :")
    currenc_finder(a,b,fc)
    
if __name__ == "__main__":
    main()