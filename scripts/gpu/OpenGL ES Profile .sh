#!/bin/bash

OpenGLESProfile=$(glxinfo|grep "OpenGL ES profile version"| head -n 1|cut -d ":" -f 2)
OpenGLESProfileExten=$(glxinfo|grep "OpenGL ES profile extensions"| head -n 1|cut -d ":" -f 2)
OpenGLESProfileShadLang=$(glxinfo|grep "OpenGL ES profile shading"| head -n 1|cut -d ":" -f 2)

echo PATH BAS opengl.es
echo VALUE ADV OpenGl_ES_Profile_Version \"$OpenGLESProfile\"
echo VALUE ADV OpenGl_ES_Profile_Extensions \"$OpenGLESProfileExten\"
echo VALUE ADV OpenGl_ES_Profile_Shading_Language \"$OpenGLESProfileShadLang\"
