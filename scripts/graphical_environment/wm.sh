#!/usr/bin/bash
WM="Not Found"
pgrep_flags="-U"
PID="$(pgrep ${pgrep_flags} ${UID} "^$each$")"
if [ "$PID" ]; then
        case $each in
                '2bwm') WM="2bwm";;
                '9wm') WM="9wm";;
                'awesome') WM="Awesome";;
                'beryl') WM="Beryl";;
                'blackbox') WM="BlackBox";;
                'bspwm') WM="bspwm";;
                'budgie-wm') WM="BudgieWM";;
                'chromeos-wm') WM="chromeos-wm";;
                'cinnamon') WM="Muffin";;
                'compiz') WM="Compiz";;
                'deepin-wm') WM="deepin-wm";;
                'dminiwm') WM="dminiwm";;
                'dtwm') WM="dtwm";;
                'dwm') WM="dwm";;
                'e16') WM="E16";;
                'emerald') WM="Emerald";;
                'enlightenment') WM="E17";;
                'fluxbox') WM="FluxBox";;
                'flwm'|'flwm_topside') WM="FLWM";;
                'fvwm') WM="FVWM";;
                'herbstluftwm') WM="herbstluftwm";;
                'howm') WM="howm";;
                'i3') WM="i3";;
                'icewm') WM="IceWM";;
                'kwin') WM="KWin";;
                'metacity') WM="Metacity";;
                'monsterwm') WM="monsterwm";;
                'musca') WM="Musca";;
                'mwm') WM="MWM";;
                'notion') WM="Notion";;
                'openbox') WM="OpenBox";;
                'pekwm') WM="PekWM";;
                'ratpoison') WM="Ratpoison";;
                'sawfish') WM="Sawfish";;
                'scrotwm') WM="ScrotWM";;
                'spectrwm') WM="SpectrWM";;
                'stumpwm') WM="StumpWM";;
                'subtle') WM="subtle";;
                'sway') WM="sway";;
                'swm') WM="swm";;
                'twin') WM="TWin";;
                'wmaker') WM="WindowMaker";;
                'wmfs') WM="WMFS";;
                'wmii') WM="wmii";;
                'xfwm4') WM="Xfwm4";;
                'xmonad.*') WM="XMonad";;
        esac
fi
if [[ ${WM} != "Not Found" ]]; then
        break 1
fi

if [[ ${WM} == "Not Found" ]]; then
        if type -p xprop >/dev/null 2>&1; then
                WM=$(xprop -root _NET_SUPPORTING_WM_CHECK)
                if [[ "$WM" =~ 'not found' ]]; then
                        WM="Not Found"
                elif [[ "$WM" =~ 'Not found' ]]; then
                        WM="Not Found"
                elif [[ "$WM" =~ '[Ii]nvalid window id format' ]]; then
                        WM="Not Found"
                elif [[ "$WM" =~ "no such" ]]; then
                        WM="Not Found"
                else
                        WM=${WM//* }
                        WM=$(xprop -id "${WM}" 8s _NET_WM_NAME)
                        WM=$(echo "$(WM=${WM//*= }; echo "${WM//\"}")")
                fi
        fi
fi

# Proper format WM names that need it.
if [[ ${BASH_VERSINFO[0]} -ge 4 ]]; then
        if [[ ${BASH_VERSINFO[0]} -eq 4 && ${BASH_VERSINFO[1]} -gt 1 ]] || [[ ${BASH_VERSINFO[0]} -gt 4 ]]; then
                WM_lower=${WM,,}
        else
                WM_lower="$(tr '[:upper:]' '[:lower:]' <<< "${WM}")"
        fi
else
        WM_lower="$(tr '[:upper:]' '[:lower:]' <<< "${WM}")"
fi
case ${WM_lower} in
        *'gala'*) WM="Gala";;
        '2bwm') WM="2bwm";;
        'awesome') WM="Awesome";;
        'beryl') WM="Beryl";;
        'blackbox') WM="BlackBox";;
        'budgiewm') WM="BudgieWM";;
        'chromeos-wm') WM="chromeos-wm";;
        'cinnamon') WM="Cinnamon";;
        'compiz') WM="Compiz";;
        'deepin-wm') WM="Deepin WM";;
        'dminiwm') WM="dminiwm";;
        'dwm') WM="dwm";;
        'e16') WM="E16";;
        'echinus') WM="echinus";;
        'emerald') WM="Emerald";;
        'enlightenment') WM="E17";;
        'fluxbox') WM="FluxBox";;
        'flwm'|'flwm_topside') WM="FLWM";;
        'fvwm') WM="FVWM";;
        'gnome shell'*) WM="Mutter";;
        'herbstluftwm') WM="herbstluftwm";;
        'howm') WM="howm";;
        'i3') WM="i3";;
        'icewm') WM="IceWM";;
        'kwin') WM="KWin";;
        'metacity') WM="Metacity";;
        'monsterwm') WM="monsterwm";;
        'muffin') WM="Muffin";;
        'musca') WM="Musca";;
        'mutter'*) WM="Mutter";;
        'mwm') WM="MWM";;
        'notion') WM="Notion";;
        'openbox') WM="OpenBox";;
        'pekwm') WM="PekWM";;
        'ratpoison') WM="Ratpoison";;
        'sawfish') WM="Sawfish";;
        'scrotwm') WM="ScrotWM";;
        'spectrwm') WM="SpectrWM";;
        'stumpwm') WM="StumpWM";;
        'subtle') WM="subtle";;
        'sway') WM="sway";;
        'swm') WM="swm";;
        'twin') WM="TWin";;
        'wmaker') WM="WindowMaker";;
        'wmfs') WM="WMFS";;
        'wmii') WM="wmii";;
        'xfwm4') WM="Xfwm4";;
        'xmonad') WM="XMonad";;
esac
echo VALUE BAS wm $WM
