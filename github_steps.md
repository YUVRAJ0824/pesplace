# COMPLETE GITHUB REPOSITORY WORKFLOW GUIDE

## STEP 0: SETUP GIT CONFIGURATION

### 0.1 - Set Global Git User (One-time setup)
```bash
git config --global user.name"yuvraj"
git config --global user.email"yraj3342@gmail.com"
```

### 0.2 - Verify Git Configuration
```bash
git config --global user.name
git config --global user.email
git config --global --list
```

### 0.3 - Create Personal Access Token (PAT) on GitHub
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name it: `my-git-token`
4. Set Expiration: 90 days
5. Select Scopes: `repo`, `read:user`
6. Click "Generate token"
7. **COPY AND SAVE TOKEN IMMEDIATELY** (you won't see it again)

---

## STEP 1: CREATE LOCAL REPOSITORY

### 1.1 - Navigate to Your Project Directory
```bash
cd c:\Users\yraj3\Desktop\pes\ place
```

### 1.2 - List Files in Directory
```bash
ls -la
dir
```

### 1.3 - Initialize Local Git Repository
```bash
git init
```
This creates a `.git` folder in your project.

---

## STEP 2: CREATE REPOSITORY ON GITHUB

### 2.1 - Go to GitHub
1. Visit https://github.com
2. Click "+" icon → "New repository"
3. Repository name: (e.g., `pes-place`)
4. Description: (optional)
5. Choose: Public or Private
6. Click "Create repository"
7. **DO NOT initialize with README** (you already have local files)

### 2.2 - Copy Repository URL
Copy the HTTPS URL: `https://github.com/username/repo-name.git`

---

## STEP 3: CONNECT LOCAL TO REMOTE REPOSITORY

### 3.1 - Add Remote Origin
```bash
git remote add origin https://github.com/username/repo-name.git
```
Replace `username` and `repo-name` with your actual GitHub details.

### 3.2 - Verify Remote Connection
```bash
git remote -v
```
You should see:
```
origin  https://github.com/username/repo-name.git (fetch)
origin  https://github.com/username/repo-name.git (push)
```

---

## STEP 4: STAGE FILES FOR COMMIT

### 4.1 - Check Current Status
```bash
git status
```
This shows untracked files (in red) and changes.

### 4.2 - Add All Files
```bash
git add .
```
This stages all files in current directory and subdirectories.

### 4.3 - Add Specific Files/Folders (Alternative)
```bash
git add D1/
git add D2/main.html
git add filename.txt
```

### 4.4 - Verify Staged Files
```bash
git status
```
Staged files should appear in green.

---

## STEP 5: CREATE YOUR FIRST COMMIT

### 5.1 - Create Commit with Message
```bash
git commit -m "Initial commit"
```

### 5.2 - View Commit History
```bash
git log
git log --oneline
```

---

## STEP 6: PUSH TO GITHUB

### 6.1 - Push to Remote (First Time)
```bash
git push -u origin main
```
The `-u` flag sets `main` as the default branch for future pushes.

### 6.2 - For Subsequent Pushes
```bash
git push
```
Or explicitly:
```bash
git push origin main
```

### 6.3 - When Prompted for Password
Paste your Personal Access Token (from Step 0.3) as the password.

---

## STEP 7: CREATE AND WORK WITH BRANCHES (Optional)

### 7.1 - Check Current Branch
```bash
git branch
```

### 7.2 - Create New Branch
```bash
git checkout -b dev
```
or
```bash
git checkout -b feature/new-feature
```

### 7.3 - Switch Between Branches
```bash
git checkout main
git checkout dev
```

### 7.4 - Push New Branch to GitHub
```bash
git push -u origin dev
```

---

## STEP 8: DAILY WORKFLOW (ADD → COMMIT → PUSH)

### 8.1 - After Making Changes
```bash
git status                           # Check what changed
git add .                            # Stage all changes
git commit -m "Descriptive message"  # Create commit
git push                             # Push to GitHub
```

### 8.2 - Commit Message Best Practices
```bash
git commit -m "Add Python abstraction module"
git commit -m "Fix bug in animal.py"
git commit -m "Update main.html styling"
git commit -m "Implement polymorphism feature"
```

### 8.3 - Push Specific Folder/Branch
```bash
git add D3/                    # Stage specific folder
git commit -m "Update D3 module"
git push origin dev            # Push to dev branch
```

---

## USEFUL COMMANDS REFERENCE

| Command | Purpose |
|---------|---------|
| `git status` | Show current status |
| `git log` | View commit history |
| `git log --oneline` | Compact commit history |
| `git diff` | View changes before staging |
| `git diff --cached` | View staged changes |
| `git remote -v` | Show remote URLs |
| `git branch -a` | Show all branches (local & remote) |
| `git branch -vv` | Show branch tracking info |

---

## TROUBLESHOOTING

### Issue: "fatal: not a git repository"
**Solution:** Run `git init` in project directory

### Issue: "fatal: destination path already exists"
**Solution:** Repository already cloned; use `git pull` instead

### Issue: "remote origin already exists"
**Solution:** Remove and re-add:
```bash
git remote remove origin
git remote add origin https://github.com/username/repo-name.git
```

### Issue: "Permission denied" when pushing
**Solution:** 
1. Check token has `repo` scope
2. Paste Full token (not username) when prompted for password
3. Or use SSH keys instead

### Check Remote URL
```bash
git remote -v
```

### Delete Branch Locally
```bash
git branch -d branch-name
```

### Delete Branch on GitHub
```bash
git push origin --delete branch-name
```

---

## COMPLETE QUICK START (Copy & Paste)

```bash
# Setup (one-time)
git config --global user.name "yuvraj"
git config --global user.email "yraj3342@gmail.com"

# Initialize local repo
git init
git remote add origin https://github.com/username/repo-name.git
git remote -v

# First commit and push
git add .
git status
git commit -m "Initial commit"
git push -u origin main

# For future changes
git add .
git commit -m "Your message"
git push
```
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
