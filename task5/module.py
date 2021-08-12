def categorias(letters: list) -> list:
    """Convert the list into a dict and then into a list.

    Args:
        letters (list): List of random letters

    Returns:
        list: 'Letters' without duplicates elements
    """
    letters = list(dict.fromkeys(letters))

    return letters


def mefaltandelacategoria(list_1: list, list_2: list, string: str) -> list:
    """Analize the first and the last list, then returns a valid position.

    Args:
        list_1 (list): List of Index
        list_2 (list): List of letters
        string (str): The main letter

    Returns:
        list: The position where the list_3 is in list_2
    """

    final_list = []

    for i in range(len(list_1)):
        if list_2[list_1[i]] == string:
            final_list.append(list_1[i])

    return final_list


def notengopacientes(list_1: list, list_2: list) -> list:
    """Returns values of the first list that aren't in the second list.

    Args:
        list_1 (list): First list of integers
        list_2 (list): Second list of integers

    Returns:
        list: Values of the first list that aren't in the second list
    """
    final_list = []

    for i in list_1:
        if i not in list_2:
            final_list.append(i)

    return final_list


def puedecambiar(list_1: list, list_2: list) -> int:
    """Returns the lower number of the possible changes between both lists.

    Args:
        list_1 (list): First list of letters
        list_2 (list): Second list of letters

    Returns:
        list: Lower number of the possible changes between both lists
    """

    counter_1 = 0
    counter_2 = 0

    for i in list_1:
        if i not in list_2:
            counter_1 += 1

    for y in list_2:
        if y not in list_1:
            counter_2 += 1

    if counter_1 > counter_2:
        return counter_2
    else:
        return counter_1
