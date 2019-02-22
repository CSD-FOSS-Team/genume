#!/bin/bash

configure echo grep head cut

# Test if glxinfo command is available.
if ! hash glxinfo 2> /dev/null; then
    value opengl \<opengl info not found\>
    exit 0
fi

# Cache info.
info="$(glxinfo)"

# Parse information
OpenGlVendor=$(echo "$info" | grep "OpenGL vendor string" | head -n 1 | cut -d ":" -f 2)
OpenGLRendererString=$(echo "$info" | grep "OpenGL renderer string" | head -n 1 | cut -d ":" -f 2)
OpenGLVersion=$(echo "$info" | grep "OpenGL version" | head -n 1 | cut -d ":" -f 2)
OpenGLShadLangVersion=$(echo "$info" | grep "OpenGL version string" | head -n 1 | cut -d ":" -f 2)
OpenGLContextFlags=$(echo "$info" | grep "OpenGL context" | head -n 1 | cut -d ":" -f 2)
OpenGLExtension=$(echo "$info" | grep "OpenGL extensions" | head -n 1 | cut -d ":" -f 2)

subcat opengl
value OpenGl_Vendor_String $OpenGlVendor
value OpenGl_Rendrerer_String $OpenGLRendererString
value OpenGl_Version $OpenGLVersion
value --advanced OpenGL_Shading_Language_Version $OpenGLShadLangVersion
value --advanced OpenGL_Context_Flags $OpenGLContextFlags
>&2 echo $OpenGLExtension
value --advanced OpenGL_Extension $OpenGLExtension

OpenGLCoreProfVersion=$(echo "$info" | grep "OpenGL core profile version" | head -n 1 | cut -d ":" -f 2)
OpenGLCoreProfShadLang=$(echo "$info" | grep "OpenGL core profile shading" | head -n 1 | cut -d ":" -f 2)
OpenGLCoreProfMask=$(echo "$info" | grep "OpenGL core profile profile mask" | head -n 1 | cut -d ":" -f 2)
OpenGLCoreProfContext=$(echo "$info" | grep "OpenGL core profile context" | head -n 1 | cut -d ":" -f 2)

subcat opengl
value --advanced OpenGl_Core_Profile_Version $OpenGLCoreProfVersion
value --advanced OpenGl_Core_Profile_Shanding_Language_Version $OpenGLCoreProfShadLang
value --advanced OpenGl_Core_Profile_Mask $OpenGLCoreProfMask
value --advanced OpenGl_Core_Profile_Context_Flags $OpenGLCoreProfContext

OpenGLESProfile=$(echo "$info" | grep "OpenGL ES profile version" | head -n 1 | cut -d ":" -f 2)
OpenGLESProfileExten=$(echo "$info" | grep "OpenGL ES profile extensions" | head -n 1 | cut -d ":" -f 2)
OpenGLESProfileShadLang=$(echo "$info" | grep "OpenGL ES profile shading" | head -n 1 | cut -d ":" -f 2)

subcat opengl.es
value --advanced OpenGl_ES_Profile_Version $OpenGLESProfile
value --advanced OpenGl_ES_Profile_Extensions $OpenGLESProfileExten
value --advanced OpenGl_ES_Profile_Shading_Language $OpenGLESProfileShadLang
