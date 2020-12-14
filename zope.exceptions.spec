#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.exceptions
Version  : 4.4
Release  : 31
URL      : https://files.pythonhosted.org/packages/41/c5/84f68fa73055d6a6937e55ee31888e5a8ca4a877a192e4a844f9fcacd00d/zope.exceptions-4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/c5/84f68fa73055d6a6937e55ee31888e5a8ca4a877a192e4a844f9fcacd00d/zope.exceptions-4.4.tar.gz
Summary  : Zope Exceptions
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.exceptions-license = %{version}-%{release}
Requires: zope.exceptions-python = %{version}-%{release}
Requires: zope.exceptions-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface
BuildRequires : zope.testrunner-python

%description
zope.exceptions
        =================

%package license
Summary: license components for the zope.exceptions package.
Group: Default

%description license
license components for the zope.exceptions package.


%package python
Summary: python components for the zope.exceptions package.
Group: Default
Requires: zope.exceptions-python3 = %{version}-%{release}

%description python
python components for the zope.exceptions package.


%package python3
Summary: python3 components for the zope.exceptions package.
Group: Default
Requires: python3-core
Provides: pypi(zope.exceptions)
Requires: pypi(setuptools)
Requires: pypi(zope.interface)

%description python3
python3 components for the zope.exceptions package.


%prep
%setup -q -n zope.exceptions-4.4
cd %{_builddir}/zope.exceptions-4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594928138
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.exceptions
cp %{_builddir}/zope.exceptions-4.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.exceptions/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.exceptions/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
