#!/usr/bin/python
# ! encoding=utf-8

import paramiko
import unicode_utils


class SSHConnection(object):
    def __init__(self, host_dict):
        self.host = host_dict['host']
        self.port = host_dict['port']
        self.username = host_dict['username']
        self.pwd = host_dict['pwd']
        self.__transport = None

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def run_cmd(self, command):
        """
        execute Shell command and return dict
        return {'color': 'red', 'res': error} or
        return {'color': 'green', 'res': res}
        :param command:
        :return:
        """
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # command execute
        stdin, stdout, stderr = ssh.exec_command(command)
        # get the result
        res = unicode_utils.to_str(stdout.read())
        # get error info
        error = unicode_utils.to_str(stderr.read())
        # if there has error info, return error
        if error.strip():
            return {'color': 'red', 'res': error}
        else:
            return {'color': 'green', 'res': res}

    def upload(self, local_path, target_path):
        # connect
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # upload location.py to server /tmp/test.py
        sftp.put(local_path, target_path, confirm=True)
        # add privilege
        sftp.chmod(target_path, 0o755)

    def download(self, target_path, local_path):
        # connect, download
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.get(target_path, local_path)

    def __del__(self):
        self.close()


if __name__ == '__main__':
    # input the host,port,username,pwd
    ssh_connect = SSHConnection({'host': 'hostname or ip', 'port': 22, 'username': 'username', 'pwd': 'password'});
    ssh_connect.connect()
    result = ssh_connect.run_cmd('df -h')
    print(result)
    ssh_connect.close()
