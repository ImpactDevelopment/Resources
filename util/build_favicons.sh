#!/bin/bash

declare -A icons=(
    ["apple-touch-icon"]="57 60 72 76 114 120 144 152"
    ["favicon"]="16 32 96 128 196 256"
)

file() {
    printf "$1-%sx%s.png " $2
    echo ""
}

mkdir -p "textures/favicon"

echo "${icons[favicon]}"
for name in "${!icons[@]}"; do
    for size in ${icons[$name]}; do
    file="${name}-${size}x${size}.png"
    echo "Building textures/favicon/${file}"
    rsvg-convert -h "${size}" -f "png" "textures/Icon.svg" > "textures/favicon/${file}"
    done
done

echo "Building textures/favicon/favicon.ico"
magick -background transparent "textures/favicon/favicon-*.png" "textures/favicon/favicon.ico"
