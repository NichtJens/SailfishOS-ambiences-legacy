#!/bin/bash

rpmbuild --target noarch --define "_topdir ${PWD}"  -bb ambiences-legacy.spec
rm -r BUILD SOURCES SPECS SRPMS


