import os
import zipfile
import glob
import pandas as pd


def extract_file(compress_file: str, output_directory: str) -> None:
    """
    descomprimir archivo
        parametros:
            compress_file: ruta del archivo .zip para descomprimir
            output directory: directorio para alojar el archivo descomprimido
        return:
            None
    """
    if not os.path.exists(compress_file):
        raise Exception("No existe el archivo")

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    with zipfile.ZipFile(compress_file, mode="r") as file_zip:
        file_zip.extractall(output_directory)


def get_list_data(files):
    list_data = []

    for file_ in files:

        with open(file_, "r") as doc:
            doc_data = doc.readline()
        folder = file_.split("\\")[1]
        list_data.append([doc_data, folder])

    return list_data


def save(data, name_file, path=None):
    """
    Saves the given data to a CSV file.

    Parameters:
    - data: The data to be saved.
    - name_file: The name of the CSV file.
    - path: Optional. The path where the file will be saved. If not provided, the file will be saved in the current directory.

    Returns:
    None
    """
    if path:
        if not os.path.exists(path):
            os.mkdir(path)
            name_file = os.path.join(path, name_file)
    data.to_csv(name_file, index=False)


def main():
    extract_file("data.zip", "data")

    pattern_test = "data/test/*/*.txt"
    pattern_train = "data/train/*/*.txt"

    files_test = glob.glob(pattern_test)
    files_train = glob.glob(pattern_train)

    data_test = get_list_data(files_test)
    data_train = get_list_data(files_train)

    columns = ["phrase", "sentiment"]
    df_test = pd.DataFrame(data_test, columns=columns)
    df_train = pd.DataFrame(data_train, columns=columns)
    save(df_test, "test_dataset.csv")
    save(df_train, "train_dataset.csv")


if __name__ == "__main__":
    main()
