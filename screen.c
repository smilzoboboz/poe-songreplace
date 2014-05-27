/*  Copyright (C)   2011-2012   Nicolo' Barbon

    This file is part of Calise.

    Calise is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    Calise is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Calise.  If not, see <http://www.gnu.org/licenses/>.

*/


#include <Python.h>
#include <stdio.h>
#include <X11/Xlib.h>


/* standard cameramodule python-error */
//static PyObject* ScreenError;


/* functions declaration */
static PyObject* get_color_pixels (PyObject* self, PyObject *args);


static PyObject *
get_color_pixels(PyObject *self, PyObject *args)
{
    char* screen_name = NULL;
    char* color_code = NULL;

    if (!PyArg_ParseTuple(args, "ss", &screen_name, &color_code))
        return NULL;
    
    Display
        *display;

    Window
        root_window;
    XImage
        *ximage;
    int
        x=1179, y=31,
        w=100, h=9;
    int
        p, r=0, g=0, b=0,
        cr=135, cg=86, cb=33;

    display = XOpenDisplay(screen_name);
    if ( !display )
    {
        return NULL;
    }

    root_window=XRootWindow(display, XDefaultScreen(display));
    ximage = XGetImage(display, root_window, x,y, w,h, AllPlanes, ZPixmap);
    if (ximage == (XImage *) NULL)
        return NULL;

    XCloseDisplay(display);

    // takes 1 pixel every div*div area (div values > 8 will almost not 
    // give performance improvements)
    int i,k,counter=0;
    int matching_pixels[100];
    for (i=0; i<w; i++) {
        for (k=0; k<h; k++) {

            // obtain r,g,b components from hex(p)
            p = XGetPixel(ximage,i,k);
            r=((int) p >> 16) & 0xFF;
            g=((int) p >> 8) & 0xFF;
            b=((int) p) & 0xFF;
            // menu-only check
            if ( r == 114 && g == 88 && b == 57 && i < 20 && k == 4)
            {
                //printf("height: %i // r: %i, g: %i, b: %i\n", k, r, g, b);
                matching_pixels[counter] = 900 + i;
                counter += 1;
            }
            // normal pixel matcher
            if ( r == cr && g == cg && b == cb && i > 9)
            {
                if ( counter < 100 )
                {
                    matching_pixels[counter] = i * 10 + k;
                    counter += 1;
                }
            }
        }
    }
    int blabla[counter];
    int j;
    for ( j=0; j < counter; j++ )
    {
        blabla[j] = matching_pixels[j];
    }
    //free(matching_pixels);

    XDestroyImage(ximage);
    
    PyObject *l = PyList_New(counter);
    size_t ii;
    for (ii = 0; ii != counter; ++ii) {
        PyList_SET_ITEM(l, ii, PyInt_FromLong(blabla[ii]));
    }
    
    return l; //Py_BuildValue("O", blabla);
}

// Copy-pasted...
/*
PyObject *makelist(int array[], size_t size)
{
    PyObject *l = PyList_New(size);
    for (size_t i = 0; i != size; ++i) {
        PyList_SET_ITEM(l, i, PyInt_FromLong(array[i]));
    }
    return l;
}
*/


/* Python related stuff */
static PyMethodDef screen_funcs[] = {
    {"get_pixeldata", (PyCFunction)get_color_pixels, METH_VARARGS},
    {NULL}
};

PyMODINIT_FUNC initscreen(void)
{
    //PyObject* m;

    Py_InitModule3("screen", screen_funcs,
                   "Display brightness calculator module");
    //ScreenError = PyErr_NewException("screenBrightnessmodule.ScreenError", NULL, NULL);
    //if (ScreenError)
    //    PyModule_AddObject(m, "Error", ScreenError);
}
