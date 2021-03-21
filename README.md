# find-dead-links
This progam was created for the use of finding broken/inactive links on a website.

##Installation
Before you install, make sure you have python3 and virtualenv. After those dependencies are installed and the repository has been cloned, use the command make install INSTALL_DIR=<where you want the program>. It is best that you specify a directory that is already in your path.

##RUNNING
Run either of these commands:
find-dead-links <url>
find-dead-links -<search depth> <url>
Specifying a search deapth will recursively search the input url and its children urls until. Not specifying a search depth will search just the input url.

