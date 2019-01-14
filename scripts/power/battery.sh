#!/bin/bash

# Float point divisions have been done without the use of extra tools.
# The output is human readable.

# Looks for all the power supplies.
dir=$(find /sys/ -name power_supply -type d 2>/dev/null)

# Distinguises the batteries.
dir=$(grep -lir Battery $dir 2>/dev/null)
cnt=0

# Counts the batteries.
for i in $dir; do
    cnt=$(($cnt + 1))
done
echo VALUE BAS connected_batteries ${cnt}

# Prints info for each battery.
for i in $dir; do
    curdir=${i%/*}
    if [ -f ${curdir}/manufacturer ]; then
        manufacturer=$(cat ${curdir}/manufacturer)
        name=${manufacturer}
    fi
    if [ -f ${curdir}/model_name ]; then
        model_name=$(cat ${curdir}/model_name)
        name=${name}-${model_name}
    fi
    if [ -f ${curdir}/serial_number ]; then
        serial_number=$(cat ${curdir}/serial_number | sed 's/ //g')
        name=${name}-${serial_number}
    fi

    # Specify the battery only if there are more than 1.
    if [ $cnt -gt 1 ]; then
        fieldsuffix="(${name})"
    fi
    if [ ! -z "${manufacturer}" ]; then
        echo VALUE BAS manufacturer${fieldsuffix} ${manufacturer}
    fi
    if [ ! -z "${model_name}" ]; then
        echo VALUE BAS model_name${fieldsuffix} ${model_name}
    fi
    if [ ! -z "${serial_number}" ]; then
        echo VALUE ADV serial_number${fieldsuffix} ${serial_number}
    fi
    if [ -f ${curdir}/status ]; then
        status=$(cat ${curdir}/status)
        echo VALUE BAS status${fieldsuffix} ${status}
    fi
    if [ -f ${curdir}/capacity ]; then
        capacity=$(cat ${curdir}/capacity)
        echo VALUE BAS capacity${fieldsuffix} ${capacity}%
    fi
    if [ -f ${curdir}/technology ]; then
        technology=$(cat ${curdir}/technology)
        echo VALUE ADV technology${fieldsuffix} ${technology}
    fi
    if [ -f ${curdir}/voltage_now ]; then
        voltage=$(cat ${curdir}/voltage_now)
        if [ ! -z "$voltage" ]; then
            hrvoltage=$(($voltage / 1000000))
            hrvoltage=${hrvoltage}.$((($voltage / 100000) % 10))
            hrvoltage=${hrvoltage}$((($voltage / 10000) % 10))
            echo VALUE ADV current_voltage${fieldsuffix} ${hrvoltage}V
        fi
    fi
    if [ -f ${curdir}/power_now ]; then
        power=$(cat ${curdir}/power_now)
        hrpower=$(($power / 1000000))
        hrpower=${hrpower}.$((($power / 100000) % 10))
        hrpower=${hrpower}$((($power / 10000) % 10))
        echo VALUE ADV power_now${fieldsuffix} ${hrpower}W
    fi
    if [ -f ${curdir}/energy_now ]; then
        energy=$(cat ${curdir}/energy_now)
        hrenergy=$(($energy / 1000000))
        hrenergy=${hrenergy}.$((($energy / 100000) % 10))
        hrenergy=${hrenergy}$((($energy / 10000) % 10))
        echo VALUE ADV energy_now${fieldsuffix} ${hrenergy}Wh
        if
            [ -f ${curdir}/power_now ] &
            [ "$power" -gt 0 ]
        then
            hrhoursleft=$((${energy} / ${power}))
            hrhoursleft=${hrhoursleft}.$(((${energy} * 10 / ${power}) % 10))
            echo VALUE BAS remaining_hours${fieldsuffix} ${hrhoursleft}
        fi
    fi
    if [ -f ${curdir}/energy_full_design ]; then
        energy_full_design=$(cat ${curdir}/energy_full_design)
        hrenergyfull=$(($energy_full_design / 1000000))
        hrenergyfull=${hrenergyfull}.$((($energy_full_design / 100000) % 10))
        hrenergyfull=${hrenergyfull}$((($energy_full_design / 10000) % 10))
        echo VALUE ADV energy_full_design${fieldsuffix} ${hrenergyfull}Wh
        if [ -f ${curdir}/energy_full ]; then
            echo VALUE ADV health${fieldsuffix} $(($(cat ${curdir}/energy_full) * 100 / $(cat ${curdir}/energy_full_design)))%
        fi
    fi

done
