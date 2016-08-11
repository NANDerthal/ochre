brew install sdl2
brew install sdl2_ttf
brew install glew
brew install glm

git clone https://github.com/smibarber/libSOIL.git
cd libSOIL; make; make install; cd ..;

brew install python$TRAVIS_PYTHON_VERSION
virtualenv venv -p python$TRAVIS_PYTHON_VERSION
source venv/bin/activate

