pause() {
    read -n1 -r -p "Press any key to continue..." key
    espeak -ven-us+f2 -s170 "Please wait" |  python progress.py
}
banner() {
    clear
    echo -e "\e[1;31m"
    if ! [ -x "$(command -v figlet)" ]; then
        echo 'Introducing FTOOL'
    else
        figlet FTOOL
    fi
    if ! [ -x "$(command -v toilet)" ]; then
        echo -e "\e[4;34m This TOOL Was Created By \e[1;32mHUNT3R \e[0m"
    else
        echo -e "\e[1;34mCreated By \e[1;34m"
        toilet -f mono12 -F border HUNT3R
    fi
    echo -e "\e[1;32m           Managed By: DINESH CHAUDHARY \e[0m"
    echo " "
    echo " "
}


banner
pause

install_deps(){
    INSTALL="pkg install -y"
    packages=(openssl git python figlet toilet mplayer espeak )
    if [ -n "$INSTALL" ];then
        for package in ${packages[@]}; do
            $INSTALL $package
        done
        pip install -r requirements.txt
    else
        echo "We could not install dependencies."
        echo "Please make sure you have git, python3, pip3 and requirements installed."
        exit
    fi
}

if [ -f .hunter ];then
    echo "All Requirements Found...."
else
    echo 'Installing Requirements....'
    echo .
    echo .
    install_deps
    echo We Fuck The Fuckers.> .hunter
    echo 'Requirements Installed....'
    pause
fi



while :
do
    banner
    echo -e "\e[1;31m >>>>>>To avoid get-error Always Enter Correct Filename<<<<<< \e[0m"
    echo " "
    echo " "
    echo -e "\e[45mMENU: ☟︎︎︎☟︎︎︎  \e[0m "
    echo ""
    echo -e "\e[93m[1]   MP3 Tools "
    echo -e "\e[93m[2]   Video To Gif "
    echo -e "\e[93m[3]   QrCode Genrator"
    echo -e "\e[93m[4]   S-Fast SMS Bombing"
    echo -e "\e[93m[5]   Follow me on Instagram \e[0m"
    echo -e "\e[93m[6]   Exit \e[1;96m"
    read -p "Choose option[1-6] :" ch
    clear
    if [ $ch -eq 1 ];then
        python mptool.py
        exit
    elif [ $ch -eq 2 ];then
        bash gifbann
        python gif.py
        exit
    elif [ $ch -eq 3 ];then
        banner
        echo -e "\e[92m  COMING SOON!!\e[0m"
        exit
    elif [ $ch -eq 4 ];then
        python boom.py
        clear
        banner
        echo -e "\e[1;93m                   MESSAGES SENT Successfully!!\e[0m"
        exit
   elif [ $ch -eq 5 ];then
        banner
        xdg-open https://instagram.com/raazzz136
        pause
    elif [ $ch -eq 6 ];then
        banner
        exit
    else
        clear
        banner
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
