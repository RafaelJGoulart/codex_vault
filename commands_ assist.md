########################################################
Git
########################################################
echo "# codex_vault" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/RafaelJGoulart/codex_vault.git
git push -u origin main

git remote add origin https://github.com/RafaelJGoulart/codex_vault.git
git branch -M main
git push -u origin main

git status
git add .
git commit -m "mensagem"
git push


########################################################
Python Venv
########################################################

Venv/Scripts/activate

pip freeze > requirements.txt
