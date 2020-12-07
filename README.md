# agora

This project serves as a collection of jupyter notebooks to help understand various different parts of life, e.g. statistics, optimization, financial analysis, etc.

## stats

This folder containts examples of statistical distributions and its applications, as well as some key concept in statistics.


Environment Installation
------------------------

The Python environment can be set up in either of the following two ways.
Run the following commands in the console given that you are in the projects folder.

- Using the requirements.txt file

````bash
    conda create --name <Environment_Name> --file requirements.txt
````

- Using the environment.yml file

````bash
    conda env create -f environment.yml
````

If the environment should be installed in a different install path than the default for your system, use the -p
flag followed by the desired path, i.e.:

````bash
    conda create -p <Your_Path> --file requirements.txt
    conda env create -f environment.yml -p <Your_Path>
````

If some additional requirements are necessary, type the following two commands and hence add them to the files:

````bash
    conda list -e > requirements.txt
    conda env export --from-history > environment.yml
````

Git Tips
--------

In order to change the user name and/or user email, open a command line and type one of the following commands:

````bash
    git config --global user.name "<New_User_Name>"
    git config --global user.email "<New_Email>"
    git config --global user.name "<New_User_Name>" user.email "<New_Email>"
````

When you have added or you are going to add 2FA (Tow-Factor-Authentication)
to your GitLab repository, you have to create access tokens.
See [this link](https://kb.lsa.umich.edu/public/index.php/GitLab_command_line_access)
on how to do it.

In short, create a token with the appropriate permissions, it is really important to copy the token you created.
Checkout the repository from the command line with the following format:

````bash
    git clone https://<token_name>:<token_id>@gitlab.lrz.de/<user_name/project_name>/<repo_name>
````
