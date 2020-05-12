cd C:\Users\ktais\github\atcoder
git init
git config --global user.name "Taishiro Kitahara"
git config --global user.email "ktaishiro1227@gmail.com"
git clone https://github.com/galileo15640215/atcoder C:\Users\ktais\github\atcoder\atcoder
xcopy /d C:\Users\ktais\desktop\at C:\Users\ktais\github\atcoder\atcoder
cd atcoder
git add --all
git commit -m "auto commit"
git push -f
exit
