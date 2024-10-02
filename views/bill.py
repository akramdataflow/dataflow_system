import streamlit as st
from datetime import datetime
import pandas as pd
import os

data_path = r'C:\Users\rf\Desktop\dataflow\dataflow_system\dataflow_system\data\coustumer data.csv'

def get_last_order_number(data_path):
    try:
        if not os.path.exists(data_path):
            # Create the CSV file with the appropriate headers if it doesn't exist
            headers = [
                'order number', 'costumer name', 'dis', "Customer's field of work",
                'price', 'Creation time', 'order type', 'bill type', 
                'Completion time', 'payment method', 'discount', 
                'amount received', 'remaining amount'
            ]
            pd.DataFrame(columns=headers).to_csv(data_path, index=False, encoding='utf-8-sig')
            return 0
        
        df = pd.read_csv(data_path)
        if 'order number' in df.columns:
            if not df.empty:
                return df['order number'].max()
        return 0
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return 0

def save_to_csv(order_number, name, Domain, Description, Request_type, Duration_of_completion, Payment_type, price, discount, bill_type, amount_received, remaining_amount):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # إنشاء DataFrame جديد مع البيانات
    df = pd.DataFrame([{
        'order number': order_number,
        'costumer name': name,
        'dis': Description,
        "Customer's field of work": Domain,
        'price': price,
        'Creation time': current_time,
        'order type': Request_type,
        'bill type': bill_type,
        'Completion time': Duration_of_completion,
        'payment method': Payment_type,
        'discount': discount,
        'amount received': amount_received,
        'remaining amount': remaining_amount
    }])

    # حفظ البيانات في CSV، مع تعيين order number كفهرس
    df.set_index('order number', inplace=True)
    df.to_csv(data_path, index=True, mode='a', header=False, encoding='utf-8-sig')

# احصل على رقم الطلب الحالي وزيادته
current_order_number = get_last_order_number(data_path)
order_number = current_order_number + 1

st.set_page_config(page_title='Dataflow', layout='wide')
st.title('Customers Bill')

col1, col2 = st.columns(2)

with col1:
    name = st.text_input('Name')

with col2:
    Domain = st.text_input('Domain')

Description = st.text_area('Description')

Request_type = st.text_area('Request type')

Duration_of_completion = st.date_input('Duration of completion')

Payment_type = st.selectbox('Payment type', ['Direct payment', 'Installment'])

price = st.number_input('Price', min_value=0, step=1000)

discount = st.number_input('Discount', min_value=0, step=1)

# إضافة التسمية الصحيحة للمبلغ المستلم
amount_received = st.number_input('Amount received', min_value=0, step=100)

# حساب المبلغ المتبقي
remaining_amount = price - amount_received - discount

bill_type = st.selectbox('Bill type', ['Invoice', 'Receipt'])

# عند النقر على زر الإرسال
submet = st.button('Submit')

if submet:
    # حفظ البيانات المجمعة في ملف CSV
    save_to_csv(order_number, name, Domain, Description, Request_type, Duration_of_completion, Payment_type, price, discount, bill_type, amount_received, remaining_amount)
    st.success('Order saved successfully!')
