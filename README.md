# How To Install DeepLabCut

DeepLabCut is a toolbox for markerless pose estimation of animals performing various tasks.[ Read a short development and application summary below](https://github.com/DeepLabCut/DeepLabCut#why-use-deeplabcut). As long as you can see (label) what you want to track, you can use this toolbox, as it is animal and object agnostic. DeepLabCut can be run on Windows, Linux, or MacOS. This tutorial is based on the original DLC tutorial at:



* [https://github.com/DeepLabCut/DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) 
* [https://deeplabcut.github.io/DeepLabCut/docs/intro.html](https://deeplabcut.github.io/DeepLabCut/docs/intro.html) 

The original papers can be found at:

* [https://www.nature.com/articles/s41593-018-0209-y](https://www.nature.com/articles/s41593-018-0209-y) 
* [https://www.nature.com/articles/s41596-019-0176-0](https://www.nature.com/articles/s41596-019-0176-0) 

The tutorials are also available as PDF files in the PDF_Tutorial folder.

A tutorial about how to use DLC can be found in the wiki of this repository: https://github.com/LW1989/DLC_tutorial/wiki/How-to-use-DeepLabCut 

## Step 1: You need to have Python installed

Simply download Anaconda: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution) 

Anaconda is perhaps the easiest way to install Python and additional packages across various operating systems. With Anaconda you create all the dependencies in an environment on your machine. For more information see:

[https://conda.io/docs/user-guide/tasks/manage-environments.html](https://conda.io/docs/user-guide/tasks/manage-environments.html)


## Step 2: Install Git



* Install Git on Windows: 
    * Navigate to the latest Git for Windows installer and download the latest version.
    * Once the installer has started, follow the instructions as provided in the Git Setup wizard screen until the installation is complete. 
    * Open the windows command prompt (or Git Bash if you selected not to use the standard Git Windows Command Prompt during the Git installation).
    * Type `git version` to verify Git was installed.

    **Note:** git-scm ([https://git-scm.com/](https://git-scm.com/)) is a popular and recommended resource for downloading Git for Windows. The advantage of downloading Git from git-scm is that  your download automatically starts with the latest version of Git included with the  recommended command prompt, Git Bash . The download source is the same Git for Windows installer as referenced in the steps above.


    

* Install Git on Mac: Most versions of MacOS will already have Git installed, and you can activate it through the terminal with git version. After typing `git version` into your terminal, usually your Mac asks you to install the “command line developer tools”

    

* Install Git From an Installer: git-scm is a popular and recommended resource for downloading Git on a Mac. The advantage of downloading Git from git-scm is that your download automatically starts with the latest version of Git. The download source is the same macOS Git Installer as referenced in the steps above. Open the command prompt "terminal" and type `git version` to verify Git was installed.


## Step 2: Get DLC from GitHub



* Create a folder where you want to install DLC
* Open Terminal (Mac) or Anaconda Command Prompt (Windows) and type the following command:  `cd **Full path of the folder**`
* Type: `git clone https://github.com/DeepLabCut/DeepLabCut.git` 
* Now, in Terminal or Anaconda Command Prompt, go to the subfolder of the cloned repo. For example, If you cloned the repo onto your Desktop, the command may look like:

     `cd C:\Users\YourUserName\Desktop\DeepLabCut\conda-environments`


To get the location right, a cool trick is to drag the folder and drop it into Terminal. Alternatively, you can (on Windows) hold SHIFT and right-click > Copy as path, or (on Mac) right-click and while in the menu press the OPTION key to reveal Copy as Pathname.



* Now, in the terminal run: `conda env create -f DEEPLABCUT.yaml`
* You can now use this environment from anywhere on your computer (i.e. no need to go back into the conda- folder). Just enter your environment by running the following command within the terminal or the anaconda command prompt :
    * MacOS: `conda activate nameoftheenv` (eg. DEEPLABCUT)
    * Windows: `activate nameoftheenv` (eg. DEEPLABCUT)
* Now you should see (“nameofenv”) on the left of your terminal screen, i.e. (DEEPLABCUT) YourName-MacBook. NOTE: no need to run pip install deeplabcut, as it is already installed!!! :)

**<span style="text-decoration:underline;">**Great, that's it! DeepLabCut is installed!**</span>**

For a guide about how to use DLC please check the PDF_Tutorial folder


## Pro Tips:

If you ever want to update your DLC, just run `pip install --upgrade deeplabcut` once you are inside your env. Here are some conda environment management tips: 

[https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index](https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index) 


## Troubleshooting:

FFMPEG: A few Windows users report needing to install re-install ffmpeg (after windows updates) as described here (A potential error could occur when making new videos): 

[https://video.stackexchange.com/questions/20495/how-do-i-set-up-and-use-ffmpeg-in-windows](https://video.stackexchange.com/questions/20495/how-do-i-set-up-and-use-ffmpeg-in-windows)  







 

