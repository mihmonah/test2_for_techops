import paramiko
import prilines


def find_log_print_info(host, mask, log, pas, id):
    """
    Function from this module connects to server using paramiko
    SSHclient, opens log file and prints required
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=log, password=pas)
    sftp_client = client.open_sftp()
    try:
        remote_file = sftp_client.open(mask)
        prilines.find_and_print_lines(remote_file, id)
    except:
        print("Cann't open file with mask '%s'" % mask)
    finally:
        remote_file.close()
        client.close()
