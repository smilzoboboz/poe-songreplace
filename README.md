C lib build commands (from setuptools):
    gcc -pthread -DNDEBUG -march=x86-64 -mtune=generic -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -march=x86-64 -mtune=generic -O2 -pipe -fstack-protector-strong --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2 -fPIC -I/usr/include/python2.7 -c screen.c -o screen.o
    gcc -pthread -shared -Wl,-O1,--sort-common,--as-needed,-z,relro -Wl,-O1,--sort-common,--as-needed,-z,relro -march=x86_64 -mtune=generic -O2 -pipe -fstack-protector-strong --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2 screen.o -L/usr/lib -lX11 -lpython2.7 -o screen.so

