from Files_SSH import Files_SSH

if __name__ == "__main__":
    from argparse import ArgumentParser

    usage = 'usage:python Simple_SSH_Client.py -i ipddr -u username -p password -c command'

    parser = ArgumentParser(usage=usage)
    parser.add_argument('-i','--ipaddr',dest='ipaddr',help='SSH Server',default='172.30.13.1',type=str)
    parser.add_argument('-u', '--username', dest='username', help='SSH Username', default='admin', type=str)
    parser.add_argument('-p', '--password', dest='password', help='SSH Password', default='asiafort@ro', type=str)
    parser.add_argument('-c', '--command', dest='command', help='Shell Command', default='ip address print', type=str)

    args = parser.parse_args()
    print(Files_SSH(args.ipadd, args.username, args.password, cmd=args.command))

