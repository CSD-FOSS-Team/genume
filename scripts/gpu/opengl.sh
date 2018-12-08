#!/bin/bash

OpenGlVendor=$(glxinfo| grep "OpenGL vendor string"| head -n 1|cut -d ":" -f 2)
OpenGLRendererString=$(glxinfo| grep "OpenGL renderer string"| head -n 1|cut -d ":" -f 2)
OpenGLVersion=$(glxinfo|grep "OpenGL version"| head -n 1|cut -d ":" -f 2)
OpenGLShadLangVersion=$(glxinfo|grep "OpenGL version string"| head -n 1|cut -d ":" -f 2)
OpenGLContextFlags=$(glxinfo|grep "OpenGL context"| head -n 1|cut -d ":" -f 2)
OpenGLExtension=$(glxinfo|grep "OpenGL extensions"| head -n 1|cut -d ":" -f 2)


echo GROUP BAS opengl
echo VALUE BAS OpenGl_Vendor_String \"$OpenGlVendor\"
echo VALUE BAS OpenGl_Rendrerer_String \"$OpenGLRendererString\"
echo VALUE BAS OpenGl_Version \"$OpenGLVersion\"
echo VALUE ADV OpenGL_Shading_Language_Version \"$OpenGLShadLangVersion\"
echo VALUE ADV OpenGL_Context_Flags \"$OpenGLContextFlags\"
echo VALUE ADV OpenGL_Extension \"$OpenGLExtension\"


OpenGLCoreProfVersion=$(glxinfo|grep "OpenGL core profile version"| head -n 1|cut -d ":" -f 2)
OpenGLCoreProfShadLang=$(glxinfo|grep "OpenGL core profile shading"|head -n 1|cut -d ":" -f 2)
OpenGLCoreProfMask=$(glxinfo|grep "OpenGL core profile profile mask"|head -n 1|cut -d ":" -f 2)
OpenGLCoreProfContext=$(glxinfo|grep "OpenGL core profile context"|head -n 1|cut -d ":" -f 2)

echo GROUP BAS opengl
echo VALUE ADV OpenGl_Core_Profile_Version \"$OpenGLCoreProfVersion\"
echo VALUE ADV OpenGl_Core_Profile_Shanding_Language_Version \"$OpenGLCoreProfShadLang\"
echo VALUE ADV OpenGl_Core_Profile_Mask \"$OpenGLCoreProfMask\"
echo VALUE ADV OpenGl_Core_Profile_Context_Flags \"$OpenGLCoreProfContext\"

OpenGLESProfile=$(glxinfo|grep "OpenGL ES profile version"| head -n 1|cut -d ":" -f 2)
OpenGLESProfileExten=$(glxinfo|grep "OpenGL ES profile extensions"| head -n 1|cut -d ":" -f 2)
OpenGLESProfileShadLang=$(glxinfo|grep "OpenGL ES profile shading"| head -n 1|cut -d ":" -f 2)

echo PATH BAS opengl.es
echo VALUE ADV OpenGl_ES_Profile_Version \"$OpenGLESProfile\"
echo VALUE ADV OpenGl_ES_Profile_Extensions \"$OpenGLESProfileExten\"
echo VALUE ADV OpenGl_ES_Profile_Shading_Language \"$OpenGLESProfileShadLang\"
