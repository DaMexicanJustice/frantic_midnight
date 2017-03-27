#Installation guide:

##Setup

We need to setup a Python environment. There are many ways, but to follow along with our example we recommend a virtual machine running ubuntu. 
The following is a step by step guide to setting up a virtual machine Python enviroment and getting everything ready.

### Necessary software
The editor most of us use is called jupyter and the way to get into that editor is by doing the following:

Get a Bash-like terminal terminal on Windows by installing Git Bash, which can be downloaded from the following link: https://git-scm.com/downloads.
`git clone https://github.com/HelgeCPH/get_things_done_with_python` will cloneinto a new folder, which you do by opening git bash on the selected folder and write git clone.

Next up, we need to handle virtualization. We recommend [Virtual Box](https://www.virtualbox.org/). Download, run and install.
The cloned github repository from earlier contains a Vagrant file. In order to use it you need to get [Vagrant](https://www.vagrantup.com/). Download, run & install.
If you did not get the Vagrant file from the repository, you can find it [here](https://pastebin.com/7XxNfvGZ).


### Virtual Environment

Navigate to the folder containing the cloned github project or the vagrant file you created using the pastebin. Open a terminal here (On Windows, right-click and GitBash here). Finally in the terminal type:
vagrant up

The first installation is heavy and expect it to take up towards an hour. It installs many useful libraries and programs on your Virtual Machine that we will end up using.
On the other side of the installation type:
`vagrant ssh`

to remote connect to your new virtual enviroment. With a little luck, you should see a similar screen to this ![image](http://i66.tinypic.com/6h2uk9.png).

Your environment is now ready, but let's work in a fitting directory, so use the cd command to navigate to:
/python_course/notebooks
once there type
workon course
and you are now ready to create a Python file in the directory and implement our solution.

### Python file creation

You can create a new Python file in various ways. You can open Jupyter in a browser and work from there or alternatively create one from the command line with:
$ touch filename.py
we recommend Jupyter:

You direct to python_course/notebook.
 e e
From the `/python_course/notebooks` directory you should run the command `jupyter notebook --no-browser --ip=0.0.0.0 --NotebookApp.token=''` to start the Jupyter server.
Accessible by opening any browser outside your Virtual Machine and connecting to 127:0:0.8884

Notice that opening a Jupyter server will reserve the ssh connection, which then will be needed to be closed and opened everytime you wish to navigate the terminal. Done by pressing:
ctrl + c and then Y and enter. Alternatively run a second terminal and vagrant ssh from there to have both. 

You are now ready to implement the code below to do the necessary data handling!
