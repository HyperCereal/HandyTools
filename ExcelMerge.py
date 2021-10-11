import pandas as pd
import xlsxwriter

path1 = 'a.xlsx'
path2 = 'b.xlsx'
path3 = 'c.xlsx'

combine_sheet_1 = pd.read_excel(path1,sheet_name='Sheet1')
combine_sheet_2 = pd.read_excel(path2,sheet_name='Sheet1')
combine_sheet_3 = pd.read_excel(path3,sheet_name='Sheet1')

print(combine_sheet_1)
print(combine_sheet_2)
print(combine_sheet_3)

# 首尾相接拼接进一个sheet
combined_df = pd.concat([combine_sheet_1,combine_sheet_2,combine_sheet_3],axis=0,ignore_index=True)
combined_df.to_excel('./combine_result.xlsx',index=0)

# 将读取的sheet放进一个workbook
sheets_dict = {'sheet1':combine_sheet_1,'sheet2':combine_sheet_2,'sheet3':combine_sheet_3}
output_book = pd.ExcelWriter('./combined_workbook.xlsx',engine='xlsxwriter')

for sheets in sheets_dict.keys():
    sheets_dict[sheets].to_excel(output_book,sheet_name=sheets,index=False)

output_book.save()
