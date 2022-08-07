import pandas
import re

def load_dataset(file_path, encoding_standard):
    data_file = pandas.read_csv(filepath_or_buffer=file_path, encoding=encoding_standard)

    base_text = data_file["base_text"].tolist()
    summary_text = data_file["summary_text"].tolist()

    return (base_text,summary_text)


def clean_dataset(text_set):
    returning_set = []
    for i in range(len(text_set)):
        temp_string = text_set[i]
        
        #remove escape characters from the text
        temp_string = re.sub("(\\t)", ' ', str(temp_string)).lower()
        temp_string = re.sub("(\\r)", ' ', str(temp_string)).lower()
        temp_string = re.sub("(\\n)", ' ', str(temp_string)).lower()

        #remove underscore if it occurs more than once in a row
        temp_string = re.sub("(__+)", ' ', str(temp_string)).lower()

        #remove hyphen if it occurs more than once in a row
        temp_string = re.sub("(--+)", ' ', str(temp_string)).lower()

        #remove tilde symbol if it occurs more than once in a row
        temp_string = re.sub("(~~+)", ' ', str(temp_string)).lower()

        #remove the plus symbol if it occurs more than once in a row
        temp_string = re.sub("(\+\++)", ' ', str(temp_string)).lower()

        #remove period if it occurs more than once in a row
        temp_string = re.sub("(\.\.+)", ' ', str(temp_string)).lower()

        #remove special characters: <>()|&©ø"',;?~*!
        temp_string = re.sub(r"[<>()|&©ø\[\]\'\",;?~*!]", ' ', str(temp_string)).lower()

        #remove mailto attribute from the scraped HTML page
        temp_string = re.sub('(mailto:)', ' ', str(temp_string)).lower()

        #remove \x9*
        temp_string = re.sub(r"(\\x9\d)", ' ', str(temp_string)).lower()

        #remove INC nums with the INC_NUMS constant
        temp_string = re.sub("([iI][nN][cC]\d+)", 'INC_NUM', str(temp_string)).lower()

        #remove CM# and CHG# with the CM_NUMS constant
        temp_string = re.sub("([cC][mM]\d+)|([cC][hH][gG]\d+)", 'CM_NUM', str(temp_string)).lower()

        #remove fullstops but only if they occur at the end of the words, not the ones in between words
        temp_string = re.sub("(\.\s+)", ' ', str(temp_string)).lower()

        #remove hyphens but only if they occur at the end of the words, not the ones in between words
        temp_string = re.sub("(\-\s+)", ' ', str(temp_string)).lower()

        #remove colons but only if they occur at the end of the words, not the ones in between words
        temp_string = re.sub("(\:\s+)", ' ', str(temp_string)).lower()

        #remove single characters between 2 spaces
        temp_string = re.sub("(\s+.\s+)", ' ', str(temp_string)).lower()

        #try removing https info from any url's embedded in the text
        try:
            url = re.search(r'((https*:\/*)([^\/\s]+))(.[^\s]+)', str(temp_string))
            replacement_url = url.group(3)
            temp_string = re.sub(r'((https*:\/*)([^\/\s]+))(.[^\s]+)', replacement_url, str(temp_string))
        except:
            pass #case of emails with no url in them

        #remove multiple consecutive spaces
        temp_string = re.sub("(\s+)", ' ', str(temp_string)).lower()

         #remove single characters between 2 spaces
        temp_string = re.sub("(\s+.\s+)", ' ', str(temp_string)).lower()

        #put cleaned string back into the text set
        returning_set.append(temp_string)
    
    return returning_set