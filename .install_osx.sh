brew install sdl2
brew install sdl2_ttf
brew install glew
brew install glm

git clone https://github.com/smibarber/libSOIL.git
cd libSOIL; make; make install; cd ..;

brew install $PYTHON
virtualenv venv -p $PYTHON
source venv/bin/activate

