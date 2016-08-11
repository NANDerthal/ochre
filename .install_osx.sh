brew install sdl2
brew install sdl2_ttf
brew install glew
brew install glm

git clone https://github.com/smibarber/libSOIL.git
cd libSOIL; make; make install; cd ..;

export PYTHON=$TRAVIS_PYTHON_VERSION

brew install python$PYTHON
virtualenv venv -p python$PYTHON
source venv/bin/activate

export PYTHON=$TRAVIS_PYTHON_VERSION

