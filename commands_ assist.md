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

pip install -r requirements.txt

Venv/Scripts/activate

pip freeze > requirements.txt

########################################################
Clonar repositório
########################################################

git config --global user.name "Seu Nome"
git config --global user.email "Seu Email"

git clone URL_DO_REPO
cd codex_vault

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt