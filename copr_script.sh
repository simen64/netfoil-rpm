#!/bin/bash

# pre copr script
#git clone "https://github.com/simen64/netfoil-rpm"
#bash ./netfoil-rpm/copr_script.sh

set -euo pipefail

PKGNAME="netfoil"
VERSION="1.0"
SRC_REPO="https://github.com/tinfoil-factory/$PKGNAME.git"
SPEC_REPO="https://github.com/simen64/$PKGNAME-rpm"
SPEC_FILE="$PKGNAME.spec"

# Get source
git clone "$SRC_REPO" "$PKGNAME-$VERSION"
rm -rf "$PKGNAME-$VERSION/.git"

# Get go dependencies
cd "$PKGNAME-$VERSION"/ 
go mod vendor
cd ..

# Create tarball
tar -czf "$PKGNAME-$VERSION.tar.gz" "$PKGNAME-$VERSION"
rm -rf "$PKGNAME-$VERSION"

# Get spec
git clone "$SPEC_REPO"

# Cleanup
mv $PKGNAME-rpm/$PKGNAME.spec ./
rm -rf "$PKGNAME-rpm"
