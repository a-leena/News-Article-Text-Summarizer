import pandas

def load_dataset(file_path, encoding_standard):
    data_file = pandas.read_csv(filepath_or_buffer=file_path, encoding=encoding_standard)

    base_text = data_file["base_text"].tolist()
    summary_text = data_file["summary_text"].tolist()

    return (base_text,summary_text)


def clean_dataset(text_set):
    pass