# mariokartAI


Instructions to install python console M64py:

0. 	Possible dependences:
		sudo apt-get install binutils-dev
		sudo apt-get install libiberty-dev
		pip install pysdl2

1. 	Install m64py-0.2.3 (https://sourceforge.net/projects/m64py/files/m64py-0.2.3/m64py-0.2.3.tar.gz/download)

2. 	https://github.com/mupen64plus/mupen64plus-core.git (https://github.com/mupen64plus/mupen64plus-core/tree/d679ba0292be679fe1ba27e611b0015708c2dfec)

3. 	Change name of the folder to mupen64plus-core

4. 	Go to mupen64plus-core/projects/unix

5. 	In terminal: make all DEBUGGER=1 CPU=x86

6. 	Download: https://bitbucket.org/runhello/mupen64plus-input-sdl/downloads/

7. 	**** mupen64plus-core must be in the same root folder than the downloaded folder

8. 	Go to runhello-mupen64plus-input-sdl-29c932285dd9/projects/unix

9. 	In terminal: make all DEBUGGER=1 CPU=x86

10.	Move library from 5.4 to M64py generic plugin folder (/usr/lib/x86_64-linux-gnu/mupen64plus)

11. 	In terminal: sudo cp mupen64plus-input-sdl.so /usr/lib/x86_64-linux-gnu/mupen64plus

12. 	Download: https://bitbucket.org/runhello/mupen64plus-ui-python/downloads/

13.	Open folder and search for README_ORIGINAL.md
		In terminal: python setup.py install
		In terminal: python setup.py build_qt
		
14. 	Open m64py-0.2.3 (m64py)
		- Go to settings and change the Library file path for the one generated in point 4

15. You are good to go ! 
