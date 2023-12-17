import pandas as pd


def get_last_id_from_first_file(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')

        last_id_value = df['id'].max()

        return last_id_value + 1
    except Exception as e:
        print(f"Ошибка: {e}")

        return None


def numerate_rows_in_excel(file_path, start):
    df = pd.read_excel(file_path)
    df["id"] = range(start, start + len(df))

    df.to_excel(file_path, index=False)

    return start + len(df)
