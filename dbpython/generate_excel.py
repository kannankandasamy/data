import snowflake.connector
import openpyxl
import os
from datetime import datetime
import pandas as pd

class Executor:
    def __init__(self, acc_user, acc_pwd, account, role=None, wh=None, db=None, sch=None):
        self.acc_user = acc_user
        self.acc_pwd = acc_pwd
        self.account = account
        self.role = role
        self.warehouse = wh
        self.database = db
        self.schema = sch

    def connect(self):
        conn = snowflake.connector.connect(
            user = self.acc_user,
            password = self.acc_pwd,
            account = self.account,
            role = self.role,
            WAREHOUSE = self.warehouse,
            DATABASE = self.database,
            SCHEMA = self.schema
        )
        return conn

    def gen_excel(self, filename, fmt_col, df):
        writer = pd.ExcelWriter(filename, engine="xlsxwriter")
        df.to_excel(writer, sheet_name = "testSheet1", index=False, freeze_panes=(1,0))
        workbook = writer.book
        worksheet = writer.sheets["testSheet1"]
        (max_row, max_col) = df.shape
        worksheet.autofilter(0,0,max_row,max_col-1)
        format1 = workbook.add_format({"num_format":"#,##0.00"})
        worksheet.set_column(fmt_col,fmt_col,None, format1)
        for i, col in enumerate(df.columns):
            column_len = df[col].astype(str).str.len().max()
            column_len = max(column_len, len(col)) +2
            worksheet.set_column(i,i,column_len)
        writer.save()

if __name__ == "__main__":
    query_date = "2023-08-23"
    base_path = r"C:\Kannan\Guvi"
    date_path = base_path + datetime.today().strftime(r"\%Y\%m\%d")
    file_date = datetime.today().strftime("%Y-%m-%d")

    try:
        os.makedirs(date_path, exist_ok = True)
        print(date_path)
    except OSError as error:
        print(error)

    exe = Executor(
            acc_user = "*****",
            acc_pwd = "*****",
            account = "*****",
            role = "DEV_ROLE",
            wh = "SMALL_ELT_WH",
            db = "SALES_DWH",
            sch = "SALES_SCHEMA"         
        )
    con = exe.connect()
    print(con)
    cur = con.cursor()

    query_txt = """select * from sales_dwh.sales_schema.dim_customer;"""
    query_op = cur.execute(query_txt.format(query_date))
    out_df1 = query_op.fetch_pandas_all()
    #out_df1['AMOUNT'] = out_df1['AMOUNT'].astype(float)
    f_name = date_path + "\\"+ file_date + ".xlsx"
    exe.gen_excel(f_name,8, out_df1)
    print(f_name)


