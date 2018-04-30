#!/bin/bash

OpenGlVendor=$(glxinfo| grep "OpenGL vendor string"| head -n 1|cut -d ":" -f 2)
OpenGLRendererString=$(glxinfo| grep "OpenGL renderer string"| head -n 1|cut -d ":" -f 2)
OpenGLVersion=$(glxinfo|grep "OpenGL version"| head -n 1|cut -d ":" -f 2)
OpenGLShadLangVersion=$(glxinfo|grep "OpenGL version string"| head -n 1|cut -d ":" -f 2)
OpenGLContextFlags=$(glxinfo|grep "OpenGL context"| head -n 1|cut -d ":" -f 2)
OpenGLExtension=$(glxinfo|grep "OpenGL extensions"| head -n 1|cut -d ":" -f 2)



echo VALUE BAS OpenGl_Vendor_String \"$OpenGlVendor\"
echo VALUE BAS OpenGl_Rendrerer_String \"$OpenGLRendererString\"
echo VALUE BAS OpenGl_Version \"$OpenGLVersion\"
echo VALUE ADV OpenGL_Shading_Language_Version \"$OpenGLShadLangVersion\"
echo VALUE ADV OpenGL_Context_Flags \"$OpenGLContextFlags\"
echo VALUE ADV OpenGL_Extension \"$OpenGLExtension\"
