def showSection(index: int,  json_data: list) -> None:
    for item in json_data[index]['Messages']:
        print(item['dates'])
        print(rf"{item['message']}", '\n')


def removeTitleSpecialParts(string: str) -> str:
    special_parts = ['\n', '*', '_', ':']

    for part in special_parts:
        string = string.replace(part, '')

    return string
