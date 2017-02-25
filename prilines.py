

def find_and_print_lines(opened_file, numb_id):
    """
    Function from this module print first line of file which contains number id
    'numb_id' and 100 lines after and before if it possible. If number id
    doesn't presented in this file, function prints message about it.
    """
    # list with lines before line with numb_id
    prev_lines = []
    # variable for control of printing 100 lines after, also flag
    ln = 0
    # finding of line with numb_id and making list of previous lines
    for line in opened_file:
        if numb_id in line:
            print("\n" + line)
            ln = 100
            break
        prev_lines.append(line)
    # return if there is no line with numb_id in this file
    if ln == 0:
        print("No line with number id '%s' in opened file" % numb_id)
        return 0
    # print of 100 lines after line with numb_id
    for line in opened_file:
        if ln < 1:
            break
        print(line, end="")
        ln -= 1
    # print for beauty output
    print("")
    # print of 100 lines before line with numb_id
    if len(prev_lines) < 100:
        for pr_line in prev_lines:
            print(pr_line, end="")
    else:
        for i in reversed(range(100)):
            print(prev_lines[-1 - i], end="")
    return 1
