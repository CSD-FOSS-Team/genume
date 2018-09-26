#!/bin/bash


OpenGLCoreProfVersion=$(glxinfo|grep "OpenGL core profile version"| head -n 1|cut -d ":" -f 2)

OpenGLCoreProfShadLang=$(glxinfo|grep "OpenGL core profile shading"|head -n 1|cut -d ":" -f 2)

OpenGLCoreProfMask=$(glxinfo|grep "OpenGL core profile profile mask"|head -n 1|cut -d ":" -f 2)

OpenGLCoreProfContext=$(glxinfo|grep "OpenGL core profile context"|head -n 1|cut -d ":" -f 2)


echo GROUP BAS opengl
echo VALUE ADV OpenGl_Core_Profile_Version \"$OpenGLCoreProfVersion\"
echo VALUE ADV OpenGl_Core_Profile_Shanding_Language_Version \"$OpenGLCoreProfShadLang\"
echo VALUE ADV OpenGl_Core_Profile_Mask \"$OpenGLCoreProfMask\"
echo VALUE ADV OpenGl_Core_Profile_Context_Flags \"$OpenGLCoreProfContext\"
