find . -mindepth 2 -type f | while read f; do
    # Extract filename and parent folder name
    folder=$(basename "$(dirname "$f")")
    file=$(basename "$f")
    dest="./${folder}_${file}"

    # If destination already exists, add a unique suffix
    if [ -e "$dest" ]; then
        base="${file%.*}"
        ext="${file##*.}"
        dest="./${folder}_${base}_$(date +%s%N).${ext}"
    fi

    mv "$f" "$dest"
done
