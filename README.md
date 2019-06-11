# script-to-download-dependencies

Most of the programming languages have tools to manually define project dependencies and simple command line interfaces to download those dependencies. For example Java have Maven and NodeJs have npm. In Java we define pom.xml and in npm we use package.json. You need to build a tool to automatically download python packages. 


Input:
A json file containing different dependencies

Output: 

A script in any language to download and install all these dependencies. 

If case all are successfully installed print success

If some failed then print list of all failed packages, one of each in separate line. 



Note: You can use PIP or any other command line tool to install python packages



Handle cases like: 

When one library fail to download then the process shall continue.


