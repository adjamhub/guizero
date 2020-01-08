=============
Installazione
=============

La libreria guizero è stata progettata per permettere a chi la studia di imparare a creare velocemente delle GUI per i propri programmi.

Ci sono tre possibili opzioni per l'installazione:

#. il download del codice dal repository dove viene sviluppato

#. l'installazione tramite **python pip**

#. (solo Windows) l'installazione tramite pacchetto MSI installer


Il metodo con pip presenta numerosi vantaggi:


Installazione tramite Python pip
================================

You can use the command prompt and `pip` to install guizero for:

+ [Windows](#windows)
+ [macOS](#macos)
+ [Raspberry Pi](#raspberry-pi)
+ [Linux](#linux)

`pip` can also be used to [install additional features](#additional-features-install) and [upgrade guizero](#upgrading).


Windows
-------

1. Open a command prompt by clicking **Start** > **Windows System** > **Command Prompt**, or by typing 'command' into the start menu's search bar.

    .. image:: images/windows_command_prompt_app.png

2. Type this command and press enter:

    .. code:: bash

        $ pip3 install guizero

    .. image:: images/windows_pip_install.gif


If you experience problems, have a look at this guide to [_Using pip on Windows_](https://projects.raspberrypi.org/en/projects/using-pip-on-windows).


macOS
-----

1. Open a terminal window by clicking **Applications** > **Utilities** > **Terminal**, or by typing 'terminal' into the desktop's search bar.

   .. image:: images/mac-terminal.png

2. Type this command and press enter:

    .. code:: bash
        
        $ pip3 install guizero

   .. image:: images/mac_pip_install.gif


Linux
-----

1. Open a terminal
2. Install `tkinter` using your distribution's package manager, e.g. `sudo apt install python3-tk`
3. Install guizero using pip by typing `pip3 install guizero` or `sudo pip3 install guizero` if you don't have superuser rights

   .. image:: images/linux_pip_install.gif

**Note:** If you are using Debian, you alternatively have the option to install guizero via apt
`sudo apt-get install python-guizero`



### Install additional features

To use the additional [image features](images.md) of guizero such as:

- JPG image support
- scaling images
- animated gifs

... you will need to install guizero with the pip command:

- Windows / macOS

    .. code:: bash
        
        $ pip install guizero[images]

- Linux / Raspberry Pi

    .. code:: bash
        
        $ sudo pip install guizero[images]

The additional image features are not available to install using the easy install method.

