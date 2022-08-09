from google.cloud import translate
import csv
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./apikeys.json'
# GOOGLE_APPLICATION_CREDENTIALS = ""

def listToString(s):
    """ Transform list to string"""
    str1 = " "
    return (str1.join(s))

def detect_language(project_id,content):
    """Detecting the language of a text string."""

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.detect_language(
        content=content,
        parent=parent,
        mime_type="text/plain",  # mime types: text/plain, text/html
    )

    for language in response.languages:
        return language.language_code


def translate_text(text, project_id,source_lang):
    """Translating Text."""

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_lang,
            "target_language_code": "pa",
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))
        
def main():
    project_id="engg-hiring"
    csv_files = ["q.csv"]
    # Perform your content extraction here if you have a different file format #
    for csv_file in csv_files:
        csv_file = open(csv_file)
        read_csv = csv.reader(csv_file)
        content_csv = []

        for row in read_csv:
            content_csv.extend(row)
        content = listToString(content_csv) # convert list to string
        detect = detect_language(project_id=project_id,content=content)
        translate_text(text=content,project_id=project_id,source_lang=detect)

if __name__ == "__main__":
    main()
