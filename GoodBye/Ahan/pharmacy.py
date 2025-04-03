import streamlit as st
import pandas as pd
import os


STOCK_FILE = "medicine_stock.csv"
BILLING_FILE = "billing_records.csv"


def load_stock():
    if os.path.exists(STOCK_FILE):
        return pd.read_csv(STOCK_FILE)
    else:
        return pd.DataFrame(columns=["Medicine", "Price", "Quantity", "Purchase Price", "Stock Date"])



def save_stock(df):
    df.to_csv(STOCK_FILE, index=False)


def load_billing():
    if os.path.exists(BILLING_FILE):
        return pd.read_csv(BILLING_FILE)
    else:
        return pd.DataFrame(columns=["Medicine", "Quantity", "Total Price", "Buyer Email", "Date"])


def save_billing(df):
    df.to_csv(BILLING_FILE, index=False)


stock_df = load_stock()
billing_df = load_billing()

st.title("💊 Pharmacy Management")


st.subheader("📦 Medicine Stock Management")


st.write("### ➕ Add New Medicine")
medicine_name = st.text_input("Medicine Name", key="medicine_name")
price = st.number_input("Selling Price (BDT)", min_value=0, step=1, key="price")
purchase_price = st.number_input("Purchase Price (BDT)", min_value=0, step=1, key="purchase_price")
quantity = st.number_input("Quantity", min_value=0, step=1, key="quantity")
stock_date = st.date_input("Stock Date", key="stock_date")

if st.button("Add Medicine", key="add_medicine"):
    new_data = pd.DataFrame([[medicine_name, price, quantity, purchase_price, stock_date]], 
                            columns=["Medicine", "Price", "Quantity", "Purchase Price", "Stock Date"])
    stock_df = pd.concat([stock_df, new_data], ignore_index=True)
    save_stock(stock_df)
    st.success("Medicine added successfully!")


st.write("### 📤 Upload CSV for Bulk Stock Entry")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"], key="upload_csv")
if uploaded_file:
    new_data = pd.read_csv(uploaded_file)
    stock_df = pd.concat([stock_df, new_data], ignore_index=True)
    save_stock(stock_df)
    st.success("CSV Data Added Successfully!")


st.write("### 🔍 Search Stock")
search_query = st.text_input("Search Medicine Name:", key="search_stock")
filtered_stock = stock_df[stock_df["Medicine"].str.contains(search_query, case=False, na=False)] if search_query else stock_df
st.dataframe(filtered_stock)


st.download_button("📥 Download Stock CSV", stock_df.to_csv(index=False), file_name="medicine_stock.csv", mime="text/csv", key="download_stock")


st.subheader("🧾 Billing System")

buyer_email = st.text_input("Buyer Email", key="buyer_email")
bill_medicine_name = st.text_input("Medicine Name", key="bill_medicine_name")
bill_quantity = st.number_input("Quantity", min_value=1, step=1, key="bill_quantity")

if st.button("Calculate Price", key="calculate_price"):
    if bill_medicine_name in stock_df["Medicine"].values:
        selected_medicine = stock_df[stock_df["Medicine"] == bill_medicine_name].iloc[0]
        total_price = selected_medicine["Price"] * bill_quantity
        
        
        st.success(f"Total Price: {total_price} BDT")
        
        
        updated_stock_df = stock_df.copy()
        updated_stock_df.loc[updated_stock_df["Medicine"] == bill_medicine_name, "Quantity"] -= bill_quantity
        save_stock(updated_stock_df)

        
        new_billing_data = pd.DataFrame([[bill_medicine_name, bill_quantity, total_price, buyer_email, pd.Timestamp.now()]], 
                                        columns=["Medicine", "Quantity", "Total Price", "Buyer Email", "Date"])
        billing_df = pd.concat([billing_df, new_billing_data], ignore_index=True)
        save_billing(billing_df)

        
        st.write("🛒 Sending receipt to buyer's email... (Not implemented here)")

    else:
        st.error("Medicine not found in stock!")


st.download_button("📥 Download Billing CSV", billing_df.to_csv(index=False), file_name="billing_records.csv", mime="text/csv", key="download_billing")

st.success("✔️ Billing and Stock Management Updated Successfully!")

st.write("Please wait for the final version.")

st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Medical%20Assistant/LICENSE).")      # LICENSE AND OWENERSHIP