import requests
import streamlit as st

def currency_finder():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    rates = response.json()
    
    price = rates["rates"]["INR"]
    print("💵 1 US Dollar = ₹", price)    
    
    # if rates["success"] and "rates" in rates:
    #     price = rates["rates"]["INR"]
    #     print("one doller is :", price)
    # else:
    #     print("error in the fatching of data")
    
    # if "rates" in rates and "INR" in rates["rates"]:
    #     price = rates["rates"]["INR"]
    #     st.success(f"💵 1 US Dollar = ₹{price}")
    # else:
    #     st.error("❌ Error in fetching the currency data.")

# Run the function
currency_finder()
