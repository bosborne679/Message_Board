import cmd # implement the CLI to handle functionality
import socket
import sys
import threading


class MessageBoardInterface(cmd.Cmd):
    intro = "Welcome to the message board.\tType help or ? to list commands."
    prompt = "% "

    def __init__(self):
        super().__init__()
        self._connected = False # Boolean to tell if user is connected to a server
        self._joined = False # Boolean to tell if user has joined the message board
        # if _connected is false _joined should be false by default
        self._groups = None # List of current groups

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, connected):
        self._connected = connected

    @property
    def joined(self):
        return self._joined

    @joined.setter
    def joined(self, joined):
        self._joined = joined

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, groups):
        self._group = groups

    def groups_append(self, *args):
        for arg in args:
            self._groups.append(arg)

    # Basic functionality
    def do_connect(self, arg):
        """
NAME
    conect - connect to an available server

SYNOPSIS
    connect ADDRESS PORT

DESCRIPTION
    connect will connect to a server at ADDRESS:PORT. Will report if failed or succeeded.
        """
        pass

    def do_join(self, args):
        """
NAME
    join - join a message board

SYNOPSIS
    join

DESCRIPTION
    Joins the message board so posts can be made. Reports success or failure.
        """
        pass

    def do_post(self, args):
        """
NAME
    post - post a message to the message board

SYNOPSIS
    post "MESSAGE_SUBJECT" "MESSAGE_BODY"

DESCTIPTION
    post will post the provided MESSAGE_SUBJECT and MESSAGE_BODY to the
    the current message board.
        """
        pass

    def do_users(self, args):
        """
NAME
    user - returns a list of users

SYNOPSIS
    user

DESCRIPTION
    Returns a list of users that are in the same group.
        """
        pass

    def do_leave(self, args):
        """
NAME
    leave - leaves the current group

SYNOPSIS
    leave

DESCRIPTION
    Leaves the current group if in one. Reports success or failure.
        """
        pass

    def do_message(self, args):
        """
NAME
    message - retrieves a message

SYNOPSIS
    message MESSAGE_ID

DESCRIPTION
    Retrieves the contents of a message given a MESSAGE_ID.
        """
        pass

    def do_exit(self, args):
        """
NAME
    exit

SYNOPSIS
    exit

DESCRIPTION
    Exits from the currently connected server, but keeps the program running.
    Reports success or failure.
        """
        pass


def interface():
    interface_instance = MessageBoardInterface()
    interface_instance.cmdloop()


def server():
    pass


def main():
    # this will only start the server thread and the interface thread
    interface_thread = threading.Thread(target=interface)
    # server_thread = threading.Thread(target=server, daemon=True)
    # server_thread.start()
    interface_thread.start()


if __name__ == '__main__':
    main()
