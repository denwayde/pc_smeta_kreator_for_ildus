import openpyxl
from dadata import Dadata
from setenv import token, secret
import httpx
import asyncio
from test_exit_file import file_creator
# Открываем Excel файл
workbook = openpyxl.load_workbook('reestr1.xlsx')

# Создаем список для хранения сформированных строк
formatted_rows = []
dadata = Dadata(token, secret)
# result = dadata.suggest("address", req)
# Проходим по столбцам A, C, D, E, K начиная с 4 строки

sheet_names = ['194', '212', '217']
#sheet_names = ['194']
# Функция main для обработки данных
async def arr_caretor():
    formatted_rows = []
    for x in sheet_names:
        try:
            sheet = workbook[x]
            #for row in range(122, 126):
            for row in range(2, sheet.max_row + 1):
                data = []
                for column_letter in ['A', 'C', 'D', 'E', 'J', 'K']:
                    cell_value = sheet[column_letter + str(row)].value
                    street = 'ул. '
                    house = 'д. '
                    flat = 'кв. '
                    if cell_value != None:
                        if column_letter == 'C':
                            try:
                                result = dadata.suggest("address", "г. Абакан " + cell_value)
                                #print(result)
                                if result != [] or result != None:
                                    if result[0]['data']['street_with_type'] != None:
                                        cell_value = result[0]['data']['street_with_type']
                                    else:
                                        cell_value = street + cell_value[0].capitalize() + cell_value[1:].lower()
                                    print("cell111 "+str(x) + str(cell_value))
                                else:
                                    cell_value = street + cell_value[0].capitalize() + cell_value[1:].lower()
                                    print("cell222")
                                    
                            except (httpx.RemoteProtocolError, httpx.ReadTimeout, IndexError):
                                print("Ошибка при получении адреса. Поиск продолжится.")
                                print("cell333")
                                cell_value = street + cell_value[0].capitalize() + cell_value[1:].lower()     
                        elif column_letter == 'D':
                            cell_value = house + str(cell_value)
                        elif column_letter == 'E':
                            cell_value = flat + str(cell_value)
                        data.append(cell_value)
                        await asyncio.sleep(0.3)
                    else:
                        pass
                data.append(x)
                formatted_rows.append(data)
        except KeyError:
            pass
    # Закрываем Excel файл
    workbook.close()
    return formatted_rows
    



async def main():
    arr = await arr_caretor()
    await file_creator(arr)
    #print(arr)


asyncio.run(main())
