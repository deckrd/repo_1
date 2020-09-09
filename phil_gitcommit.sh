#!/bin/bash

git add *
git config --global user.email "phlpvst@gmail.com"
git config --global user.name "deckrd"
echo Navn til commit?
read commit
git commit -m $commit
git push
