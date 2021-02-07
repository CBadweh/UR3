#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/ur_driver"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/cbadweh/UR3/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/cbadweh/UR3/install/lib/python3/dist-packages:/home/cbadweh/UR3/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/cbadweh/UR3/build" \
    "/usr/bin/python3" \
    "/home/cbadweh/UR3/src/UR3e_RG2_ER5-master/ur_driver/setup.py" \
     \
    build --build-base "/home/cbadweh/UR3/build/UR3e_RG2_ER5-master/ur_driver" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/cbadweh/UR3/install" --install-scripts="/home/cbadweh/UR3/install/bin"
