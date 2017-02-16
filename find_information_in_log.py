import paramiko
import sys


def auth_data(server_ip):
    ...
    return loginpass  # in format 'login/password'


def get_log_data_from_server(hname, log_mask):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hname, username=auth_data(hname).split('/')[0], password=auth_data(hname).split('/')[1])
    try:
        stdin, stdout, stderr = client.exec_command("cat %s" % log_mask)
    except Exception as e:
        print("Can't find log file with input mask", format(e))
    result = stdout.read().readlines()
    client.close()
    return result


def find_str_number(input_str, data_str):
    j = 0
    str_numb = -1
    while j < len(data_str):
        if input_str in data_str[j]:
            str_numb = j
            break
        j = j + 1
    return str_numb


def print_100_str_before_after(string_number, data_string):
    a = 0
    b = len(data_string) - 1
    i = string_number
    if string_number - 100 > 0:
        a = string_number - 100
    if string_number + 100 < len(data_string):
        b = string_number + 100
    while i < b:
        print(data_string[i], end="")
        i = i + 1
    print('\n')
    i = string_number
    while a < i:
        print(data_string[a], end="")
        a = a + 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 4:
        host = sys.argv[1]
        mask = sys.argv[2]
        numb_id = sys.argv[3]
        if find_str_number(get_log_data_from_server(host, mask), numb_id) != -1:
            print(get_log_data_from_server(host, mask)[find_str_number(get_log_data_from_server(host, mask), numb_id)])
            print_100_str_before_after(find_str_number(get_log_data_from_server(host, mask), numb_id),
                                       get_log_data_from_server(host, mask))
        else:
            print("Can not find %s in log file" % numb_id)
    else:
        print("Wrong number of arguments! Please put your arguments in format: ip log_mask number_id")
