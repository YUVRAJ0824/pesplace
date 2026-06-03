GITHUB SETUP GUIDE - HTTPS METHOD

CHECK GIT CONFIG
git config --global --list
git config --global user.name
git config --global user.email
git config --local --list

LIST FILES
ls
dir
ls -la

SET GIT USER
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

VERIFY CONFIG
git config --global user.name
git config --global user.email

CREATE PERSONAL ACCESS TOKEN (PAT)
1. Go to GitHub.com
2. Click profile → Settings
3. Developer settings → Personal access tokens
4. Tokens (classic)
5. Generate new token (classic)
6. Name: my-git-token
7. Expiration: 90 days
8. Scopes: repo, read:user
9. Generate token
10. COPY TOKEN IMMEDIATELY

INITIALIZE REPO
git init

CHECK REMOTE
git remote -v

ADD REMOTE
git remote add origin https://github.com/username/repo-name.git

VERIFY REMOTE
git remote -v

STAGE FILES
git add .
git add folder-name/
git add filename.txt

CHECK STATUS
git status

CREATE COMMIT
git commit -m "Initial commit"

VIEW HISTORY
git log
git log --oneline

CHECK BRANCHES
git branch
git branch -a

CREATE DEV BRANCH
git checkout -b dev

SWITCH BRANCHES
git checkout main
git checkout dev

PUSH TO GITHUB
git push -u origin dev
git push
git push origin main

PUSH SPECIFIC FOLDER
git add folder-name/
git commit -m "Update folder-name"
git push origin dev

USEFUL COMMANDS
git status - Current status
git log - Commit history
git branch -vv - Branch tracking
git diff - View changes
git remote -v - Remote connection
git diff --cached - Staged changes

TROUBLESHOOTING
git remote -v - Check remote URL
git branch -vv - Check tracking
git branch -r - Remote branches
git branch -d name - Delete branch
git push origin --delete name - Delete remote branch

QUICK WORKFLOW
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git init
git remote add origin https://github.com/username/repo-name.git
git add .
git commit -m "Initial commit"
git checkout -b dev
git push -u origin dev

WINDOWS CREDENTIAL MANAGER
git config --global credential.helper wincred
Win + R → credential-manager → Manage credentials
Find git entry → Edit → Update PAT

REMEMBER
Never commit PAT in code
Always use git status before pushing
Verify config: git config --global --list
Check remote: git remote -v
Verify commits: git log
