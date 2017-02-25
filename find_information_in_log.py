import sys
import autorize
import conprint


if __name__ == "__main__":
    if len(sys.argv) == 4:
        host = sys.argv[1]
        mask = sys.argv[2]
        numb_id = sys.argv[3]
        login = autorize.auth_data(host).split('/')[0]
        pas = autorize.auth_data(host).split('/')[1]
        conprint.find_log_print_info(host, mask, login, pas, numb_id)
    else:
        print("Wrong number of arguments! Dataformat: ip log_mask numid")
