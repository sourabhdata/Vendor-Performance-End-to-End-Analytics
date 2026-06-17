import pandas as pd 
import sqlite3
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
    Select 
        VendorNumber,
        Sum(Freight) As FreightCost
    From vendor_invoice
    group by VendorNumber
),
    PurchaseSummary As (
        Select 
            p.VendorName,
            p.VendorNumber,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            p1.Price as ActualPrice,
            p1.Volume,
            Sum(p.Quantity) as TotalPurchaseQuantity,
            sum(p.Dollars) as TotalPurchaseDollars
            From Purchases p join purchase_prices p1
                on p.Brand=p1.Brand
            where p.PurchasePrice>0
            Group By p.vendornumber,p.vendorname,p.Brand,p.Description,p.PurchasePrice,p1.Price,p1.Volume
    ),
    SalesSummary As (
        Select 
            VendorNo,
            Brand,
            Sum(SalesQuantity) as TotalSalesQuantity,
            Sum(SalesDollars) as TotalSalesDollars,
            Sum(SalesPrice) As TotalSalesPrice,
            Sum(ExciseTax) as TotalExciseTax from sales 
            group by VendorNo,Brand 
    )
    Select 
        ps.VendorName,
        ps.VendorNumber,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    Left join SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand=ss.Brand
    Left Join FreightSummary fs 
        On ps.VendorNumber=fs.VendorNumber
    Order By ps.TotalPurchaseDollars DESC""",conn)
    return vendor_sales_summary


def clean_data(df):
    '''this function wil clean the data'''
    df['Volume'] = df['Volume'].astype('float')
    df.fillna(0,inplace=True)
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    
    summary_df['GrossProfit'] = summary_df['TotalSalesDollars'] - summary_df['TotalPurchaseDollars'] 
    summary_df['ProfitMargin'] = summary_df['GrossProfit']/summary_df['TotalSalesDollars']*100 
    summary_df['StockTurnover'] = summary_df['TotalSalesQuantity']/summary_df['TotalPurchaseQuantity'] 
    summary_df['SalestoPurchaseRatio'] = summary_df['TotalSalesDollars']/summary_df['TotalPurchaseDollars']
    
    return df


if __name__ == '__main__':
    conn=sqlite3.connect('inventory.db')

    logging.info('Creating Vendor  Summary Table.....')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting Data.....')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')
       