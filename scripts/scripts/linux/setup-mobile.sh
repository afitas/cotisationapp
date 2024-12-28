#!/bin/bash

# Installation des dépendances React Native
cd mobile
npm install

# Configuration iOS
cd ios
pod install
cd ..

# Configuration Android
cd android
./gradlew clean 