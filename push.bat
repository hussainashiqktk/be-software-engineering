:: Set the path to the local repository
set repo_path="G:\My GitHub Repos\be-software-engineering"

:: Change to the local repository directory
cd %repo_path%

:: Add all changes to the repository
git add .

:: Commit the changes with a message
git commit -m "update"

:: Push the changes to the remote repository
git push origin main
