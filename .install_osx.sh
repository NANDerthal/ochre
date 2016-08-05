brew install sdl2
brew install sdl2_ttf
brew install glew
brew install glm

git clone https://github.com/smibarber/libSOIL.git
cd libSOIL; make; make install; cd ..;

brew install python3
virtualenv venv -p python3
source venv/bin/activate

