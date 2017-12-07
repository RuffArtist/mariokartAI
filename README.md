# mariokartAI


Instructions to install python console M64py:

0. 	Install m64py-0.2.3 (https://sourceforge.net/projects/m64py/files/m64py-0.2.3/m64py-0.2.3.tar.gz/download)
1. 	https://github.com/mupen64plus/mupen64plus-core.git (https://github.com/mupen64plus/mupen64plus-core/tree/d679ba0292be679fe1ba27e611b0015708c2dfec)
2. 	Change name of the folder to mupen64plus-core
3.1. 	Go to mupen64plus-core/projects/unix
3.2. 	Install possible dependences:
		- In terminal: sudo apt-get install binutils-dev
4. 	In terminal: make all DEBUGGER=1 CPU=x86
5. 	Download: https://bitbucket.org/runhello/mupen64plus-input-sdl/downloads/
5.1. 	**** mupen64plus-core must be in the same root folder than the downloaded folder
5.2. 	Go to runhello-mupen64plus-input-sdl-29c932285dd9/projects/unix
5.3.	Install possible dependences:
		- In terminal: sudo apt-get install libiberty-dev
5.4. 	In terminal: make all DEBUGGER=1 CPU=x86
6 .	Move library from 5.4 to M64py generic plugin folder (/usr/lib/x86_64-linux-gnu/mupen64plus)
6.1. 	In terminal: sudo cp mupen64plus-input-sdl.so /usr/lib/x86_64-linux-gnu/mupen64plus
7. 	Download: https://bitbucket.org/runhello/mupen64plus-ui-python/downloads/
8.	Open folder and search for README_ORIGINAL.md
		In terminal: python setup.py install
		In terminal: python setup.py build_qt
9. 	Possible dependences: 
		- pip install pysdl2
10. 	Open m64py-0.2.3 (m64py)
		- Go to settings and change the Library file path for the one generated in point 4
