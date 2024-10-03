import pandas as pd

# # مسار الملف
# data_path = r'C:\Users\rf\Desktop\dataflow\dataflow_system\dataflow_system\data\coustumer data.csv'

# # قراءة البيانات
# df = pd.read_csv(data_path)

# # تحقق مما إذا كان DataFrame يحتوي على أي صفوف
# if not df.empty:
#     # حذف السطر الأول فقط إذا كان موجودًا
#     if 0 in df.index:
#         df = df.drop(index=0)
#     else:
#         print("السطر الأول غير موجود.")

#     # إعادة تعيين الفهارس
#     df.reset_index(drop=True, inplace=True)

#     # حفظ الملف بعد حذف السطر الأول
#     df.to_csv(data_path, index=False, encoding='utf-8-sig')
#     print("تم حذف السطر الأول بنجاح.")
# else:
#     print("DataFrame فارغ، لا يوجد صفوف لحذفها.")

data_path = r'C:\Users\rf\Desktop\dataflow\dataflow_system\dataflow_system\data\incume data.csv'

headers = ['name', 'domain', 'amount_received', 'discount', 'creation_time', 'price']
pd.DataFrame(columns=headers).to_csv(data_path, index=False, encoding='utf-8-sig')