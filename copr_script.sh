#!/bin/bash

set -euo pipefail

PKGNAME="netfoil"
VERSION="1.0"
SRC_REPO="https://github.com/tinfoil-factory/$PKGNAME.git"
SPEC_FILE="$PKGNAME.spec"

# Get source
git clone "$SRC_REPO" "$PKGNAME-$VERSION"
rm -rf "$PKGNAME-$VERSION/.git"

# Create tarball
tar -czf "$PKGNAME-$VERSION.tar.gz" "$PKGNAME-$VERSION"
rm -rf "$PKGNAME-$VERSION"

# Get RPM
git clone "https://github.com/simen64/$PKGNAME-rpm"
mv netfoil-rpm/$PKGNAME.spec ./
rm -rf "$PKGNAME-rpm"
