#!/bin/bash


pipe='/tmp/mplayer_pipe'
globalvol=20

function init_slave {
    # mplayer slave session initialization.
    #
    # The first song to be played has to be specified as argument %1
    #
    # NOTE: This has to be manually input, the main program won't handle
    #       mplayer slave initialization
    #
    rm -rf $pipe
    mkfifo $pipe
    mplayer \
        -slave -vo null -loop 0 \
        -ao alsa -volume $globalvol -softvol-max 100 \
        -input file=$pipe \
        "`env python2 -c "import zonedata; print(zonedata.zones['Menu']['song'])"`"
}

function change_song {
    #
    for (( x=0; x<$globalvol; x++ ))
    do
        echo "volume -1" > $pipe
        sleep "`env python -c "print(3/$globalvol)"`"
    done
    echo "loadfile \"$1\"" > $pipe
    echo "volume $globalvol 1" > $pipe
}

change_song "$1"