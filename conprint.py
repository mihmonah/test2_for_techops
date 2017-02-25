import paramiko
import prilines


def find_log_print_info(host, mask, log, pas, id):
    """
    Function from this module connects to server using paramiko
    SSHclient, opens log file and prints required
    """
    # create paramiko SSH client
    client = paramiko.SSHClient()
    # add server key to known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # connect to server by ip, login and password
    client.connect(host, username=log, password=pas)
    # open an SFTP session on the SSH server
    sftp_client = client.open_sftp()
    try:
        # open masked file in read mode
        remote_file = sftp_client.open(mask)
        prilines.find_and_print_lines(remote_file, id)
    except:
        print("Cann't open file with mask '%s'" % mask)
    finally:
        remote_file.close()
        client.close()
