#!/bin/bash

info="$(glxinfo)"

OpenGlVendor=$(echo "$info"| grep "OpenGL vendor string"| head -n 1|cut -d ":" -f 2)
OpenGLRendererString=$(echo "$info"| grep "OpenGL renderer string"| head -n 1|cut -d ":" -f 2)
OpenGLVersion=$(echo "$info"|grep "OpenGL version"| head -n 1|cut -d ":" -f 2)
OpenGLShadLangVersion=$(echo "$info"|grep "OpenGL version string"| head -n 1|cut -d ":" -f 2)
OpenGLContextFlags=$(echo "$info"|grep "OpenGL context"| head -n 1|cut -d ":" -f 2)
OpenGLExtension=$(echo "$info"|grep "OpenGL extensions"| head -n 1|cut -d ":" -f 2)


echo GROUP BAS opengl
echo VALUE BAS OpenGl_Vendor_String \"$OpenGlVendor\"
echo VALUE BAS OpenGl_Rendrerer_String \"$OpenGLRendererString\"
echo VALUE BAS OpenGl_Version \"$OpenGLVersion\"
echo VALUE ADV OpenGL_Shading_Language_Version \"$OpenGLShadLangVersion\"
echo VALUE ADV OpenGL_Context_Flags \"$OpenGLContextFlags\"
echo VALUE ADV OpenGL_Extension \"$OpenGLExtension\"


OpenGLCoreProfVersion=$(echo "$info"|grep "OpenGL core profile version"| head -n 1|cut -d ":" -f 2)
OpenGLCoreProfShadLang=$(echo "$info"|grep "OpenGL core profile shading"|head -n 1|cut -d ":" -f 2)
OpenGLCoreProfMask=$(echo "$info"|grep "OpenGL core profile profile mask"|head -n 1|cut -d ":" -f 2)
OpenGLCoreProfContext=$(echo "$info"|grep "OpenGL core profile context"|head -n 1|cut -d ":" -f 2)

echo GROUP BAS opengl
echo VALUE ADV OpenGl_Core_Profile_Version \"$OpenGLCoreProfVersion\"
echo VALUE ADV OpenGl_Core_Profile_Shanding_Language_Version \"$OpenGLCoreProfShadLang\"
echo VALUE ADV OpenGl_Core_Profile_Mask \"$OpenGLCoreProfMask\"
echo VALUE ADV OpenGl_Core_Profile_Context_Flags \"$OpenGLCoreProfContext\"

OpenGLESProfile=$(echo "$info"|grep "OpenGL ES profile version"| head -n 1|cut -d ":" -f 2)
OpenGLESProfileExten=$(echo "$info"|grep "OpenGL ES profile extensions"| head -n 1|cut -d ":" -f 2)
OpenGLESProfileShadLang=$(echo "$info"|grep "OpenGL ES profile shading"| head -n 1|cut -d ":" -f 2)

echo PATH BAS opengl.es
echo VALUE ADV OpenGl_ES_Profile_Version \"$OpenGLESProfile\"
echo VALUE ADV OpenGl_ES_Profile_Extensions \"$OpenGLESProfileExten\"
echo VALUE ADV OpenGl_ES_Profile_Shading_Language \"$OpenGLESProfileShadLang\"
