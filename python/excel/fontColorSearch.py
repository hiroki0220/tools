import os
from openpyxl import load_workbook
from openpyxl.styles import Font

# 処理するフォルダのパス
folder_path = "work"

# フォントが赤字になっているセルを検索する関数
def search_red_font_cells(file_path):
    # ワークブックを開く
    wb = load_workbook(filename=file_path)
    # アクティブなシートを取得する
    sheet = wb.active
    # 赤字のフォントを持つセルを探す
    red_font = Font(color="FF0000")
    for row in sheet.rows:
        for cell in row:
            if cell.font == red_font:
                print(f"Red font found in {file_path}: {cell.coordinate} = {cell.value}")

# フォルダ内のExcelファイルを処理する
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 拡張子が xlsx のファイルのみを処理する
        if file.endswith(".xlsx"):
            file_path = os.path.join(root, file)
            search_red_font_cells(file_path)
