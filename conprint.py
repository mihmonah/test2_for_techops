import paramiko
import prilines

# Function from this module connects to server using paramiko SSHclient, opens log file and 
# prints required 

def find_log_print_info(host, mask, log, pas, id):
    client = paramiko.SSHClient()                                   # create paramiko SSH client
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # add server key to known hosts
    client.connect(hname, username=log, password=pas)               # connect to server by ip, login and password
    sftp_client = client.open_sftp()                                # open an SFTP session on the SSH server
    try:
        remote_file = sftp_client.open(mask)                        # open masked file in read mode
        prilines.find_and_print_lines(remote_file,id)
    except:
        print("Cann't open file with mask '%s'" % mask)    
    finally:
        remote_file.close()
        client.close()