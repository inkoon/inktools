cp .vimrc ~/
DIR=`ls -d /usr/share/vim/*/ | grep /usr/share/vim/vim`
if [ -d $DIR ] ; then
    sudo cp edge.vim $DIR/colors/
fi
