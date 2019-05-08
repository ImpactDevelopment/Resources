#!/bin/bash

for ICON in "Icon" "Pepsi"; do
    for SIZE in "16" "32" "64" "128" "256" "512" "1024" "2048" "4096"; do
        echo "Building textures/${ICON}_${SIZE}.png"
        rsvg-convert -h "${SIZE}" "textures/${ICON}.svg" > "textures/${ICON}_${SIZE}.png"
    done
done
