cp inkvim/.vimrc ./
if [ -d "/usr/share/vim/vim82" ] ; then
    sudo cp inkvim/edge.vim /usr/share/vim/vim82/colors/
fi
if [ -d "/usr/share/vim/vim74" ] ; then
    sudo cp inkvim/edge.vim /usr/share/vim/vim74/colors/
fi
