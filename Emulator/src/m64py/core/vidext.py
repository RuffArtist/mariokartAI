# -*- coding: utf-8 -*-
# Author: Milan Nikolic <gen2brain@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ctypes

from PyQt5.QtOpenGL import QGLFormat

try:
    # nvidia hack
    from OpenGL import GL
    glimport = True
except ImportError:
    glimport = False

from m64py.core.defs import *
from m64py.opts import SDL2
from m64py.frontend.log import log

if SDL2:
    from m64py.SDL2 import SDL_WasInit, SDL_InitSubSystem, SDL_QuitSubSystem, SDL_INIT_VIDEO
    from m64py.SDL2 import SDL_GetNumDisplayModes, SDL_DisplayMode, SDL_GetDisplayMode
else:
    from m64py.SDL import SDL_WasInit, SDL_InitSubSystem, SDL_QuitSubSystem, SDL_INIT_VIDEO
    from m64py.SDL import SDL_ListModes, SDL_FULLSCREEN, SDL_HWSURFACE

try:
    if not SDL_WasInit(SDL_INIT_VIDEO):
        SDL_InitSubSystem(SDL_INIT_VIDEO)
    MODES = []
    if SDL2:
        display = SDL_DisplayMode()
        for mode in range(SDL_GetNumDisplayModes(0)):
            ret = SDL_GetDisplayMode(0, mode, ctypes.byref(display))
            if (display.w, display.h) not in MODES:
                MODES.append((display.w, display.h))
    else:
        for mode in SDL_ListModes(None, SDL_FULLSCREEN|SDL_HWSURFACE):
            if (mode.w, mode.h) not in MODES:
                MODES.append((mode.w, mode.h))
    if SDL_WasInit(SDL_INIT_VIDEO):
        SDL_QuitSubSystem(SDL_INIT_VIDEO)
except Exception as err:
    log.warn(str(err))


class Video():
    """Mupen64Plus video extension"""

    def __init__(self):
        """Constructor."""
        self.parent = None
        self.widget = None
        self.glformat = None
        self.glcontext = None

    def set_widget(self, parent):
        """Sets GL widget."""
        self.parent = parent
        self.widget = self.parent.glwidget

    def init(self):
        """Initialize GL context."""
        if not self.glcontext:
            self.glformat = QGLFormat()
            self.glcontext = self.widget.context()
            self.glcontext.setFormat(self.glformat)
            self.glcontext.create()
        return M64ERR_SUCCESS

    def quit(self):
        """Shuts down the video system."""
        if self.glcontext:
            self.glcontext.doneCurrent()
            self.glcontext = None
        return M64ERR_SUCCESS

    def list_fullscreen_modes(self, size_array, num_sizes):
        """Enumerates the available resolutions
        for fullscreen video modes."""
        num_sizes.contents.value = len(MODES)
        for num, mode in enumerate(MODES):
            width, height = mode
            size_array[num].uiWidth = width
            size_array[num].uiHeight = height
        return M64ERR_SUCCESS

    def set_video_mode(self, width, height, bits, mode):
        """Creates a rendering window."""
        self.glcontext.makeCurrent()
        if self.glcontext.isValid():
            if glimport:
                GL.glClearColor(0.0, 0.0, 0.0, 1.0);
                GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
                self.widget.swapBuffers()
                GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
            return M64ERR_SUCCESS
        else:
            return M64ERR_SYSTEM_FAIL

    def set_caption(self, title):
        """Sets the caption text of the
        emulator rendering window. """
        title = "M64Py :: %s" % title.decode()
        self.parent.set_caption.emit(title)
        return M64ERR_SUCCESS

    def toggle_fs(self):
        """Toggles between fullscreen and
        windowed rendering modes. """
        self.widget.toggle_fs.emit()
        return M64ERR_SUCCESS

    def gl_get_proc(self, proc):
        """Used to get a pointer to
        an OpenGL extension function."""
        addr = self.glcontext.getProcAddress(proc.decode())
        if addr is not None:
            return addr.__int__()
        else:
            log.warn("VidExtFuncGLGetProc: '%s'" % proc.decode())

    def gl_set_attr(self, attr, value):
        """Sets OpenGL attributes."""
        attr_map = {
            M64P_GL_DOUBLEBUFFER: self.glformat.setDoubleBuffer,
            M64P_GL_BUFFER_SIZE: self.glformat.setDepthBufferSize,
            M64P_GL_DEPTH_SIZE: self.glformat.setDepth,
            M64P_GL_RED_SIZE: self.glformat.setRedBufferSize,
            M64P_GL_GREEN_SIZE: self.glformat.setGreenBufferSize,
            M64P_GL_BLUE_SIZE: self.glformat.setBlueBufferSize,
            M64P_GL_ALPHA_SIZE: self.glformat.setAlphaBufferSize,
            M64P_GL_SWAP_CONTROL: self.glformat.setSwapInterval,
            M64P_GL_MULTISAMPLEBUFFERS: self.glformat.setSampleBuffers,
            M64P_GL_MULTISAMPLESAMPLES: self.glformat.setSamples
        }
        set_attr = attr_map[attr]
        set_attr(value)
        return M64ERR_SUCCESS

    def gl_get_attr(self, attr, value):
        """Gets OpenGL attributes."""
        attr_map = {
            M64P_GL_DOUBLEBUFFER: self.glformat.doubleBuffer,
            M64P_GL_BUFFER_SIZE: self.glformat.depthBufferSize,
            M64P_GL_DEPTH_SIZE: self.glformat.depth,
            M64P_GL_RED_SIZE: self.glformat.redBufferSize,
            M64P_GL_GREEN_SIZE: self.glformat.greenBufferSize,
            M64P_GL_BLUE_SIZE: self.glformat.blueBufferSize,
            M64P_GL_ALPHA_SIZE: self.glformat.alphaBufferSize,
            M64P_GL_SWAP_CONTROL: self.glformat.swapInterval,
            M64P_GL_MULTISAMPLEBUFFERS: self.glformat.sampleBuffers,
            M64P_GL_MULTISAMPLESAMPLES: self.glformat.samples
        }
        get_attr = attr_map[attr]
        new_value = int(get_attr())
        if new_value == value.contents.value:
            return M64ERR_SUCCESS
        else:
            return M64ERR_SYSTEM_FAIL

    def gl_swap_buf(self):
        """Swaps the front/back buffers after
        rendering an output video frame. """
        self.widget.swapBuffers()
        return M64ERR_SUCCESS

    def resize_window(self, width, height):
        """Called when the video plugin has resized its OpenGL
        output viewport in response to a ResizeVideoOutput() call"""
        return M64ERR_SUCCESS

video = Video()
vidext = m64p_video_extension_functions()
vidext.Functions = 11
vidext.VidExtFuncInit = FuncInit(video.init)
vidext.VidExtFuncQuit = FuncQuit(video.quit)
vidext.VidExtFuncListModes = FuncListModes(video.list_fullscreen_modes)
vidext.VidExtFuncSetMode = FuncSetMode(video.set_video_mode)
vidext.VidExtFuncGLGetProc = FuncGLGetProc(video.gl_get_proc)
vidext.VidExtFuncGLSetAttr = FuncGLSetAttr(video.gl_set_attr)
vidext.VidExtFuncGLGetAttr = FuncGLGetAttr(video.gl_get_attr)
vidext.VidExtFuncGLSwapBuf = FuncGLSwapBuf(video.gl_swap_buf)
vidext.VidExtFuncSetCaption = FuncSetCaption(video.set_caption)
vidext.VidExtFuncToggleFS = FuncToggleFS(video.toggle_fs)
vidext.VidExtFuncResizeWindow = FuncResizeWindow(video.resize_window)
