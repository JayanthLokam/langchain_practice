# To find does the langchain is installed or not we need to use these command in windows powershell:
pip list | findstr "langchain"
- these command gives us an output as list of the packages installed in the computer 

# To uninstall all the old packages of the langchain 
pip uninstall x,y,z -y
x,y,z -represents the names of the packages we have to mention from the list that we got as an output from the earlier command 

# TO install the new chain fresh we have to use the command:
pip install -U langchain or pip install langchain
-U represents to update the packages old ones 
