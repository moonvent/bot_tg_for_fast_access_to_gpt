import re


def __decorate_in_code(text: str) -> str:
    result = text

    for code_element in re.finditer('```((?!```).)*```', text, flags=re.DOTALL):

        old_code_element = code_element.group()
        new_code_element = old_code_element
        new_code_element = new_code_element[3:-3]

        code_language_title = new_code_element[:new_code_element.find('\n')]

        new_code_element = new_code_element[new_code_element.find('\n'):]
        new_code_element = '<code>' + new_code_element + '</code>'

        new_code = '<b>[' + code_language_title + ']</b>' + '\n' + new_code_element

        result = result.replace(old_code_element, new_code)
        
    return result


def prepare_text_to_output_in_tg(text: str) -> str:
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    text = __decorate_in_code(text)
    return text
