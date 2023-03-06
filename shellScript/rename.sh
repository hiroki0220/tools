#!/bin/bash

# 変更したい親ディレクトリに移動する
cd work

# ディレクトリ内のすべてのディレクトリについてループする
for directory in */
do
    # ディレクトリ内のすべてのファイルについてループする
    for file in "$directory"*
    do
        if [ `echo $file | grep '[変更]'` ] ; then
            # ファイル名を取得する
            filename=$(basename "$file")
            # ファイル名の最初の4文字を抽出する
            newname=${filename:0:4}
            # ファイル名を変更する
            echo $directory$newname.${file##*.}
            mv "$file" "$directory/$newname${filename##*.}"
        fi
    done
done
