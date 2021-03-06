#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.exceptions
Version  : 4.5
Release  : 47
URL      : https://files.pythonhosted.org/packages/1b/63/7e651aba4d137405d8a6eafb911a51a457c7efce727798c027db1f290963/zope.exceptions-4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/1b/63/7e651aba4d137405d8a6eafb911a51a457c7efce727798c027db1f290963/zope.exceptions-4.5.tar.gz
Summary  : Zope Exceptions
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.exceptions-license = %{version}-%{release}
Requires: pypi-zope.exceptions-python = %{version}-%{release}
Requires: pypi-zope.exceptions-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=================
zope.exceptions
=================
.. image:: https://img.shields.io/pypi/v/zope.exceptions.svg
:target: https://pypi.python.org/pypi/zope.exceptions/
:alt: Latest release

%package license
Summary: license components for the pypi-zope.exceptions package.
Group: Default

%description license
license components for the pypi-zope.exceptions package.


%package python
Summary: python components for the pypi-zope.exceptions package.
Group: Default
Requires: pypi-zope.exceptions-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.exceptions package.


%package python3
Summary: python3 components for the pypi-zope.exceptions package.
Group: Default
Requires: python3-core
Provides: pypi(zope.exceptions)
Requires: pypi(setuptools)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-zope.exceptions package.


%prep
%setup -q -n zope.exceptions-4.5
cd %{_builddir}/zope.exceptions-4.5
pushd ..
cp -a zope.exceptions-4.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656359444
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.exceptions
cp %{_builddir}/zope.exceptions-4.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.exceptions/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.exceptions/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
